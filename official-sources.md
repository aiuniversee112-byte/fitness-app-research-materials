# Дополняющие официальные источники для Fitness & Workout Tracker audit

Дата проверки: 2026-10-11. Исполнитель: official_gaps. Источники: официальные сайты, help centers, листинги разработчиков в Apple App Store/Google Play и Apple Lookup API. Поиск: agent-reach / Exa; чтение страниц: Jina Reader. AppLlama и архив исследуются отдельно; этот файл не заменяет наблюдение интерфейсов.

## Ответ

Идентичности целевых приложений установлены; особенно важно различать MacroFactor Nutrition и отдельный MacroFactor Workouts, а также несколько приложений BeFit и TRX. В пользовательском архиве родительский агент установил MacroFactor Nutrition и Befit от 3APPS; MCI — отдельное приложение MCI Solutions GmbH, добавленное пользователем под №23. Точные брендовые цвета и кастомный шрифт документированы у MacroFactor; семейства body/UI-шрифтов, физика анимаций и наличие Liquid Glass у остальных продуктов по текстовым официальным источникам не подтверждены.

## Ключевые находки

### Реестр идентичностей

Данные текущих версий получены непосредственно из Apple Lookup API 2026-10-11. Это версии магазина на дату проверки, **не доказанные версии записей в архиве**. API-запрос: [Apple Lookup](https://itunes.apple.com/lookup?id=6504535443,6621180202,1553503471,6737156524,949905528,1350534443,976506047,1483572798,6474446718,1645679272&country=us).

| Название в аудите | Официальное имя / App Store ID | Издатель / Bundle ID | Текущая версия; дата выпуска UTC |
|---|---|---|---|
| BeFit | [Befit: Gym Workout Tracker — 6504535443](https://apps.apple.com/us/app/befit-gym-workout-tracker/id6504535443) | 3APPS SOLUTIONS AND ADVISORY LTDA; `co.3apps.befit` | 1.2.21; 2026-10-09 |
| MacroFactor | [MacroFactor - Macro Tracker — 1553503471](https://apps.apple.com/us/app/macrofactor-macro-tracker/id1553503471) | Stronger By Science Technologies LLC; `com.sbs.diet` | 5.8.9; 2026-09-24 |
| TRX | [TRX: Strength & Home Workouts — 949905528](https://apps.apple.com/us/app/trx-strength-home-workouts/id949905528) | Fitness Anywhere, LLC; `com.fisikal.member.trxshop` | 10.8.17; 2026-10-01 |
| Gymdone | [GymDone: Workout Planner & Log — 1350534443](https://apps.apple.com/us/app/gymdone-workout-planner-log/id1350534443) | Gor Aghavelyan; `com.gymdone.gymworkoutios` | 3.8.7; 2026-10-11 |
| Technogym | [Technogym: Training & Gym app — 976506047](https://apps.apple.com/us/app/technogym-training-gym-app/id976506047) | Technogym S.p.A; `com.technogym.tgapp` | 3.45.5; 2026-09-25 |
| Buddyfit | [Buddyfit: Exercise at Home — 1483572798](https://apps.apple.com/us/app/buddyfit-exercise-at-home/id1483572798) | Buddyfit SRL; `it.tripix.Buddyfit` | 2026.20.0; 2026-10-05 |
| Symmetry | [Symmetry: Gym Workout Tracker — 6474446718](https://apps.apple.com/us/app/symmetry-gym-workout-tracker/id6474446718) | SymmetryClub LLC; `com.application.symmetry` | 7.15.0; 2026-10-07 |
| MCI | [MCI - Personal Training AI — 1645679272](https://apps.apple.com/us/app/mci-personal-training-ai/id1645679272) | MCI Solutions GmbH; `com.mci.mciApp` | 3.5.2850; 2026-09-21 |

### BeFit: подтверждённые UX-факты

- **Идентичность.** Официальный [Help Center](https://appbefit.com/help-center/) ссылается на ID 6504535443 и называет издателя 3APPS Solutions and Advisory Ltda. Упоминания прежних названий `Befit: AI Workout Routines` и `Befit: Gym & Home Workout Plan` относятся к этому же ID.
- **Редактирование в тренировке.** Вес и повторения меняются тапом непосредственно по числам. Замена упражнения во время занятия вызывается через `⋯` рядом с упражнением; до начала занятия — через `Edit` → `Replace`. [Help Center](https://appbefit.com/help-center/)
- **Отдых и обратная связь.** Таймер можно изменить в текущей тренировке; звук регулируется в `Profile` → `Sounds`. На [странице персонального плана](https://appbefit.com/features/personalized-workout-plan-powered-by-ai/) заявлен автоматический запуск rest timer после подхода.
- **Структура.** История и аналитика открываются из `Progress` / `Analytics`; день недели на главном экране обозначает слот сплита, а не жёсткое календарное обязательство. [Help Center](https://appbefit.com/help-center/)
- **Медиа и типы подходов.** Листинг перечисляет библиотеку 500+ упражнений, пошаговые видео, Warmup / Normal / Drop / Superset, отслеживание восстановления мышц. Наличие видео подтверждено описанием, но уровень съёмки и конкретную технику рендера следует оценивать по экранам. [App Store](https://apps.apple.com/us/app/befit-gym-workout-tracker/id6504535443)
- **Не переносить чужие свойства.** [BeFit - Optimize your workouts — 6621180202](https://apps.apple.com/us/app/befit-optimize-your-workouts/id6621180202) принадлежит Steve NOSSE, bundle `com.mobitra.befit`. Именно его описание явно обещает Dark Mode; это не доказательство поддержки тем в продукте 3APPS.

### MacroFactor Nutrition: подтверждённая дизайн-система

- **Точные официальные brand/app colors:** black `#000000`, white `#FFFFFF`; secondary blue `#215CDA`, purple `#A101C9`, green `#08C343`, orange `#CE5400`. Официальный гайд называет дополнительные цвета поддерживающими, прежде всего для иконографии и иллюстраций. Это брендовая палитра; конкретный surface или CTA должен сопоставляться с видео, а не назначаться автоматически. [Brand Guidelines](https://macrofactor.com/brand-guidelines/)
- **Шрифты.** Custom **Macro Sans** подтверждён для логотипа/wordmark и ключевых заголовков/сообщений. **DM Sans** рекомендован партнёрам для маркетинговых изображений; этот пункт не подтверждает семейство body font мобильного UI. [Официальный ребрендинг, 2025-09-16](https://macrofactor.com/new-look/), [Brand Guidelines](https://macrofactor.com/brand-guidelines/)
- **Темы.** `More` → `Theme` позволяет выбрать `System`, `Light`, `Dark`; System синхронизируется с системным оформлением телефона. Это отдельная статья Nutrition, не документация Workouts. [Switch Between Dark and Light Mode](https://help.macrofactorapp.com/en/articles/73-switch-between-dark-and-light-mode)
- **Семантика прогресса.** Линия цели калорий/макросов становится чёрной в Light и белой в Dark после достижения цели. Между тремя верхними dashboard widgets можно свайпать; они дают разные временные срезы питания. Описание не предполагает автоматически красную семантику превышения. [Dashboard widgets](https://help.macrofactorapp.com/en/articles/225-understanding-the-widgets-at-the-top-of-the-dashboard)
- **Иконография/анимация.** Ребрендинг описывает обновлённые food icons и космические in-app illustrations/animations в onboarding и weekly check-ins. Конкретная библиотека (Lottie/Rive), длительности и easing не раскрыты. [A new look for a new chapter](https://macrofactor.com/new-look/)
- **Отсутствие Workout HUD в рамках выбранного продукта.** Nutrition — пищевой дневник и nutrition coach. Workout player отдельного продукта нельзя использовать как доказательство для блока №2.

### MacroFactor Workouts: отдельный продукт, исключаемый из основного №2

- [MacroFactor Workouts - Tracker — 6737156524](https://apps.apple.com/us/app/macrofactor-workouts-tracker/id6737156524), bundle `com.sbs.train`, тот же издатель. Текущая версия 1.4.1 от 2026-10-03. Силовой трекер включает RIR, supersets, myoreps, partial reps, plate calculator и технику упражнений на видео с Jeff Nippard.
- Официальная документация HUD показывает duration timer слева и rest timer справа вверху; таблицу Set / Previous Performance / Weight / Reps; завершение подхода checkbox; menu снизу с Pause / Minimize / Complete / Settings / Discard; настраиваемое авто-переключение на следующее упражнение. [How to Log a Workout, со скриншотами](https://help.macrofactorapp.com/en/articles/310-how-to-log-a-workout)
- Rest timer запускается после записи подхода; коррекция `±10 s`, preset шагом 15 секунд до трёх минут. [Changing Rest Time](https://help.macrofactorapp.com/en/articles/320-changing-rest-time-during-a-workout)
- У Workouts собственная [документация Light/Dark/System](https://help.macrofactorapp.com/en/articles/357-switch-between-dark-and-light-mode) и настройка звука rest timer в [Feature Settings](https://help.macrofactorapp.com/en/articles/352-feature-setting-overview-workouts).

### TRX: подтверждённая архитектура видеотренировок

- Официальный [TRX App FAQ](https://www.trxtraining.com/pages/getstarted-with-trx-app) подтверждает `For You` на Home, фильтры по продолжительности, сложности, тренеру и области тела; историю `Profile` → `Activity`; Settings открываются в правом верхнем углу Home.
- Под видеоплеером есть отдельное `Tap To Play Music`. Это подтверждает раздельное управление музыкальным слоем, но не описывает crossfade или аудиодаккинг. [TRX App FAQ](https://www.trxtraining.com/pages/getstarted-with-trx-app)
- Контент — prerecorded trainer workouts, live classes и replays. Листинг описывает strength / HIIT / core / mobility / yoga и фильтры по equipment/fitness level. [App Store](https://apps.apple.com/us/app/trx-strength-home-workouts/id949905528)
- **Не путать:** [TRX Training Center — 6472662809](https://apps.apple.com/us/app/trx-training-center/id6472662809) предназначен для расписания и бронирования занятий, а [TRX FORCE — 575378654](https://apps.apple.com/us/app/trx-force/id575378654) — другой продукт. Доказательств системного theme switching, точного шрифта или Liquid Glass в указанных текстах нет.

### GymDone: доказательства и границы маркетинговой демоверсии

- Идентификатор 1350534443 связывает старые названия `GYMDONE: Ai Workout Planner`, `GYDMONE - Gym Workout Planner`, `GymDone - Workout Planner` с нынешним `GymDone: Workout Planner & Log`. Текущее имя взято из Apple Lookup, а не из старого поискового сниппета.
- [Официальный сайт](https://gymdone.com/) содержит interactive demo с **явной пометкой `Illustrative workout data`**. В нём представлены tabs Workout / Progress / Profile, длительность занятия, ряды warm-up/working sets, Rest / Swap, CTA Log set, графики 1RM / Volume / Max Weight / Top Reps, календарь и `Pack my bag`.
- На сайте демонстрируются варианты `App appearance: Light / Dark`, но это переключатель **веб-демо**. Без проверки приложения нельзя записывать его как доказанную пользовательскую настройку native app.
- [App Store](https://apps.apple.com/au/app/gymdone-workout-planner/id1350534443) описывает упражнения с текстом, GIF и видео, custom routines, workout history и body measurements. Это подтверждает типы контента, но не частоту кадров, 3D-rendering engine или качество UI-motion.
- Интерактивную анимацию сайта нельзя выдавать за физику переходов установленного приложения. Для итогового motion-блока приоритет имеет архив.

### Technogym: разные форматы контента внутри одной оболочки

- [App Store](https://apps.apple.com/us/app/technogym-training-gym-app/id976506047) подтверждает персональный Precision Program, workout builder, библиотеку self-guided и instructor-led тренировок, Wellness Magazine, challenges/badges, Wellness Passport, MOVEs/MOVERGY и интеграции датчиков.
- Официальная [страница Technogym App](https://technogym.com/en-US/technogym-app/) разделяет **Sessions** (занятия с тренером) и **Routines** (упражнения с video demos и cues), а также classes. Это важнее, чем сводить всё приложение к единому видеоплееру.
- Страница была доступна в Exa extract, прямое чтение через Jina вернуло 403; [support hub](https://support.technogym.com/products/technogym-app) вернул SSL error. Поэтому детальный Workout HUD, темизация и motion не подтверждены этим источником и должны опираться на локальные/Appllama материалы.

### Buddyfit: редакционная библиотека и видеоклассы

- [App Store](https://apps.apple.com/us/app/buddyfit-exercise-at-home/id1483572798) подтверждает instructor-guided workouts, progressive multi-week programs, live classes, длительности 7–60 минут. В описании — 80+ программ и 1000+ занятий; эти числа являются изменяемыми данными каталога, не оценкой качества.
- Официальная [страница Samsung TV partnership](https://landing.buddyfit.club/samsungtv) описывает разделы `Workouts`, `Program`, `Mindfulness`, live chat и replay, а также вывод на Android TV / Fire TV, Chromecast, Smart View, AirPlay. Это партнёрская посадочная страница без надёжной даты UI; её названия разделов следует сверять с наблюдаемой записью, а не считать актуальной спецификацией навигации.
- [Руководство по выбору программы](https://www.buddyfit.club/mybuddy-it/programma-di-allenamento-come-scegliere-quello-giusto-con-buddyfit) подтверждает выбор по цели, уровню, времени и тренеру. Точные typefaces, theme switching, радиусы и playback controls не раскрыты.

### Symmetry: отдельное приложение, а не Gymmetry

- [App Store](https://apps.apple.com/us/app/symmetry-gym-workout-tracker/id6474446718) и [официальный сайт](https://symmetry.club/en) согласуются по бренду/назначению. Название `Symmetry: AI Gym Workout Log` встречается у того же ID; это не Gymmetry.
- В официальном описании: рейтинг для 300+ упражнений, body maps of exercise ranks, прогресс-фото и графики, социальная лента, логирование тренировок. Это подтверждает функциональную геймификацию; визуальный архетип и насыщенность эффектов всё равно оцениваются по экранам. [App Store](https://apps.apple.com/us/app/symmetry-gym-workout-tracker/id6474446718)
- [Официальный Google Play listing](https://play.google.com/store/apps/details?id=club.symmetry.application&hl=en_US) содержит release note о переработанных rank icons/colors и немедленном появлении celebration screen после завершения занятия. Это заявление разработчика об Android-релизе; его нельзя подменять замером iOS-анимации.
- На сайте есть [официальный app mockup](https://symmetry.club/images/home/mockup-updated.png), пригодный как дополнительная визуальная проверка. По тексту сайта не установлены UI-font, Light/Dark switch, Lottie/Rive или точные материалы.

### Peloton: не смешивать video classes, Peloton Gym и Strength+

- В основном Peloton App существует **Peloton Gym** — self-paced strength routines. Официальная [help article](https://support.onepeloton.com/s/article/14195473421332-Peloton-Gym) описывает путь Workouts → Gym, chips muscle-group filtering, верхний elapsed timer с Pause и зелёную стрелку, которую сдвигают слева направо для завершения блока. Прочитано через Exa; прямое чтение через Jina вернуло Salesforce loading/CSS error.
- [Официальный анонс Peloton Gym](https://www.onepeloton.com/blog/peloton-gym) описывает tutorial videos по отдельным упражнениям, текстовые объяснения, ввод веса/повторов и self-paced progression. Это не тот же режим, что полноэкранный live/on-demand видеокласс.
- [Peloton Strength+](https://www.onepeloton.com/strength-plus-app) — отдельное приложение/опыт: генерация тренировок, self-paced программы, демонстрации техники, swap movements, tracking. Его особенности нельзя автоматически переносить на основной Peloton App. Аппаратные Peloton IQ camera/form-tracking features также нельзя приписывать мобильному HUD.

### MCI: новый №23, идентичность подтверждена

- [MCI - Personal Training AI — 1645679272](https://apps.apple.com/us/app/mci-personal-training-ai/id1645679272), MCI Solutions GmbH; [официальный сайт](https://mcisolutions.de/) напрямую ссылается на этот App Store ID и Google Play `com.mci.mciApp`.
- Описание разработчика подтверждает 500+ strength exercises с **3D animations**, отдельные модули strength/cardio/nutrition/mobility, personalised plans и gamification. Текст не подтверждает 3D-движок или конкретные motion libraries. [App Store](https://apps.apple.com/us/app/mci-personal-training-ai/id1645679272)
- Сайт подтверждает onboarding questions по целям, опыту, частоте и продолжительности тренировок, streaks, progress statistics и календарь. [MCI website](https://mcisolutions.de/)
- Родительский агент нашёл MCI в AppLlama (32 entries: 30 images + 2 videos, welcome/onboarding/paywall) и в записи V12. Полный визуальный блок создаётся отдельно в `audit-23.md`.

### Strava: системные темы подтверждены

- `You` → Settings → Preferences → Appearance предлагает `Phone default / Light Mode / Dark Mode`. Первое следует за системой, остальные переопределяют её. Это прямая официальная инструкция, поэтому нельзя называть Strava приложением только со светлой темой по одной серии экранов. [How Do I Enable Dark Mode on Strava?, 2026-09-14](https://support.strava.com/en-us/articles/15401628-how-do-i-enable-dark-mode-on-strava)

### Gravl: реальный Workout HUD, video-help и расширенная темизация

- **Theme Settings:** Profile → App preferences → Theme: `Light / Original / System / Custom`; Original — стандартная тёмная тема. Custom содержит `Stealth` (pure black, без цветового акцента), `Pulse` (plum-black + magenta), `Rose` (white + rose-pink). В System отдельно выбираются light и dark варианты. У обычной Light доступны accents Black / Blue / Violet / Rose / Emerald / Orange. Это официально описанные настройки, а не вывод из рекламных иллюстраций. [Themes, 2026-09-27](https://gravl.ai/help/themes-change-how-gravl-looks), [официальный screenshot](https://gravl.ai/help/themes.jpg)
- **Rest:** Train → sliders вверху справа → Workout Settings → Rest time. Defaults: 90 s isolation и 120 s compound; timer можно отключить. [Adjust Your Rest Times, 2026-08-07](https://gravl.ai/help/adjust-your-rest-times), [встроенная запись интерфейса MP4](https://gravl.ai/help/2176473642-record-2026-03-18-19-14-29-4bc24.mp4)
- **Pause/Resume:** tap по elapsed time на активном workout screen; подтверждение `Paused`, мигающая точка рядом со временем. Повторный tap или log set возвращает сессию в running; появляется `Resumed`. [Pause Your Workout](https://gravl.ai/help/life-calling-pause-your-workout), [реальный HUD MP4](https://gravl.ai/help/pause-workout.mp4)
- **Вне приложения:** Android notification показывает текущее упражнение, next set с weight/reps, тип подхода и прогресс подходов; rest countdown — отдельная notification. Документация называет это аналогом iPhone Live Activity. Не переносить раскладку Android notification на iOS без визуальной проверки. [Workout notification](https://gravl.ai/help/workout-progress-notification-on-android)
- Видео переданы агенту `audit_16_22` для визуального/motion-анализа; в настоящем файле зафиксированы подтверждённые текстом взаимодействия и адреса первичных материалов.

### Muscle Booster: реальный player из официального Help Center

- **Источник скриншотов:** [How do I turn off the background music?, 2025-12-03](https://musclebooster.welltech.com/help-center/features-personalization/how-do-i-turn-off-the-background-music/). Изображения скачаны и просмотрены: [player 1](official-media/booster-player-help-01.webp), [player 2](official-media/booster-player-help-02.webp). Статья показывает варианты для платформ; первый screenshot содержит Android status bar. Дата статьи не доказывает дату/версию самого screenshot.
- **Наблюдаемый HUD:** top segmented progress; длительность и Close справа сверху; `Current` + название упражнения; кнопки `How to` / `Change`; крупная анатомическая 3D-демонстрация; центральные Previous / Pause / Next controls; нижние число reps или timer; Cast / Audio / Music; карточка `Next` с thumbnail и названием следующего шага. Это прямое визуальное наблюдение справочного снимка, не перенос дизайна рекламного сайта.
- **Состояние overlay:** показанные playback controls активны; scrim затемняет модель и нижний большой счётчик. Нельзя оценивать обычный контраст модели/числа только по этому затемнённому состоянию. Плавность/автоскрытие controls из статичного screenshot не доказаны.
- **Audio feedback:** инструкции произносят название упражнения и начало/конец интервала. Tap по экрану раскрывает Music/Audio; музыка выбирается во внешних Apple Music / YouTube Music / Spotify, voiceover отключается отдельно. [Официальная инструкция](https://musclebooster.welltech.com/help-center/features-personalization/how-do-i-turn-off-the-background-music/)
- **Замена упражнения:** доступна как в preview, так и во время workout через Arrows; затем alternatives list и Save. Число повторов/время остаются прежними. [Help + screenshots](https://musclebooster.welltech.com/help-center/features-personalization/can-i-change-the-exercise-that-is-offered-in-the-workout/), [локальный screenshot 1](official-media/booster-swap-help-01.webp), [локальный screenshot 2](official-media/booster-swap-help-02.webp)
- **Официальные CDN URL:** [player 1 original](https://images.ctfassets.net/nwmr7vzznfrp/mb-img-1adbdd52608308c505e4/042023a73bca509bbd1375d0d1b8dc1a/EN_Howtoturnoffbackgroundmusic_.png?w=600&fm=webp&q=75), [player 2 original](https://images.ctfassets.net/nwmr7vzznfrp/mb-img-26013e28ab3ee7ef3b78/5fb58e6d815622266467727c3fc1ff29/ENGHowdoIturnoffthebackgroundmusic.jpg?w=600&fm=webp&q=75).

### Muscle Monster: официальные продуктовые инструкции

- [Help & Support](https://supportcenter.musclemonster.fit/?from=officialweb) содержит реальные guide screenshots для Library, Custom, Daily, Me. Library filters: Duration / Your Goal / Target Area; расширенный Filter содержит Level и Equipment Type. Custom включает AI Coach, duration/location/target/goals/equipment и Saved Templates. Daily → Overview открывает настройки плана. Эти прямые маршруты полезнее, чем выводы из рекламного макета.
- В этом help center не обнаружен полноценный активный workout player. Список course-library thumbnails не даёт права придумывать rest-timer layout или доступность жестов во время подхода.
- Доступные первичные изображения: [Library filters](https://dailyyogaappimage.dailyyoga.com/0f/69/0f6931b063468b435d8d49c8f39d63f7.png), [AI Coach/custom plan](https://dailyyogaappimage.dailyyoga.com/72/19/7219f3fe481dd9f45cba1e29a67fedea.png), [Manual custom workout](https://dailyyogaappimage.dailyyoga.com/27/5b/275bfcfc630c4cd9b0a0e47ae0d0088c.png), [Workout replacement](https://dailyyogaappimage.dailyyoga.com/ba/42/ba42c12046f7354fd55101d0fac80ecb.png). CDN принадлежит инфраструктуре Daily Yoga, но ссылки встроены в официальный Muscle Monster support.
- [App Store — 6471547318](https://apps.apple.com/us/app/muscle-monster-workout-planner/id6471547318) release history подтверждает Live Activities на iOS и multi-speed class playback. Это заявленные функции; micro-animation curve и specific HUD appearance не раскрыты.

### Peloton: дополнительные сведения и текущие store screenshots

- [App metrics](https://support.onepeloton.com/s/article/Peloton-App-One-App-Metrics?language=en_US) описывает in-class calories и heart rate при подключённом датчике. [Target Metrics](https://support.onepeloton.com/s/article/Peloton-Workouts-Target-Metrics) явно распространяет target ranges на mobile App для cycling/running; [документация cadence connection](https://support.onepeloton.com/s/article/360026787151-Connecting-A-Cadence-Sensor-To-The-Peloton-App-For-Apple-iOS-and-Android) описывает Connected Devices, checkmark после успешного pairing и синюю точку рядом с connected-devices icon. Проверено по Exa extraction официальных страниц; live-reader возвращает Salesforce CSS error. Между статьями расходится информация о доступности cadence на Android, поэтому лучше не делать лишнего платформенного обобщения.
- Текущие screenshots магазина [Peloton: Fitness & Workouts — 792750948](https://apps.apple.com/us/app/peloton-fitness-workouts/id792750948) сохранены в `official-media/792750948-store-*.jpg`, обзор [здесь](official-media/792750948-store-board.jpg). Они показывают продуктовый dark UI с purple activity/streak markers, пятью нижними tab icons, Classes / Gym / Collections / Programs наверху каталога, белым floating Filter pill, weekly plan и Club Peloton gold rewards. **Это официальные store compositions, не запись приложения.** Из них можно описывать видимые статические компоненты, но нельзя заключать об их движении или размерах hit targets.
- Ни текущие store images, ни успешные прочитанные web-тексты не предоставили полностью проверенный мобильный video-class HUD для оценки motion. Информацию про Peloton Bike touchscreen нельзя автоматически переносить на телефон.

### Реестр загруженных дополнительных изображений

- `official-media/manifest.json` хранит исходный App Store CDN URL, URL увеличенного представления, App Store ID и локальное имя каждого из 21 изображения. Получены через официальный Apple Lookup API 2026-10-11.
- [Muscle Booster store board](official-media/1446447749-store-board.jpg) — **промокомпозиты**, не достоверный screenshot конкретного рабочего состояния. Не использовать их glass-like overlay как доказательство glassmorphism native UI.
- [Muscle Monster store board](official-media/6471547318-store-board.jpg) — светлые продуктовые экраны с жёлтым accent внутри рекламных композиций; HUD не показан.
- [Peloton store board](official-media/792750948-store-board.jpg) — статические продуктовые screens в phone frame; полезен для визуальной структуры после входа.

## Подробности

Официальная документация — достаточное основание для именования функции, пути навигации и поддерживаемого варианта настройки. Она не устанавливает фактическую плавность, easing, качество тактильного отклика или длительности транзишенов. Скриншот с тёмным фоном доказывает наличие данного состояния, но сам по себе не доказывает переключение темы. Прозрачная панель не доказывает Apple Liquid Glass API. Web CSS или брендовый font guideline не подтверждают семейство native body font.

При различии видео, базы AppLlama и магазина в финальном аудите следует указать источник/дату и описать наблюдаемую версию. Маркетинговые эпитеты (`intuitive`, `clean`, `premium`, `science-backed`, `#1`) не приняты здесь за результаты UX-исследования. Perceived Value должен выводиться из визуального качества, а не цены подписки, рейтинга магазина или обещаний разработчика.
