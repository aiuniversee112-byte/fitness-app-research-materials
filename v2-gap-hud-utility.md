# V2 — Strava / Lyfta / Strong: проверка реального core motion

Дата проверки: 2026-10-11. Дополнительный публичный video evidence; это **не** пользовательский Video Archive и не новый AppLlama capture. Основной отчёт не изменён. Артефакты: `v2-media/utility/`.

## Ответ

Для Strava найдены реальные переключения нового recorder в 2026 году и отдельная историческая цепочка record → pause → finish → save. Для Strong визуально подтверждены logging, реальный rest countdown, достижение нуля, finish confirmation и post-workout/template. Для Lyfta подтверждены реальные logging, валидация пустого завершения и discard; работающий rest countdown и успешное сохранение пока не подтверждены видео.

## Ключевые находки

### Проверенные источники

Даты — публикация из сохранённого YouTube `.info.json`, не гарантированная дата записи/версия сборки. Все записи сторонние; визуальный сеанс служит первичным свидетельством именно показанного UI. Промокод автора Lyfta означает коммерческую заинтересованность, но наблюдаемые действия отделены от его оценок.

| ID | Источник | Дата / платформа | Проверенный интервал | Артефакты |
|---|---|---|---|---|
| U-ST1 | [How to Use the New Record Experience — 4kEasyGuide](https://www.youtube.com/watch?v=XsP_7DtGNrQ) | 2026-04-30; Android, физический handset и видимый палец; build неизвестен | 00:10–00:47: sport sheet, start, live timer, карта ↔ крупная статистика | `XsP_7DtGNrQ.mkv`, `.info.json`, `strava-new-board-1.jpg`, `strava-new-board-2.jpg`, `strava-new-*.png` |
| U-ST2 | [How To Use Strava App For Beginners — Thrive Media](https://www.youtube.com/watch?v=INgtDl2Rj0g) | **2025-05-26**, Android; «2026» в заголовке не соответствует upload date | 02:28–03:04: start → metrics → pause → finish → Save Activity → first-run feedback | `INgtDl2Rj0g.webm`, `.info.json`, `strava-old-board-1.jpg`, `strava-old-board-2.jpg`, `strava-old-*.png` |
| U-SR1 | [How to Use the Strong Workout App — KevTheTrainer](https://www.youtube.com/watch?v=JtFDmIhGicg) | 2025-01-01; iPhone/iOS, физический handset + screen recording. В summary видна дата тренировки 2024-12-31 | 00:52–01:38: input → rest picker → countdown → Rest Complete → Finish → summary → template | `JtFDmIhGicg.webm`, `.info.json`, `strong-correct-board-1.jpg`, `strong-correct-board-2.jpg`; точный кадр `strong-rest-complete-74.png` |
| U-SR2 | [STRONG APP 2026 Review — Peter Burianek](https://www.youtube.com/watch?v=4sR5xNAL3as) | **2025-09-28**; cropped portrait recording, платформа не установлена надёжно; German UI | 08:42–11:42 overview; 08:56–09:36 detailed extraction: отметка подхода → inline rest bar; затем finish/summary | `4sR5xNAL3as.mkv`, `.info.json`, `strong-second-board.jpg`, `strong-second-0550.png`, `strong-inline-*.png` |
| U-LY1 | [Good Gym App For Tracking Progress (Lyfta) — The Viglot](https://www.youtube.com/watch?v=mfAZYWEpOFk) | 2024-11-12; Android, системная строка/Google Play; исторический интерфейс | 02:24–03:12: добавить упражнение → ввод → error on finish → set checks → discard | `mfAZYWEpOFk.webm`, `.info.json`, `lyfta-detail-1.jpg`, `lyfta-detail-2.jpg`, `lyfta-detail-3.jpg`, `lyfta-*.png` |
| U-REJECT1 | [Lyfta vs Hevy — TWiz](https://www.youtube.com/watch?v=63_HHVb3iX8) | 2026-07-08 | Проверен обзорный board; **отклонён целиком** | `63_HHVb3iX8.mkv`, `.info.json`, `lyfta-second-board.jpg`: автор демонстрирует образовательный Lyfta, а не workout tracker, и сравнивает сайты. Источник нельзя использовать даже для функций Lyfta Fitness |

### Готовые точечные дополнения к motion/HUD

**Strava [U-ST1, U-ST2].** В записи Android 2026 года нижняя панель статистики раскрывается до полноэкранных крупных чисел и возвращается к карте; elapsed продолжает расти. Оранжевая широкая Pause остаётся внизу в обоих режимах. В исторической записи 2025 года после Pause появляются отдельные Resume/Finish, Finish открывает прокручиваемую Save Activity форму, а Save приводит к первому поздравлению и социальному onboarding. Первый-run reward нельзя обобщать на каждую тренировку. Старый круглый orange Finish не следует смешивать с чёрным Finish актуального официального iPhone screenshot из ST-D1.

**Strong [U-SR1, U-SR2].** На iPhone выбор 1:00 в большой белой Rest Timer card запускает уменьшение крупного числового остатка и синей дуги; в центре отдельно остаётся исходная длительность 1:00, снизу доступны −10s/+10s/Skip. В 01:14 реально виден Rest Complete с trophy поверх затемнённого журнала. Finish требует подтверждения; затем показаны Well Done, три жёлтые звезды, workout summary и 9 Personal Records, после чего предлагается сохранить template. U-SR2 дополнительно показывает **другой** presentation: после зелёной отметки подхода синий горизонтальный rest bar с убывающим числом появляется прямо под строкой. Это различие capture/platform/version, а не основание объявлять один вариант универсальным.

**Lyfta [U-LY1].** Исторический Android logger имеет сворачиваемые упражнения, колонки Previous/Kg/Reps и числовую клавиатуру. Отметка подходов меняет фон строк и checks на зелёный. Попытка закончить с нулём completed sets вызывает modal с требованием отметить хотя бы один; удаление даёт Undo snackbar, discard требует подтверждения. Во всём проверенном эпизоде явно написано Rest Timer: Off: elapsed тренировки растёт, но это **не** rest countdown. Этот источник закрывает реальную динамику ввода и ошибок, не rest/успешный finish.

## Подробности

### Границы вывода

- Просмотрено шесть новых видео через contact sheets; подробные интервалы каждого принятого core-сеанса изучены с шагом около 2 секунд. Для Strong Rest Complete дополнительно извлечён и просмотрен точный кадр 01:14. Это покадровая проверка состояний и последовательности, а не замер performance на устройстве.
- U-ST2 и U-SR1 содержат монтаж/ускорение. В Strong остаток перескакивает с ~0:57 к ~0:02 между сценами. Нельзя считать это фактической длительностью минуты или «скачком» приложения. Easing, spring parameters, haptics, 60/120 fps и используемые Lottie/Rive/framework не установлены.
- В U-ST1 видны физические касания и переходы map/stats, однако нет Finish/Save. В U-ST2 запись телефона вставлена в рамку, но внутри реально меняются elapsed, pace, GPS, формы и навигация: она принята как запись сеанса, а не как marketing composition. Внешние стрелки/фон не являются элементами Strava.
- `strong-detail-*.jpg` — ранние увеличенные crops с обрезанным правым краем; для экспорта использовать **strong-correct-board** и полное исходное видео. FFmpeg boards дают обзорные таймкоды с точностью примерно ±1 секунды; cv2 `lyfta-*.png` / `strong-*.png` сохраняют запрошенные позиции. Для измерений применять исходные записи, не boards.
- Остаточный gap: Lyfta rest activation/countdown/completion и успешный finish не наблюдены; текущие 2026 Strong iOS/Android версии и Strava iOS motion не проверены этими историческими роликами. Эти ограничения не означают отсутствия функций.

### Журнал маршрутов

Agent-reach YouTube backend: `yt-dlp --flat-playlist --dump-json ytsearch...`; затем публичные URL загружены с `--js-runtimes node`, без cookies/login. Обработаны запросы `Lyfta app workout tutorial`, `Strong app rest timer workout tutorial`, `Strava record pause save activity tutorial 2026`, `Lyfta rest timer`, `Strong workout app timer rest tutorial`, `Strong app rest timer settings`. Множество нерелевантных exercise videos и generic review titles не принимались по заголовку. После обнаружения ошибочного сравнения U-REJECT1 дальнейший перебор таких how-to остановлен. Изначальный format selector не нашёл combined streams; использован обычный video+audio selector. `source-manifest.json` хранит компактную provenance-матрицу; полные метаданные каждого источника сохранены рядом. `agent-reach check-update`: установленная v1.5.0 актуальна.
