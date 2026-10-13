## Проверка тем, native typography и документированных технологий

Все 23 публичных store histories и доступные первичные help/design-источники проверены повторно. Таблица отделяет наличие функции в документации от её визуального исполнения в конкретном snapshot. Полный журнал: [v2-themes-type.md](v2-themes-type.md); машинная матрица: [v2-themes-type.json](v2-themes-type.json).

| № | Приложение | Темы: подтверждённое состояние | Типографика: точная атрибуция | Технологические сведения |
|---:|---|---|---|---|
| 1 | BeFit | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | Спецификация реализации не найдена |
| 2 | MacroFactor Nutrition | System, Light, Dark | Macro Sans — ecosystem, не исчерпывающий native font inventory | motion: Космические in-app illustrations/animations для onboarding и weekly check-ins официально описаны; engine/easing не раскрыты. |
| 3 | Fitbod | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | Спецификация реализации не найдена |
| 4 | Gymverse | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | Спецификация реализации не найдена |
| 5 | TRX | Проверено; публично не установлено | Montserrat — только brand communications | Спецификация реализации не найдена |
| 6 | Muscle Booster | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | audio_feedback: Голос называет упражнение и начало/конец интервала; его можно отключить отдельно от музыки. |
| 7 | Strava | Phone default, Light Mode, Dark Mode | Не раскрыта в проверенных native источниках | theme_accessibility: Phone default/Light/Dark — документированная настройка восприятия; наличие темы не равно WCAG соответствию. |
| 8 | Lyfta | Пункт Theme виден; варианты публично не установлены | Не раскрыта в проверенных native источниках | Спецификация реализации не найдена |
| 9 | Fitify | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | Спецификация реализации не найдена |
| 10 | FitOn | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | Спецификация реализации не найдена |
| 11 | SmartGym | Dark Mode (documented) | Не раскрыта в проверенных native источниках | materials: Официально Apple Liquid Glass; в 8.0.3 расширен на segmented controls, muscle-group picker, alerts и duration timer.; motion: Haptic Feedback — прямо указанная технология; параметры/виды импульсов не раскрыты.; accessibility: Accessibility APIs указаны; Voice Over for HIIT Workouts не интерпретирован как полное покрытие Apple VoiceOver screen reader. |
| 12 | BODi | System (default follows iPhone), Light, Dark | Не раскрыта в проверенных native источниках | materials: Релиз 11.3.0 прямо заявляет iOS 26 Liquid Glass; это более новая документация, чем возможная старая flat выборка. |
| 13 | Gymdone | Только Light/Dark веб-демо; native unknown | Не раскрыта в проверенных native источниках | Спецификация реализации не найдена |
| 14 | Technogym | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | Спецификация реализации не найдена |
| 15 | Buddyfit | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | accessibility: Заявлена базовая совместимость iOS VoiceOver и Android TalkBack; производитель признаёт неполные labels и возможную ненадёжность dynamic text. WCAG2.1AA назван ориентиром, не результатом полного прохождения. |
| 16 | Strong | Dark Mode (documented), Custom themes (names not fully documented) | Не раскрыта в проверенных native источниках | materials: Release note о readability fix у Calendar highlight прямо называет Liquid Glass theme; общий охват приложения/API не детализирован.; accessibility: Разработчик заявляет improved support for Show Borders. Это конкретная поддержка accessibility setting, не полная сертификация. |
| 17 | JEFIT | Dark Mode (release-note confirmed) | Не раскрыта в проверенных native источниках | materials: Liquid Glass прямо заявлен для navigation, sheets и menus на iOS 26.; motion: Onboarding entrance animations и haptics заявлены developer notes; confetti относится к завершению training phase, не произвольно каждому PR. |
| 18 | Muscle Monster | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | typography_version_change: Разработчик сообщает об обновлённом app font без имени семьи; улучшены male English voice и добавлен female English voice. |
| 19 | SHRED | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | materials: Improved Liquid Glass Layout: UI components обновлены, CoachAI перенесён в floating Talk to Coach; доступно iOS 26+. Это заявленный design-language rollout, не измерение физики. |
| 20 | Symmetry | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | motion: New rank-up animation в 7.15.0; animated streak screen в 7.13.0; redesigned rank icons/colors и немедленное celebration screen в 7.12.0. Длительность/easing/library не раскрыты. |
| 21 | Gravl | Light, Original (dark), System, Custom: Stealth, Custom: Pulse, Custom: Rose | Не раскрыта в проверенных native источниках | motion: Paused подтверждается сообщением и мигающей точкой; это документированный feedback, не deduced animation engine. |
| 22 | Peloton | Light, Dark | SF Pro — iOS; Inter — Android | accessibility: Официально описана поддержка subtitles для on-demand и live English content; актуальный охват каждого player/platform отдельно не тестировался. |
| 23 | MCI | Проверено; публично не установлено | Не раскрыта в проверенных native источниках | haptic_feedback: Apple Watch вибрирует по окончании отдыха; характер iPhone haptics остаётся неизвестен. |

Версионные qualifiers, первичные URL и даты относятся к отдельным фактам в JSON/индивидуальных блоках. Неуказанная Accessibility-декларация App Store не равна отсутствию поддержки; положительные и отрицательные факты Buddyfit, SmartGym, Strong иMCI приведены отдельно.
