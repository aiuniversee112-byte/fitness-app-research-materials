# V2: темы, типографика, материалы, motion и accessibility — 23 приложения

Дата проверки: **2026-10-11**. Этот файл дополняет визуальный аудит. Он не заменяет анализ старых записей сведениями о текущем релизе. Машиночитаемая матрица: [v2-themes-type.json](v2-themes-type.json).

## Достоверные дополнения

- **Peloton:** Kinetic документирует **SF Pro для iOS и Inter для Android**. Это утверждение команды design/engineering в официальном кейсе Figma, а не определение по CSS. История iOS-релизов отдельно подтверждает Light/Dark toggle в Settings. Двенадцать тем Kinetic включают оформление команд и Strength+; считать их двенадцатью глобальными скинами приложения нельзя. [Figma case](https://www.figma.com/customers/peloton-speeds-up-design-handoff-by-5x-with-figma/)
- **BODi:** Light/Dark с системным режимом по умолчанию и override в Settings документированы в 11.1.0/11.2.0; Liquid Glass для iOS26 — в 11.3.0. Названия месяцев/дней в history сохранены без выдуманного года. [Developer release history](https://apps.apple.com/us/app/bodi-fitness-home-workouts/id1031660123)
- **SmartGym, JEFIT, SHRED:** есть прямые заявления об использовании Liquid Glass с ограничениями версии/платформы. У Strong release note упоминает именно Liquid Glass theme; это более узкое подтверждение. Их следует добавить рядом с результатами визуального наблюдения, а не переписать старый плоский screenshot как стеклянный.
- **Buddyfit:** официально заявляет базовую поддержку VoiceOver/TalkBack и одновременно признаёт неполные labels и ненадёжную реакцию некоторых областей на dynamic text. Это опубликованное ограничение, а не наша догадка по мелкому тексту. [Mobile accessibility statement, June 2025](https://www.buddyfit.club/de/accessibility)
- **Muscle Monster:** в 3.25.0 разработчик сообщает об обновлённом app font, но не называет семейство. **Symmetry** документирует rank-up/streak animations; **MCI** — вибрацию Apple Watch по окончании отдыха. Эти сведения закрывают наличие функции, но не её easing, длительность или качество реализации.

## Правила интерпретации

- **Подтверждено** означает, что источник прямо называет настройку/технологию. Это не самостоятельный performance или accessibility test.
- **Проверено, не установлено** означает отсутствие нужного утверждения в прочитанных публичных источниках. Не означает «функции нет» или «тема фиксирована».
- В разделах **Accessibility всех 23 текущих App Store listings** разработчик ещё не указал поддерживаемые функции. Это отсутствие декларации магазина; отдельная справка может содержать положительные и отрицательные факты.
- Native font family, `tnum`, haptics, accessibility tree, полноценная Dynamic Type support и параметры spring нельзя надёжно вывести из одного растрового изображения. Веб-CSS, учебные redesign-концепты и одноимённые продукты не используются как native evidence.
- `current_release_date_utc` в JSON — дата текущего релиза из Apple Lookup; `checked_on` — дата проверки; `date_label` — дата именно документа/release note. Эти поля не взаимозаменяемы.

## Краткая матрица

| № | Приложение | Темы | Типографика | Материалы / motion / accessibility |
|---|---|---|---|---|
| 1 | BeFit | Проверено; публичное подтверждение не найдено | Native family не установлен | Технической спецификации не найдено |
| 2 | MacroFactor Nutrition | Подтверждены пользовательские режимы: System, Light, Dark | Macro Sans — display; body неизвестен | Motion: документированные свойства |
| 3 | Fitbod | Проверено; публичное подтверждение не найдено | Native family не установлен | Технической спецификации не найдено |
| 4 | Gymverse | Проверено; публичное подтверждение не найдено | Native family не установлен | Технической спецификации не найдено |
| 5 | TRX | Проверено; публичное подтверждение не найдено | Montserrat — communications; native неизвестен | Технической спецификации не найдено |
| 6 | Muscle Booster | Проверено; публичное подтверждение не найдено | Native family не установлен | Технической спецификации не найдено |
| 7 | Strava | Подтверждены пользовательские режимы: Phone default, Light Mode, Dark Mode | Native family не установлен | Технической спецификации не найдено |
| 8 | Lyfta | Проверено; публичное подтверждение не найдено | Native family не установлен | Технической спецификации не найдено |
| 9 | Fitify | Проверено; публичное подтверждение не найдено | Native family не установлен | Технической спецификации не найдено |
| 10 | FitOn | Проверено; публичное подтверждение не найдено | Native family не установлен | Технической спецификации не найдено |
| 11 | SmartGym | Dark подтверждён; полный menu contract не раскрыт: Dark Mode (documented) | Native family не установлен | Liquid Glass: документирован, с оговорками; Motion: документированные свойства; A11y: отдельные документированные свойства |
| 12 | BODi | Подтверждены пользовательские режимы: System (default follows iPhone), Light, Dark | Native family не установлен | Liquid Glass: документирован, с оговорками |
| 13 | Gymdone | Только варианты официальной веб-демонстрации: Light (web-demo), Dark (web-demo) | Native family не установлен | Технической спецификации не найдено |
| 14 | Technogym | Проверено; публичное подтверждение не найдено | Native family не установлен | Технической спецификации не найдено |
| 15 | Buddyfit | Проверено; публичное подтверждение не найдено | Native family не установлен | A11y: отдельные документированные свойства |
| 16 | Strong | Dark + custom themes подтверждены частично: Dark Mode (documented), Custom themes (names not fully documented) | Native family не установлен | Liquid Glass: документирован, с оговорками; A11y: отдельные документированные свойства |
| 17 | JEFIT | Dark подтверждён; полный menu contract не раскрыт: Dark Mode (release-note confirmed) | Native family не установлен | Liquid Glass: документирован, с оговорками; Motion: документированные свойства |
| 18 | Muscle Monster | Проверено; публичное подтверждение не найдено | Font обновлён в 3.25.0; семья неизвестна | Технической спецификации не найдено |
| 19 | SHRED | Проверено; публичное подтверждение не найдено | Native family не установлен | Liquid Glass: документирован, с оговорками |
| 20 | Symmetry | Проверено; публичное подтверждение не найдено | Native family не установлен | Motion: документированные свойства |
| 21 | Gravl | Подтверждены пользовательские режимы: Light, Original (dark), System, Custom: Stealth, Custom: Pulse, Custom: Rose | Native family не установлен | Motion: документированные свойства |
| 22 | Peloton | Подтверждены пользовательские режимы: Light, Dark | SF Pro (iOS), Inter (Android), Kinetic scope | A11y: отдельные документированные свойства |
| 23 | MCI | Проверено; публичное подтверждение не найдено | Native family не установлен | Apple Watch haptics |

## Проверенные маршруты и границы по каждому приложению

### [1] BeFit

- **Текущий магазин:** 1.2.21; release date 2026-10-09T15:07:26Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Архив показывает dark, но официальный FAQ и текущая история магазина не устанавливают Light/Dark/System. Одноимённый BeFit другого издателя исключён.
- **Типографика:** Семейство native UI не раскрыто проверенными источниками. По screenshot/веб-CSS не определялось.
- **Материалы/motion/accessibility:** конкретные implementation facts в проверенных публичных источниках не установлены. Общее «smooth/intuitive» не засчитано как техническая спецификация.
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/befit-gym-workout-tracker/id6504535443) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_help](https://appbefit.com/help-center/) — Прочитан FAQ, включая редактирование чисел, Profile→Sounds и настройки плана; Theme/Light/Dark, font family и технические материалы не раскрыты.

### [2] MacroFactor Nutrition

- **Текущий магазин:** 5.8.9; release date 2026-09-24T15:08:27Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Подтверждены пользовательские режимы. Подтверждено именно для Nutrition; не перенесено из Workouts.
- **Документированный путь:** More → Theme.
- **Типографика:** Macro Sans подтверждён для брендового display/key headlines. Native body, numbers и tnum не раскрыты.
  - Macro Sans: ecosystem, не исчерпывающий native font inventory; logo/wordmark; key headlines and important messages. [Первичный источник](https://macrofactor.com/new-look/)
  - DM Sans: partner marketing graphics only. К native body не приравнивается. [Брендовый источник](https://macrofactor.com/brand-guidelines/)
- **Документированные свойства:**
  - Космические in-app illustrations/animations для onboarding и weekly check-ins официально описаны; engine/easing не раскрыты. Scope: brand update. Дата источника: 2025-09-16. [Источник](https://macrofactor.com/new-look/)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/macrofactor-macro-tracker/id1553503471) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_help](https://help.macrofactorapp.com/en/articles/73-switch-between-dark-and-light-mode) — Nutrition: More→Theme→System/Light/Dark; System следует телефону.
  - [official_product_design_announcement](https://macrofactor.com/new-look/) — Ребрендинг 16.09.2025: Macro Sans для логотипа/wordmark и ключевых headlines/messages; новые in-app illustrations/animations.
  - [official_brand_guide](https://macrofactor.com/brand-guidelines/) — DM Sans указан для партнёрских marketing images; это не доказательство body font приложения.

### [3] Fitbod

- **Текущий магазин:** 8.35.1; release date 2026-10-06T01:37:53Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Сведения о переключении не найдены в проверенных публичных источниках; это не утверждение о единственной теме.
- **Типографика:** Первичный кейс автора design system подтверждает саму систему, но не называет native fonts. Стороннее «similar to Brandon Grotesque» и storefront CSS отвергнуты.
- **Материалы/motion/accessibility:** конкретные implementation facts в проверенных публичных источниках не установлены. Общее «smooth/intuitive» не засчитано как техническая спецификация.
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/fitbod-gym-fitness-planner/id1041517543) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_help_search_api](https://help.fitbod.me/api/v2/help_center/articles/search.json?query=dark) — Read-only поиск вернул count 0; это только результат индекса справки, не отсутствие функции.
  - [official_help](https://help.fitbod.me/hc/en-us/sections/360012732693-App-Features) — Feature Overview не описывает theme/font contract.
  - [first_person_designer_case_study](https://www.bpowell.co/design/fitbod) — Principal designer описывает внедрение iOS/Android/web design system в конце 2021; семейства шрифтов и переключатель темы в тексте не названы.

### [4] Gymverse

- **Текущий магазин:** 8.8800; release date 2026-09-27T08:32:37Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Тёмная визуальная выборка не превращена в вывод dark-only. Сторонние GymApp repositories и icon Light/Dark/Tinted previews не относятся к theme engine Gymverse.
- **Типографика:** Семейство native UI не раскрыто проверенными источниками. По screenshot/веб-CSS не определялось.
- **Материалы/motion/accessibility:** конкретные implementation facts в проверенных публичных источниках не установлены. Общее «smooth/intuitive» не засчитано как техническая спецификация.
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/gymverse-gym-workout-planner/id1048454034) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_product_site](https://gymverse.app/) — Прочитан полный публичный product/FAQ; настройки theme и native typography не документированы.

### [5] TRX

- **Текущий магазин:** 10.8.17; release date 2026-10-01T15:37:15Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Сведения о переключении не найдены в проверенных публичных источниках; это не утверждение о единственной теме.
- **Типографика:** Montserrat — подтверждённая коммуникационная гарнитура бренда. Ни её, ни системное семейство нельзя объявлять точным native body font без app-specific evidence.
  - Montserrat: TRX communications, standard and italic weights. К native body не приравнивается. [Брендовый источник](https://www.trxtraining.com/pages/trx-branding)
- **Материалы/motion/accessibility:** конкретные implementation facts в проверенных публичных источниках не установлены. Общее «smooth/intuitive» не засчитано как техническая спецификация.
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/trx-strength-home-workouts/id949905528) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_help_faq](https://www.trxtraining.com/pages/getstarted-with-trx-app) — Проверен FAQ: app navigation/music controls; переключение app theme не описано.
  - [official_brand_guide](https://www.trxtraining.com/pages/trx-branding) — Montserrat назван primary typeface для TRX communications; native app UI явно не указан.

### [6] Muscle Booster

- **Текущий магазин:** 3.83.0; release date 2026-10-09T08:08:28Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Сведения о переключении не найдены в проверенных публичных источниках; это не утверждение о единственной теме.
- **Типографика:** Семейство native UI не раскрыто проверенными источниками. По screenshot/веб-CSS не определялось.
- **Документированные свойства:**
  - Голос называет упражнение и начало/конец интервала; его можно отключить отдельно от музыки. Scope: help screenshots разных платформ; не весь accessibility contract. Дата источника: 2025-12-03. [Источник](https://musclebooster.welltech.com/help-center/features-personalization/how-do-i-turn-off-the-background-music/)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/muscle-booster-workout-tracker/id1446447749) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_help_index_and_articles](https://musclebooster.welltech.com/help-center/features-personalization/) — Прочитан список features/preferences; глобальная тема и семейство native fonts не раскрыты.
  - [official_help](https://musclebooster.welltech.com/help-center/features-personalization/how-do-i-turn-off-the-background-music/) — Подтверждены отдельные voiceover/audio controls и голосовые сигналы интервалов; это не доказательство screen-reader support.

### [7] Strava

- **Текущий магазин:** 484.0.0; release date 2026-10-07T20:15:48Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Подтверждены пользовательские режимы. Доступность подтверждена справкой; вся Dark palette в старой выборке не измерена.
- **Документированный путь:** You → Settings → Preferences → Appearance.
- **Типографика:** Текущий native family не установлен. Найденный сторонний mirror Spandex brand PDF, неофициальные DESIGN.md с конфликтующими SF Pro/Inter и webCSS не использованы. Исторический дизайнерский кейс сейчас 404.
- **Документированные свойства:**
  - Phone default/Light/Dark — документированная настройка восприятия; наличие темы не равно WCAG соответствию. Scope: mobile app. Дата источника: 2026-09-14. [Источник](https://support.strava.com/en-us/articles/15401628-how-do-i-enable-dark-mode-on-strava)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/strava-run-bike-walk/id426826309) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_help](https://support.strava.com/en-us/articles/15401628-how-do-i-enable-dark-mode-on-strava) — You→Settings→Preferences→Appearance: Phone default/Light Mode/Dark Mode.
  - [designer_case_study_unavailable](https://www.designbyti.com/strava-brand) — Поисковый индекс содержит историческое brand-Maison-Neue утверждение автора; прямое чтение вернуло 404. Не использовано как подтверждение текущей native гарнитуры. **Полное чтение не удалось; не является положительным доказательством.**

### [8] Lyfta

- **Текущий магазин:** 1.163; release date 2026-10-01T15:51:47Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. В исходном UI есть пункт Theme, но публичная справка не устанавливает варианты/следование системе. Lyfta AI id6762280855 исключён как другой продукт.
- **Типографика:** Семейство не названо в проверенной справке/релизах. Одноимённые образовательные Lyfta design-system материалы и новый Lyfta AI не применялись.
- **Материалы/motion/accessibility:** конкретные implementation facts в проверенных публичных источниках не установлены. Общее «smooth/intuitive» не засчитано как техническая спецификация.
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/lyfta-gym-workout-tracker-log/id6443740936) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_help_index](https://support.lyfta.app/en) — Прочитаны доступные категории/статьи account, using app, devices: theme options и native typeface не документированы.

### [9] Fitify

- **Текущий магазин:** 1.135.1; release date 2026-10-05T08:52:38Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Сведения о переключении не найдены в проверенных публичных источниках; это не утверждение о единственной теме.
- **Типографика:** Проверен первичный кейс бывшего UX/UI designer. Семейство не названо; многочисленные Fitify учебные концепты не являются спецификацией продукта.
- **Материалы/motion/accessibility:** конкретные implementation facts в проверенных публичных источниках не установлены. Общее «smooth/intuitive» не засчитано как техническая спецификация.
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/fitify-home-workout-ai-coach/id1463386686) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_support_route](https://gofitify.com/contact) — Страница даёт email/social contact, но публичной спецификации тем и шрифтов нет; никто не был contacted.
  - [failed_official_route](https://gofitify.com/faq) — 404. Не посчитано успешным чтением. **Полное чтение не удалось; не является положительным доказательством.**
  - [first_person_designer_case_study](https://www.jakubfoglar.com/project/fitify) — Автор и iOS ID совпадают; кейс 2021 описывает refinement/reward moments, но не называет fonts/themes или motion engine.

### [10] FitOn

- **Текущий магазин:** v7.6.2; release date 2026-10-02T16:42:03Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Сведения о переключении не найдены в проверенных публичных источниках; это не утверждение о единственной теме.
- **Типографика:** Native font не установлен; первичный case study не раскрывает family. Personal redesign portfolios исключены.
- **Материалы/motion/accessibility:** конкретные implementation facts в проверенных публичных источниках не установлены. Общее «smooth/intuitive» не засчитано как техническая спецификация.
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/fiton-workouts-fitness-plans/id1442473191) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_help](https://help.fitonapp.com/en/collections/3984049-your-account) — Прочитан account-settings index: email/privacy/notifications/calendar; theme/font не раскрыты.
  - [vendor_primary_case_study](https://www.interactivelabs.com/case-studies/fiton) — Исполнитель iOS/Android/web описывает насыщенную палитру, real-time feedback и achievement badges; font family и dark switch не названы.
  - [official_related_web_statement](https://www.fitonhealth.com/accessibility) — Относится к FitOn Health website: font resizing/contrast/readers/keyboard; не перенесено как native FitOn app conformity.

### [11] SmartGym

- **Текущий магазин:** 8.0.3; release date 2026-09-16T03:24:24Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Dark подтверждён; полный menu contract не раскрыт. Положительный Dark Mode claim подтверждён; список ручных опций Light/System и точный путь не установлен.
- **Типографика:** Семейство native UI не раскрыто проверенными источниками. По screenshot/веб-CSS не определялось.
- **Документированные свойства:**
  - Официально Apple Liquid Glass; в 8.0.3 расширен на segmented controls, muscle-group picker, alerts и duration timer. Scope: iOS 26+ для LiquidGlass; текущий store8.0.3. Версия: 7.7 / 8.0.3. Дата источника: 2025-09-03 / Sep 16. [Источник](https://smartgymapp.com/releases/smartgym-7-7.html)
  - Haptic Feedback — прямо указанная технология; параметры/виды импульсов не раскрыты. Scope: feature inventory. Версия: 7.11. Дата источника: 2026-07-23. [Источник](https://smartgymapp.com/releases/smartgym-7-11.html)
  - Accessibility APIs указаны; Voice Over for HIIT Workouts не интерпретирован как полное покрытие Apple VoiceOver screen reader. Scope: feature inventory. Версия: 7.11. [Источник](https://smartgymapp.com/releases/smartgym-7-11.html)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/smartgym-gym-home-workouts/id922744883) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_release_notes](https://smartgymapp.com/releases/smartgym-7-7.html) — Liquid Glass в buttons/alerts/charts/views и Watch; функция требует iOS 26+, а базовый app поддерживает iOS 15+.
  - [official_technical_feature_list](https://smartgymapp.com/releases/smartgym-7-11.html) — Прямо перечислены Dark Mode, SwiftUI, Swift Charts, Haptic Feedback, Accessibility APIs; исчерпывающее accessibility покрытие не заявлено.

### [12] BODi

- **Текущий магазин:** 11.13.2; release date 2026-10-07T17:49:50Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Подтверждены пользовательские режимы. Developer release notes11.1.0/11.2.0; даты Apr 21/May 5 без явно указанного года.
- **Документированный путь:** Settings → override appearance (название конечного элемента не раскрыто).
- **Типографика:** Семейство native UI не раскрыто проверенными источниками. По screenshot/веб-CSS не определялось.
- **Документированные свойства:**
  - Релиз 11.3.0 прямо заявляет iOS 26 Liquid Glass; это более новая документация, чем возможная старая flat выборка. Scope: iOS 26. Версия: 11.3.0. Дата источника: May 18. [Источник](https://apps.apple.com/us/app/bodi-fitness-home-workouts/id1031660123)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/bodi-fitness-home-workouts/id1031660123) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [designer_case_study_partial_access](https://www.jdnco.com/case_study/bodi/) — Индекс прочитан: expanded headlines/mixed-font callouts; полный reader timeout. Native font family не получен; не используется как native proof. **Полное чтение не удалось; не является положительным доказательством.**
  - [official_statement_incomplete_render](https://www.bodi.com/us/en/accessibility-statement) — Страница открыта, но body statement не извлечён, только заголовок/оболочка; никакого compliance claim не добавлено.

### [13] Gymdone

- **Текущий магазин:** 3.8.7; release date 2026-10-11T06:44:53Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Только варианты официальной веб-демонстрации. Официально показаны два оформления app demo. Это не подтверждение ручного native switch или следование системе.
- **Типографика:** Native family не раскрыт. CSS современного Next.js маркетингового сайта не переносился в iPhone UI.
- **Материалы/motion/accessibility:** конкретные implementation facts в проверенных публичных источниках не установлены. Общее «smooth/intuitive» не засчитано как техническая спецификация.
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/gymdone-workout-planner-log/id1350534443) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_interactive_marketing_demo](https://gymdone.com/) — Light/Dark переключает веб-демо App appearance; сам сайт называет данные illustrative. Native settings contract не установлен.

### [14] Technogym

- **Текущий магазин:** 3.45.5; release date 2026-09-25T08:00:11Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Сведения о переключении не найдены в проверенных публичных источниках; это не утверждение о единственной теме.
- **Типографика:** Историческая кастомная typography оборудования подтверждена дизайнером, но не применена к native mobile app. Текущий family остаётся unknown.
- **Материалы/motion/accessibility:** конкретные implementation facts в проверенных публичных источниках не установлены. Общее «smooth/intuitive» не засчитано как техническая спецификация.
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/technogym-training-gym-app/id976506047) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_help_hub_unreachable](https://support.technogym.com/products/technogym-app) — Прямое чтение ранее вернуло SSL error; индекс страниц доступен, техническая спецификация тем/шрифтов не получена. **Полное чтение не удалось; не является положительным доказательством.**
  - [design_vendor_case_study](https://www.studiovisuale.it/it/all-projects/ux/technogym-wellness-experience-design) — Полностью прочитан кейс: custom pixel-font2010 и seven-segment digits относятся к оборудованию MyRun/GroupCycle; это не family текущего мобильного App.

### [15] Buddyfit

- **Текущий магазин:** 2026.20.0; release date 2026-10-05T08:32:25Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Сведения о переключении не найдены в проверенных публичных источниках; это не утверждение о единственной теме.
- **Типографика:** Семейство native UI не раскрыто проверенными источниками. По screenshot/веб-CSS не определялось.
- **Документированные свойства:**
  - Заявлена базовая совместимость iOS VoiceOver и Android TalkBack; производитель признаёт неполные labels и возможную ненадёжность dynamic text. WCAG2.1AA назван ориентиром, не результатом полного прохождения. Scope: iOS / Android mobile apps. Дата источника: June 2025. [Источник](https://www.buddyfit.club/de/accessibility)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/buddyfit-exercise-at-home/id1483572798) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_accessibility_statement](https://www.buddyfit.club/de/accessibility) — June 2025: mobile VoiceOver/TalkBack basic compatibility; возможны непомеченные controls/images и ненадёжное dynamic text resizing.
  - [vendor_case_study_scope_exclusion](https://www.thefancyfactory.com/en/portfolio/buddyfit-en/) — Автор делал logo animations/GIF для Instagram/social/website. Не использовано как доказательство in-app motion engine.

### [16] Strong

- **Текущий магазин:** 6.5.1; release date 2026-10-08T07:30:06Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Dark + custom themes подтверждены частично. Dark и custom themes официально существуют; полный список, System mode и точный settings path в проверенных документах не установлены.
- **Типографика:** Семейство native UI не раскрыто проверенными источниками. По screenshot/веб-CSS не определялось.
- **Документированные свойства:**
  - Release note о readability fix у Calendar highlight прямо называет Liquid Glass theme; общий охват приложения/API не детализирован. Scope: iOS app. Версия: 6.4.3. Дата источника: Jul 23. [Источник](https://apps.apple.com/us/app/strong-workout-tracker-gym-log/id464254577)
  - Разработчик заявляет improved support for Show Borders. Это конкретная поддержка accessibility setting, не полная сертификация. Scope: iOS app. Версия: 6.3.1. Дата источника: Apr 7. [Источник](https://apps.apple.com/us/app/strong-workout-tracker-gym-log/id464254577)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/strong-workout-tracker-gym-log/id464254577) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_product_site](https://www.strong.app/) — Прямо указан Dark Mode; полный перечень appearance options не опубликован.
  - [official_help](https://help.strongapp.io/article/132-strong-pro) — Help19 May 2021 перечисляет Custom Icons(iPhone) and Themes среди PRO features; нельзя считать актуальную цену/entitlement всех themes доказанной по этой старой статье.

### [17] JEFIT

- **Текущий магазин:** 17.2.7; release date 2026-10-09T16:01:26Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Dark подтверждён; полный menu contract не раскрыт. Dark Mode прямо подтверждён v17.0.8. Light виден в исходной выборке; точный путь/полный список modes не выводился из пользовательских Q&A/Reddit.
- **Типографика:** Семейство native UI не раскрыто проверенными источниками. По screenshot/веб-CSS не определялось.
- **Документированные свойства:**
  - Liquid Glass прямо заявлен для navigation, sheets и menus на iOS 26. Scope: iOS 26. Версия: 17.2.1. Дата источника: Sep 16. [Источник](https://apps.apple.com/us/app/jefit-workout-plan-gym-tracker/id449810000)
  - Onboarding entrance animations и haptics заявлены developer notes; confetti относится к завершению training phase, не произвольно каждому PR. Scope: iOS releases. Версия: 17.1.2 / 17.0.7. Дата источника: Aug 26 / May 22. [Источник](https://apps.apple.com/us/app/jefit-workout-plan-gym-tracker/id449810000)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/jefit-workout-plan-gym-tracker/id449810000) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_product_blog](https://www.jefit.com/blog/upcoming-enhancements-revamped-workout-tab-and-improved-exercise-screens) — Обновления UI и routes описаны, точное font family и полный theme menu не названы.

### [18] Muscle Monster

- **Текущий магазин:** 3.25.0; release date 2026-09-08T02:26:30Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Сведения о переключении не найдены в проверенных публичных источниках; это не утверждение о единственной теме.
- **Типографика:** В 3.25.0 явно обновлён app font, но гарнитура не названа. Поэтому старые визуальные guesses особенно ненадёжны.
- **Документированные свойства:**
  - Разработчик сообщает об обновлённом app font без имени семьи; улучшены male English voice и добавлен female English voice. Scope: native app release. Версия: 3.25.0. Дата источника: Sep 8. [Источник](https://apps.apple.com/us/app/muscle-monster-workout-planner/id6471547318)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/muscle-monster-workout-planner/id6471547318) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_help](https://supportcenter.musclemonster.fit/?from=officialweb) — Прочитан полный public help; settings/account/library guides не раскрывают theme switch или font family.

### [19] SHRED

- **Текущий магазин:** 5.5.5; release date 2026-10-08T16:03:26Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Liquid Glass — материал/дизайн-язык; сам по себе он не доказывает Light/Dark/System control.
- **Типографика:** Семейство native UI не раскрыто проверенными источниками. По screenshot/веб-CSS не определялось.
- **Документированные свойства:**
  - Improved Liquid Glass Layout: UI components обновлены, CoachAI перенесён в floating Talk to Coach; доступно iOS 26+. Это заявленный design-language rollout, не измерение физики. Scope: iOS 26+. Версия: 5.3.6. Дата источника: 12/17/2025. [Источник](https://apps.apple.com/us/app/shred-gym-home-workouts/id1439828095)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/shred-gym-home-workouts/id1439828095) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_faq](https://www.shred.app/faq) — Прочитаны публичные FAQ topics; global theme switch и native font family не описаны.

### [20] Symmetry

- **Текущий магазин:** 7.15.0; release date 2026-10-07T18:04:57Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Сведения о переключении не найдены в проверенных публичных источниках; это не утверждение о единственной теме.
- **Типографика:** Семейство native UI не раскрыто проверенными источниками. По screenshot/веб-CSS не определялось.
- **Документированные свойства:**
  - New rank-up animation в 7.15.0; animated streak screen в 7.13.0; redesigned rank icons/colors и немедленное celebration screen в 7.12.0. Длительность/easing/library не раскрыты. Scope: iOS developer release history. Версия: 7.15.0 / 7.13.0 / 7.12.0. Дата источника: 3d ago / Sep 17 / Sep 10 (labels captured 2026-10-11; year not inferred). [Источник](https://apps.apple.com/us/app/symmetry-gym-workout-tracker/id6474446718)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/symmetry-gym-workout-tracker/id6474446718) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_product_site](https://symmetry.club/en) — Прочитаны brand/product pages; theme menu и native family не документированы.

### [21] Gravl

- **Текущий магазин:** 1.53.4; release date 2026-10-05T21:47:54Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Подтверждены пользовательские режимы. System: Light/Rose для light; Original/Stealth/Pulse для dark. Light accents: Black/Blue/Violet/Rose/Emerald/Orange. New themes preview требует Keep this theme; dismiss отменяет preview. Настройка сохраняется на телефоне, не в account.
- **Документированный путь:** Profile → App preferences → Theme.
- **Типографика:** Share editor содержит выбор fonts, но имена native UI font не раскрыты. Шрифт editable social card не равен body font приложения.
- **Документированные свойства:**
  - Paused подтверждается сообщением и мигающей точкой; это документированный feedback, не deduced animation engine. Scope: mobile app. [Источник](https://gravl.ai/help/life-calling-pause-your-workout)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/gravl-ai-personal-trainer/id6450921637) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_help](https://gravl.ai/help/themes-change-how-gravl-looks) — 27 Sep 2026: полный путь и варианты Light/Original/System/Custom, Stealth/Pulse/Rose, light accent choices; настройка device-local.
  - [official_help](https://gravl.ai/help/life-calling-pause-your-workout) — Paused/Resumed confirmation и blinking status dot документированы; HUD layout отдельно исследует другой агент.

### [22] Peloton

- **Текущий магазин:** 15.134.0; release date 2026-10-08T17:27:33Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Подтверждены пользовательские режимы. Подтверждено developer notes15.119.4,15.119.5,15.120.0. следование системе не добавлен без прямого доказательства.
- **Документированный путь:** Settings → Light/Dark toggle.
- **Типографика:** Подтверждение изкейса design/engineering team, не web CSS. Это не доказательство каждого компонента старой записи: Kinetic внедрялся постепенно, Strength+создан с ним с самого начала.
  - SF Pro: iOS; Kinetic platform type variables. [Первичный источник](https://www.figma.com/customers/peloton-speeds-up-design-handoff-by-5x-with-figma/)
  - Inter: Android; Kinetic platform type variables. [Первичный источник](https://www.figma.com/customers/peloton-speeds-up-design-handoff-by-5x-with-figma/)
- **Документированные свойства:**
  - Официально описана поддержка subtitles для on-demand и live English content; актуальный охват каждого player/platform отдельно не тестировался. Scope: content ecosystem; historical article. Дата источника: 2021-12-03. [Источник](https://www.onepeloton.com/blog/hearing-accessibility)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/peloton-fitness-workouts/id792750948) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_customer_case_with_named_design_engineering_team](https://www.figma.com/customers/peloton-speeds-up-design-handoff-by-5x-with-figma/) — Kinetic использует platform typography variables: SF Pro iOS и Inter Android;12themes/24modes включают team colors и Strength+yellow, не 12global app skins.
  - [official_product_accessibility_article](https://www.onepeloton.com/blog/hearing-accessibility) — 3 Dec 2021: subtitles all on-demand и live English classes; исторический content-accessibility claim, не mobile VoiceOver coverage.

### [23] MCI

- **Текущий магазин:** 3.5.2850; release date 2026-09-21T14:08:00Z. Версия пользовательской записи этим не устанавливается.
- **Темы:** Проверено; публичное подтверждение не найдено. Сведения о переключении не найдены в проверенных публичных источниках; это не утверждение о единственной теме.
- **Типографика:** Семейство native UI не раскрыто проверенными источниками. По screenshot/веб-CSS не определялось.
- **Документированные свойства:**
  - Apple Watch вибрирует по окончании отдыха; характер iPhone haptics остаётся неизвестен. Scope: Apple Watch. Версия: 3.0.2368. Дата источника: 2026-03-26. [Источник](https://roadmap.mcisolutions.de/de-de/changelogs/3-0-2368-workout-sharing)
- **Проверенные публичные маршруты:**
  - [developer_app_store_listing](https://apps.apple.com/us/app/mci-personal-training-ai/id1645679272) — Прочитаны описание, доступная история релизов и раздел Accessibility. Отдельные положительные утверждения и ограничения перечислены в строке.
  - [official_changelog](https://roadmap.mcisolutions.de/de-de/changelogs) — Прочитаны публичные changelogs до 21 Sep 2026; theme switch и native font family не названы.
  - [official_release_note](https://roadmap.mcisolutions.de/de-de/changelogs/3-0-2368-workout-sharing) — 26 Mar 2026: haptic vibration на Apple Watch по окончании rest; long-press sharing cards. Не экстраполируется на iPhone haptics.

## Принципиальные пределы и следующий корректный шаг

Для пунктов со статусом «не установлено» дальнейшее достоверное закрытие требует: inspect установленной версии без покупки/создания аккаунта, явного ответа разработчика или публичной native спецификации. Простое увеличение screenshots либо OCR не устанавливает font stack, runtime API и семантику accessibility. Здесь не запрашивались закрытые репозитории, не обходились paywalls и не отправлялись сообщения производителям.

За рамки native доказательств вынесены: Montserrat из TRX communications; DM Sans из MacroFactor partner marketing; исторические Technogym pixel/seven-segment fonts для оборудования; Buddyfit logo/GIF animations для social/web; WCAG statement сайта FitOn Health; Gymdone Light/Dark switch веб-демонстрации. Дизайнерские Fitify/FitOn кейсы прочитаны, но не раскрывают точные native families.

## W3C: метод для измеренных screenshot color pairs

Для приложения отчёта с измеренными парами цветов применима формула [W3C WCAG2.2, Understanding Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html#dfn-relative-luminance):

```text
c_sRGB = c_8bit / 255
c_linear = c_sRGB / 12.92                  if c_sRGB <= 0.04045
c_linear = ((c_sRGB + 0.055)/1.055)^2.4    otherwise
L = 0.2126*R_linear + 0.7152*G_linear + 0.0722*B_linear
contrast = (L_lighter + 0.05) / (L_darker + 0.05)
```

SC1.4.3 AA: обычный текст 4.5:1, large text3:1; large — минимум 18 typographic pt regular либо 14 pt bold. Не следует автоматически приравнивать логические iOS points к typographic points критерия. Для измерения использовать внутренние цвета штрихов/фона, а не anti-aliased края; учесть активный scrim/disabled state. Растровые JPEG, масштабирование и цветовой профиль вносят погрешность. Это **измерение выбранных пар**, а не заявление о WCAG прохождении всего приложения. [Contrast ratio и large-scale definitions](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
