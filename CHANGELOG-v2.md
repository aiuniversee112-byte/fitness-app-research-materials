# Изменения редакции 2

Дата:11 октября 2026. Первая редакция сохранена в revisions/v1. Все 23 приложения и 138 разделов сохранены; Symmetry иMCI остаются в согласованном списке.

## Существенные исправления

- **Gymdone:** редкая первая выборка пропустила реальный microcycle. Плотно проверены зарегистрированный warm-up, автоматический rest, увеличение времени, закрытие rest, следующий подход и finish. Старое ограничение заменено конкретной границей короткого тестового сценария.
- **BeFit:** подтверждены First Streak, glow и движущееся конфетти. Отдельно установлено, что пользовательский файл демонстрирует ручной Register workout; выдавать его за активный set/rest нельзя.
- **FitOn:** active iPhone player теперь подтверждён публичной записью 2026. Добавлены countdown/orientation/transport/early exit/Resume и официальные HR-зоны. Full successful finish не подменён ранним выходом.
- **Gravl:** напрямую просмотрены реальные Warmup/Effective tables, retro-log, редактирование reps/weight, Save и dropset-жест. Ретроспективные сценарии отделены от live auto-rest.
- **Peloton:** добавлены исторические мобильный class-player2021 и Gym2023, включая weight/reps sheet и 2D body-map. Их актуальность не распространена автоматически на 2026.
- **Muscle Monster:** найден advertised player. Из-за несовпадения подписи Stationary Bike Run с демонстрацией жима гантелей он классифицирован как несогласованная рекламная композиция, а не новый live HUD.
- **Fitify/SmartGym/BODi:** добавлены реальные исторические рабочие записи с явными датами/платформами; старые цвета и интервалы перемотки не перенесены на нынешние screenshots.
- **Технологии:** официально подтверждены version-scoped LiquidGlass-сведения SmartGym/BODi/JEFIT/SHRED, более узкая LiquidGlass theme уStrong; старое обобщение «нигде не доказано» удалено.
- **Темы/типографика:** подтверждены Light/Dark settings Peloton иBODi; Peloton Kinetic использует SFPro/iOS иInter/Android. TRX Montserrat оставлен brand-only. Для всех 23 выполнена отдельная проверка источников; неизвестные native families не подменены webCSS.
- **Accessibility/motion:** внесены конкретные ограничения Buddyfit, developer claims SmartGym/Strong, animations Symmetry иAppleWatch feedback MCI.

## Техническая точность

- **Strong:** добавлены реальные исторические countdown→Rest Complete, Finish confirmation→summary→template и альтернативная inline rest bar.
- **Strava:** добавлены реальная Android-запись2026 карта↔статистика и цепочка Pause→Finish→Save2025.
- **Lyfta:** проверены logging, completed rows, валидация пустого finish, Undo и discard; RestTimer:Off явно отделён от elapsed. Успешный finish и countdown не приписаны этому сеансу.

- Измерены 17 числовых образцов в масштабе 430u по короткой стороне экрана. Значения обозначают видимые штрихи, не font-size.
- Рассчитаны 12 цветовых пар по формуле относительной яркостиW3C. Это single-state samples, не сертификацияWCAG.
- Исправлена методика обзорных таймкодов: первоначальный filename t соответствует запросу t+1 с; плотные серии имеют явные times.
- Добавлены проверяемые search logs, локальные кадры, source manifests, version/platform qualifiers.
- Создан audit-structured.json:23 объекта, каждый содержит metadata,6 секций, benchmark row и documentary evidence.
- Сборка проверяет 23 блока,138 секций,23 строки финальнойматрицы, валидные screen IDs и локальные ссылки, отсутствие перенесённых email.

## Граница результата

Неизвестные внутренние font stacks/tnum, spring/easing, haptics телефона, accessibility tree, profiling и актуальные закрытые workout-state нельзя достоверно получить из рекламных изображений или чужого старого видео. Реальный player MuscleMonster и современный full successful finish некоторых сервисов требуют нового доступа/записи. Пакет фиксирует выполненную проверку и оставшуюся границу; он не выдаёт заполненные словами поля за измеренные свойства.
