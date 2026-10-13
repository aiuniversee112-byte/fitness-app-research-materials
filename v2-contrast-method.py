"""E040: reproduce the 12 raster contrast samples from the design audit.

Requirements: Python 3, Pillow, numpy.
Run: python v2-contrast-method.py --output contrast-recomputed.json
Without --output, results are printed; the historical E041 file is not modified.
These are measurements of individual raster states, not app accessibility scores.
"""
from pathlib import Path
import argparse
import json
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent
SELECTED = {1: 'reps', 3: 'hold timer', 4: 'set seconds', 7: 'speed',
            8: 'rest pill', 9: 'interval seconds', 11: 'rest timer',
            13: 'kg reps', 16: 'elapsed', 17: 'rest timer',
            20: 'elapsed', 23: 'elapsed'}


def luminance(rgb):
    channels = np.array(rgb) / 255
    linear = np.where(channels <= .04045, channels / 12.92,
                      ((channels + .055) / 1.055) ** 2.4)
    return float(linear @ [.2126, .7152, .0722])


def measure():
    samples = json.loads((ROOT / 'v2-measurements/numeric-measurements.json').read_text(encoding='utf-8'))
    result = []
    for sample in samples:
        if sample['number'] not in SELECTED:
            continue
        # Original metadata used Windows separators. Accept both on every OS.
        path = ROOT / sample['image'].replace('\\', '/')
        rgb = np.array(Image.open(path).convert('RGB'))
        x, y, width, height = sample['bbox_px']
        roi = rgb[y:y + height, x:x + width]
        quantized = (roi // 4) * 4
        colors, counts = np.unique(quantized.reshape(-1, 3), axis=0, return_counts=True)
        order = counts.argsort()[::-1]
        background = colors[order[0]]
        foreground = next(color for color in colors[order[1:]]
                          if np.linalg.norm(color.astype(float) - background) > 45)
        b = roi[np.all(quantized == background, axis=2)].mean(0)
        f = roi[np.all(quantized == foreground, axis=2)].mean(0)
        lo, hi = sorted([luminance(b), luminance(f)])
        result.append({'number': sample['number'], 'app': sample['app'],
                       'role': SELECTED[sample['number']],
                       'background_sample_rgb': b.round(1).tolist(),
                       'foreground_sample_rgb': f.round(1).tolist(),
                       'contrast_ratio': round((hi + .05) / (lo + .05), 2),
                       'source': sample['source'], 'time_s': sample['time_s'],
                       'scope': 'single raster state, not app compliance'})
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(measure(), ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(text + '\n', encoding='utf-8')
    else:
        print(text)
