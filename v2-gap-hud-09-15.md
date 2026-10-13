# V2: дополнительные доказательства рабочего HUD — FitOn, Fitify, SmartGym, BODi

Дата проверки: 2026-10-11. Исходный `audit-09-15.md` и общий отчёт **не изменялись**. Все новые медиа, метаданные, кадры и скрипты находятся в `v2-media/09-15/`.

## Ответ

Основной пробел FitOn по активному интерфейсу закрыт публичной записью iPhone, опубликованной 22.06.2026: теперь наблюдаются переход из countdown в landscape, play/pause, ±15 секунд, scrubber, скрытие controls, выход из занятия с рекомендациями и возврат к карточке Resume. Для Fitify, SmartGym и BODi найдены новые записи реального рабочего интерфейса, однако они относятся к Android/iOS-версиям 2022–2023 годов и применимы как доказательство исторического поведения, а не замена текущим скриншотам AppLlama. Полная **визуальная** цепочка успешного завершения FitOn до post-workout screen не найдена; официальный Help Center подтверждает существование послетренировочной сводки HR-зон, но не её анимацию.

## Как читать уверенность

- **V — визуально наблюдено:** просмотрены новые кадры публичной записи, включая последовательность вокруг действия. Источники сторонние, но их экранная запись является первичным свидетельством своего сеанса.
- **D — документировано:** явно описано в официальной справке; не выдаётся за увиденную анимацию.
- **H — историческое:** источник опубликован до текущей выборки, платформенные отличия обязательно сохраняются.
- **U — не установлено:** отсутствие доказательства конкретного состояния, а не отсутствие функции в продукте.
- Дата ниже — дата публикации YouTube `upload_date`, сохранённая в `.info.json`, либо дата статьи. Она не гарантирует дату записи и номер сборки. Easing, haptics, fps рендеринга и UI-framework из этих записей не определяются.
- Просмотрено 10 уникальных публичных видео через обзорные контактные листы; relevant-интервалы разобраны с шагом 2–4 секунды. У Fitify исходный обзор содержит ускорения/монтаж, поэтому по его таймкодам нельзя измерять продолжительность переходов. Ничего из ранее изученных AppLlama-видео не представлено здесь как новое доказательство.

## Реестр новых источников

| ID | Источник и provenance | Дата, платформа | Новое покрытие и локальные артефакты |
|---|---|---|---|
| FO-V1 | [FitOn App Instructional Video — Jamie Shoemaker](https://www.youtube.com/watch?v=CDRczlU9Ah0), публичная сторонняя инструкция с непрерывным screen recording | 2026-06-22; iPhone/iOS по интерфейсу системы; build неизвестен | `fiton-hd-CDRczlU9Ah0.mp4`; 05:14–05:50; `fiton-current-detailboard-1.jpg`, `fiton-current-detailboard-2.jpg`, отдельные `fiton-current-0314.png`…`fiton-current-0350.png` |
| FO-V2 | [Downloading and Using the FitOn App — Yogalete](https://www.youtube.com/watch?v=YVSvITHHiYA), публичная инструкция с записью планшета | 2023-12-08; iPadOS, H | `fiton-YVSvITHHiYA.mp4`; 04:46–05:10; `fiton-ipad-detailboard-1.jpg`; подтверждение active playback/controls на планшете |
| FO-V3 | [FitON — App Review — 60 Seconds To Fitness](https://www.youtube.com/watch?v=xQ3qeysV0q4), сторонний опыт с реальным UI в боковой вставке | 2023-08-29; iPhone/iOS, H | `fiton-xQ3qeysV0q4.mp4`; 04:00–04:04; `fiton-social-detailboard-1.jpg`; видео над портретным leaderboard |
| FO-D1 | [PRO: Heart Rate Zones — официальный FitOn Help Center](https://help.fitonapp.com/en/articles/7835499-pro-heart-rate-zones) | Статья 2023-07-11; текущая страница проверена 2026-10-11; иллюстрация iPhone landscape | `fiton-official-zones.md`, `fiton-official-zones-1.jpg`; реальная панель Connect HR и документированная post-workout zone summary |
| FO-D2 | [PRO: How can I adjust music during a workout? — официальный Help Center](https://help.fitonapp.com/en/articles/7835498-pro-how-can-i-adjust-music-during-a-workout) | Статья 2023-07-11 | `fiton-official-music.md`; подтверждение раздельной регулировки MUSIC/TRAINER. Скачанная иллюстрация — рекламный artwork, **не** доказательство рабочей панели |
| FO-H1 | [FitOn Review — The Fit Careerist](https://thefitcareerist.com/fiton-review/), firsthand review с affiliate disclosure | 2021-04-24; автор использует и компьютер, и телефон; платформа конкретного finish не определена | `fiton-firsthand-2021.md`; текстовое историческое свидетельство запроса оценки playlist/instructor/difficulty/streaming после занятия; не доказательство текущего визуала |
| FY-V1 | [Fitify Fitness App Review — Holistic Healing Choices](https://www.youtube.com/watch?v=TQ5rYKmsr-E), сторонний обзор с экранной записью рядом с автором | 2023-12-06; Android по системной панели Media/громкости на 03:38, H | `fitify-hd-TQ5rYKmsr-E.mp4`; 03:22–04:10; `fitify-hud-detailboard-1.jpg`, `fitify-hud-detailboard-2.jpg`; Get Ready, рабочий timer, Pause, skip, exit feedback |
| SG-V1 | [How to start workout session on SmartGym? — Just Ask Me](https://www.youtube.com/watch?v=7RXAxVgXmgU), сторонняя пошаговая запись | 2022-11-03; iPhone/iOS по status/Control Center, H | `smartgym-7RXAxVgXmgU.mp4`; 00:58–01:26; `smartgym-hud-detailboard-1.jpg`, `smartgym-hud-detailboard-2.jpg`; HIIT prep/work/pause/stop sheet |
| SG-D1 | [How to use SmartGym — официальная Knowledge Base](https://help.smartgymapp.com/article/125-how-to-use-smartgym) | Last updated 2023-10-25; iPhone screenshots, H | `smartgym-official-howto.md`, `smartgym-official-8.png`…`smartgym-official-11.png`; силовая цепочка set logging → rest → next exercise → end; крупный elapsed/pause/end control |
| BD-V1 | [How to stream your BOD and BODi workouts… — Kelly G](https://www.youtube.com/watch?v=dXngQZ_903I), сторонняя инструкция с живой записью телефона | 2023-03-02; Android, H | `bodi-dXngQZ_903I.mp4`; 01:30–03:22; `bodi-hud-detailboard-1.jpg`…`bodi-hud-detailboard-3.jpg`; cast, pause, seek, stop casting, early exit, log/ignore incomplete workout |

Полные извлечённые метаданные всех скачанных записей: `v2-media/09-15/source-manifest.json`. Имена файлов в таблице указаны относительно `v2-media/09-15/`.

## 10. FitOn — факты, закрывающие critical gap

### Реальная последовательность

1. **05:14–05:20 FO-V1 [V]:** перед запуском уменьшаются число в центре и розово-коралловая дуга крупного кольца. При достижении нуля карточка ещё кратко видна поверх workout detail; затем сцена переходит в landscape. Это подтверждённая динамика исходного `A10/oth_w9d68`, а не предположение по screenshot.
2. **05:22–05:34 [V]:** landscape-плеер имеет небольшой кольцевой показатель общего остатка в углу, музыкальную команду и HR-элемент по краям. В этом конкретном recording область видеоконтента серая/размытая; причина не установлена. Нельзя объявлять её выбранным стилем видео или приписывать DRM/сетевую ошибку без дополнительных данных.
3. **05:34–05:36 [V]:** раскрывается transport layer: большой центральный play, ±15 секунд с обеих сторон, длинный scrubber с elapsed/total, заголовок и back слева, cast/captions/fullscreen справа. Белые controls читаются на затемнённой подложке. Это обычная схема медиаплеера; числовое время компактнее транспортных кнопок.
4. **05:36–05:44 [V]:** видимая transport-панель исчезает и снова раскрывается; остаётся компактный corner timer. Это подтверждает два состояния плотности HUD. В данном коротком фрагменте число почти не изменяется, поэтому его нельзя использовать для оценки непрерывной частоты/плавности счётчика.
5. **05:44–05:48 [V]:** выход возвращает portrait-сцену с текстом `Leaving? Try these workouts instead:` и карточками альтернатив. После закрытия — каталог, где исходная карточка теперь имеет **Resume**, а не Start. Это наблюдённый выход/продолжение, **не успешное завершение занятия**.
6. **FO-V2 04:54–05:08 [V,H]:** на iPad уменьшается остаток, при раскрытии виден pause, ±15 секунд, scrubber; кнопки скрываются и возвращаются. Демо-инструктор в этой записи остаётся размытым; сохраняется такое же ограничение качества изображения контента.
7. **FO-V3 04:00–04:04 [V,H]:** реальное видео инструктора продолжает двигаться в верхней части portrait-layout; нижнюю часть занимает фиолетовая таблица Leaderboard с Overall/Friends и выделенной строкой пользователя. Это альтернативное, более плотное социальное состояние активного занятия. Имена участников не перенесены в текст исследования.

### Семантика HR и post-workout

Официальная иллюстрация FO-D1 показывает Connect HR с тремя подписанными областями **Fat Burn → Cardio → Peak**, цветовая шкала идёт от жёлтого через оранжево-коралловый к розовому. Значение HR над шкалой и круглый marker связывают число с зоной; справа перечислены способы подключения. Это **реальный скрин интерфейса официальной справки**, в отличие от рекламного изображения Music. Статья прямо сообщает, что post-workout summary показывает время в каждой зоне. Наблюдения позволяют дополнить семантическую палитру; они не подтверждают точные актуальные HEX-токены, текущие вычисления зон или finish animation.

### Готовые абзацы для вставки в аудит FitOn

**Вместо старого ограничения Workout HUD:**

> Активный HUD дополнительно проверен по публичной записи iPhone, опубликованной 22.06.2026. После кругового countdown плеер переходит в landscape. Раскрываемый слой содержит central play/pause, перемотку ±15 секунд, длинный scrubber, elapsed/total, back, casting, captions и fullscreen; при скрытых controls остаются компактный corner timer и периферийные вспомогательные команды. Такой HUD хорошо отдаёт сцену уроку, но мелкие значения времени читаются с расстояния хуже, чем крупная центральная кнопка. В другой записи iPhone 2023 года видео работает над portrait-leaderboard с вкладками Overall/Friends: у FitOn есть и малоплотный режим просмотра, и социальный режим с таблицей. [FO-V1 05:14–05:44; FO-V3 04:00–04:04]

**Дополнение Motion/early exit:**

> Подтверждены уменьшение числа и дуги стартового кольца, смена portrait на landscape, раскрытие/скрытие transport controls и выход обратно в portrait. При раннем выходе появляется панель с альтернативными тренировками, после неё карточка исходного занятия получает Resume. Это конкретная обратная связь сохранённого незавершённого состояния. Видеосцена FO-V1 не содержит читаемой демонстрации тренера; качество самого медиаконтента оценено по отдельному источнику, а причины серой области не установлены. [FO-V1 05:14–05:50]

**Дополнение Semantic colors и уточнение оставшегося gap:**

> В официальном Connect HR screenshot присутствуют три подписанные зоны: жёлтый Fat Burn, оранжево-коралловый Cardio и розовый Peak, с числом HR и маркером текущей позиции. Официальная справка подтверждает послетренировочную сводку времени в зонах. Визуальное успешное завершение полного урока и его motion в изученных доступных материалах не наблюдались; ранний выход с Resume не используется как их замена. [FO-D1; FO-V1]

**Итог gap:** active HUD, numerical hierarchy, playback controls, transition, early exit — закрыты; post-workout HR summary — D; полный finish UI/celebration — U. Старую общую фразу «нет активного плеера» следует убрать.

## 9. Fitify — новые факты рабочего движения

- **03:22–03:28 FY-V1 [V,H]:** из Instructions осуществляется вход в белый рабочий экран с большим видео человека, центральным Get Ready/кольцом подготовки, локальной длительностью снизу, общим остатком и сегментированной полосой сверху. Затем центральная надпись исчезает, локальное значение уменьшается. Структурно это соответствует актуальному `A09/oth_nar2c`; синяя оболочка каталога в видео — историческая Android-версия и не переносится на текущий Light UI.
- **03:40–03:44 [V,H]:** по центру появляются triangle Play и **Paused**, общий timer фиксирован, а человек в демонстрации продолжает менять позу. Значит, в показанной реализации пауза тренировки сохраняет возможность изучать движение. Нельзя считать playback video и workout clock одним счётчиком.
- **03:46–04:02 [V,H]:** пользователь пропускает несколько упражнений; меняются название, сторона и локальная длительность, перед новым активным сегментом возвращается Get Ready. Источник явно ускоряет/монтирует просмотр — скорость UI-перехода из этих фрагментов не вычислялась.
- **04:04–04:08 [V,H]:** ранний выход ведёт на Why didn’t you finish your workout? с четырьмя причинами и Skip, затем в каталог. Тот же паттерн причины прерывания уже был статично подтверждён текущим `A09/oth_xsdrm`; новый источник добавляет причинно-временную связь.

### Готовая замена motion-gap Fitify

> Рабочая динамика дополнительно наблюдалась в публичном Android-обзоре от 06.12.2023: Get Ready предшествует уменьшающемуся локальному таймеру, Pause останавливает workout clock и выводит central Play/Paused, при этом демонстрация движения продолжает воспроизводиться. Пропуск переключает упражнение и его сторону с повторным Get Ready; раннее закрытие вызывает анкету причины прерывания и возврат в каталог. Основная пространственная схема совпадает с текущими screenshot A09/oth_nar2c и oth_xsdrm, но синяя старая оболочка, точные durations и поведение последней iOS-сборки не выводятся из Android-источника. Полный successful finish/reward и завершение отдельного rest-сегмента всё ещё не наблюдались. [FY-V1 03:22–04:08]

## 11. SmartGym — HIIT motion и документированная силовая цепочка

- **00:58–01:06 SG-V1 [V,H]:** Start в routine открывает крупный HIIT HUD. Сверху — движущийся анатомический демонстратор, название Jumping Jack; ниже Current Set `1/1` и Duration `30 sec`; нижнюю треть занимает кольцо. Подготовка показана лаймом, затем рабочее значение/дуга становятся cyan. Это **рабочий**, а не rest timer: рядом прямо подписана продолжительность текущего подхода.
- **01:08–01:16 [V,H]:** после паузы значение фиксируется на 28, Pause превращается в Play, демонстрация продолжает цикл движений. Большие цифры и дуга полезны на расстоянии, хотя верхние служебные данные значительно мельче.
- **01:18–01:26 [V,H]:** красный X открывает action sheet. Раздельные команды **Stop HIIT Sequence and Workout Session**, **Stop HIIT Sequence**, **Cancel** явно отделяют прерывание последовательности от завершения всей сессии. Не следует сокращать это до «один Finish».
- **SG-D1 [D,H]:** официальная инструкция силового режима: tap номера подхода сохраняет set и запускает rest; после всех подходов доступны верхняя стрелка/Next Exercise; нижняя красная кнопка завершает workout и останавливает duration. Screenshot `smartgym-official-11.png` показывает rest row над нижним крупным elapsed `01:02:27`, красный X слева и Pause справа. Не смешивать этот elapsed с меньшим rest timer.
- Текст официальной инструкции называет Next Exercise синим; текущие AppLlama-экраны используют и лаймовые commands. Это различие даты/состояния, а не основание «исправить» текущую палитру.

### Готовая замена motion-gap SmartGym

> Публичная запись iPhone от 03.11.2022 закрывает динамику HIIT: лаймовый countdown подготовки сменяется cyan рабочим кольцом, Pause фиксирует секунды и меняется на Play, а анатомическая демонстрация продолжает двигаться. Stop sheet предлагает остановить только HIIT sequence либо sequence вместе с workout session. Это историческое доказательство альтернативного HUD, а не заявление о неизменности сборки 2026 года. Для силового режима официальная инструкция от 25.10.2023 отдельно подтверждает связку «tap номера подхода → сохранение подхода → rest timer → Next Exercise → красная кнопка завершения». Анимация последней секунды rest, completion reward и текущие haptics визуально не проверены. [SG-V1 00:58–01:26; SG-D1]

## 12. BODi — воспроизведение, casting и сохранение неполной сессии

- **BD-V1 01:30–02:26 [V,H]:** в Android cast-плеере видны заголовок, Cast, CC, central Play/Pause, ±30 секунд, seekbar и elapsed/total. На телефоне во время casting показан брендовый placeholder, а не живая мини-картинка занятия. В 02:18 seekbar перемещён вперёд, появляется loading indicator; далее снова Pause, затем Play. Числа компактны, транспортные иконки заметнее.
- **02:30–02:42 [V,H]:** Cast dialog даёт stop casting/close и volume; после остановки возвращается локальный плеер с реальным instructor preview. Это смена режима вывода, а не finish.
- **02:46–03:02 [V,H]:** после выхода показывается предложение дополнительного пятиминутного занятия, затем Log your workouts. В списке незавершённого workout есть вопрос о сохранении и варианты **No Thanks / Log**; подтверждение выводится синим нижним snackbar. Это явный recovery-паттерн, позволяющий решить судьбу неполного занятия.
- **03:10–03:22 [V,H]:** сохранённый workout имеет собственную карточку и optional post-to-group. Самостоятельно никакая публикация не выполнялась; это только просмотр публичной записи автора.
- **Версионная граница:** Android 2023 показывает ±30 секунд, а текущий статичный `A12/oth_2jdo6` — ±15 секунд. В основном benchmark сохраняется **±15** для актуальной iOS-выборки; новая запись доказывает общий interaction flow, а не идентичные параметры controls.

### Готовая замена motion-gap BODi

> Новая публичная Android-запись от 02.03.2023 показывает реальные transport-состояния, seek/loading, pause/play, выход из casting обратно к локальному видео, затем recovery неполного workout. После выхода предлагается короткое дополнительное занятие; отдельный Log your workouts позволяет сохранить либо игнорировать незавершённую сессию, а результат подтверждается нижним синим snackbar. Это полезное дополнение к текущим iOS-скриншотам tracking. Значение перемотки исторического Android-плеера — 30 секунд, тогда как в текущем A12/oth_2jdo6 видно 15; эти реализации не объединяются в один якобы текущий экран. Полная последняя iOS-сессия до естественного конца и completion badges motion остаются непроверенными. [BD-V1 01:30–03:22]

## Карта закрытия задач

| Приложение | Active HUD | Numerical readability | Pause/rest | Early exit | Successful finish |
|---|---|---|---|---|---|
| FitOn | V: iPhone 2026; iPad 2023; portrait leaderboard 2023 | V: большой transport, маленький corner total; HR screenshot D/V | V: controls play/pause, ±15; отдельный rest HUD не найден | V: recommendation sheet → Resume | D: official HR summary; H: firsthand rating report; финальный motion U |
| Fitify | V/H: Android 2023; spatial match к текущему A09 | V/H: крупный local timer + маленький общий остаток | V/H: clock freezes, demo continues; последний tick rest U | V/H: reason form → catalog, форма совпадает с current screenshot | U: no full session finish |
| SmartGym | V/H: iPhone HIIT 2022; D/H: силовой режим 2023 | V/H: ring; D/V: separate rest and big elapsed | V/H: pause at 28, demo continues; D: set log starts rest | V/H: two distinct Stop scopes + Cancel | D: end session stops duration; финальная summary animation U |
| BODi | V/H: Android 2023; current iOS static remains primary | V/H: small elapsed/total, larger transport | V/H: pause/play/seek and cast state | V/H: offer → log/ignore → snackbar | V/H: manual log result; естественный final playback state U |

## Проверенные маршруты и search log

### Инструменты

1. Прочитаны `agent-reach/SKILL.md`, `references/search.md`, `references/web.md`, `references/video.md`. `agent-reach doctor --json`: Exa настроен, YouTube backend — yt-dlp, Jina — доступен. Live-поиск подтвердил работоспособность Exa и yt-dlp.
2. Публичный YouTube скачивался `yt-dlp --js-runtimes node`, без браузерных cookies, логина или создания аккаунта. Флаг задавался этому процессу; постоянная конфигурация yt-dlp не менялась.
3. Jina Reader использовался для официальных help pages и публичных review pages. После лимита Exa использован встроенный web search; обхода лимита или создания API key не выполнялось.
4. `agent-reach check-update`: установленная v1.5.0 актуальна.

### Запросы и результаты

| Маршрут / точный запрос | Результат и решение |
|---|---|
| Exa: `FitOn app workout player pause finish workout screen tutorial` | Official music/casting Help, ScreensDesign showcase; найден дополнительный маршрут, не использован его AI-текст как визуальное доказательство |
| Exa: `SmartGym app start workout session tutorial video rest timer` | Найдена официальная статья SG-D1 с 15 screenshots, скачаны релевантные 8–11 |
| Exa: `Fitify app workout session pause finish tutorial video` | Найден FY-V1; App Store release notes обнаружены, но не подменяют прямое наблюдение |
| Exa: `BODi app workout player pause completion screen tutorial video` | Official streaming articles и older walkthrough; прямой мобильный источник найден далее через YouTube |
| ScreensDesign public showcase FitOn: Jina + публичный HTML | Показаны 7 preview images; fourth preview помечен lock/Watch full video. Полное видео требует доступа к library. Не обходилось, не объявлялось просмотренным; HTML сохранён только как журнал проверенного маршрута |
| YouTube `FitOn app review workout player` | Слишком широкая выдача, далее сужена |
| YouTube `FitOn app tutorial` | FO-V1, App Class `t0kopnx_e-I`, FO-V2, FO-V3; все четыре скачаны и просмотрены по contact sheets |
| YouTube `Fitify app review tutorial` | FY-V1: реальный рабочий HUD обнаружен в 03:22–04:08; скачать HD имело смысл для чтения левой экранной вставки |
| YouTube `SmartGym app workout tutorial` | SG-V1: прямой HIIT UI; прочие ролики не объявлены просмотренными |
| YouTube `BODi app tutorial walkthrough` | BD-V1 и `WLDnNgzBtfM` — Brianna Yates, 2024-01-12. Последний оказался преимущественно web/platform tour: не использован для мобильного HUD |
| Exa: `"FitOn" "workout summary" "screen"` | Store pages и marketing, без завершённого mobile finish |
| Exa: `site:help.fitonapp.com workout finished complete rating summary stop` | Free MCP rate limit; дальнейшие Exa-запросы не выполнялись |
| YouTube `FitOn workout completed app finish` | В основном самостоятельные видео тренировок. Они не являются recording приложения и не использованы как app UI |
| YouTube `FitOn app screen recording workout review` | Повторные/общие результаты; не дал полного finish |
| Official Help index → Trainers & Workouts collection | Проверено 9 article titles; нет отдельной инструкции finish UI. Не выводить отсутствие функции из отсутствия статьи |
| Web: `"FitOn" "Workout Summary"`, `"FitOn" "rate this workout"`, `"FitOn" "workout complete" screen` | Найден FO-D1. Также выдача содержит одноимённые Figma/UI kits и другой продукт Newon FitOn — исключены как неверная идентичность |
| YouTube `FitOn app workout review completed rating` | Добавлены `lRQ1SDEa-8E` — Magenta Otter Travels (2025-01-03) и `_AgUd-upePg` — Peace Onyeagwu (2021-02-21). Первый преимущественно talking head, второй exercise-with-me; successful app finish не показан |
| Web: `FitOn app "summary" review screenshot`; `FitOn "Workout Complete" …`; `FitOn app "Great job" workout screenshot` | Найдены firsthand blogs The Fit Careerist и Mas & Pas, проверены через Jina. Первый подтверждает исторический запрос feedback текстом; второй содержит onboarding/promotional imagery, не закрывает finish |
| YouTube `Fiton complete workout screen` | В основном exercise-content; нового мобильного completion UI не найдено |

### Что намеренно не утверждается

- Не называются рекламные кадры или чужой «FitOn UI Kit» реальными экранами продукта.
- Не утверждается, что FitOn не имеет итогового экрана: официальная справка прямо подтверждает post-workout summary.
- Не переносится дата публикации ролика в точный номер сборки; historical Android playback не выдаётся за iOS 2026.
- Серый/размытый video layer не объясняется DRM, плохой сетью либо paywall без достаточных данных.
- После этой итерации старые broad gaps «HUD не наблюдался / motion только onboarding» слишком широки. Их следует заменить **узкими** ограничениями: успешное завершение полной сессии текущей сборки, точная анимация rest completion, haptics и Reduce Motion.

## Дополнительная ограниченная проверка: Strava, Lyfta, Strong

По последующему запросу проверен один официальный маршрут на каждое приложение. Этот appendix не является повторным аудитом и не превращает статичные screenshots в доказательство motion. Старые разделы приложений не изменены.

### Strava — официальный recorder/paused/save

**ST-D1:** [How do I Record an Activity on Strava? — официальный Strava Help Center](https://support.strava.com/en-us/articles/15402137-how-do-i-record-an-activity-on-strava). Проверено 2026-10-11; страница показывает относительное обновление «over 3 weeks ago», точная дата capture и app build неизвестны. iPhone на реальном screenshot, текст покрывает iOS и Android. Артефакты: `strava-official-recorder.md`, `strava-official-recorder-1.png`, `strava-official-recorder-2.png`, `strava-official-recorder-3.png`; исходные `.img` сохранены для проверки формата.

**Увидено [V, static]:** Paused-state использует очень крупный чёрный speed и меньшую distance на белом. Верхняя жёлтая плоскость объединяет Paused и elapsed. Нижняя белая sheet с drag handle содержит два больших круга: оранжевый Resume и чёрный Finish с текстовыми подписями. Save Activity — отдельная форма с типом спорта, описанием, map preview, media, дополнительными полями и широкой оранжевой CTA у нижнего края. Это сильный benchmark разделения оперативного экрана на расстоянии и подробного оформления результата.

**Документировано [D]:** карта/статистика переключаются жестом или collapse icon; нижняя sheet раскрывает дополнительные controls; Pause предшествует Finish, а Finish открывает Save Activity. У ride во время записи показывается current speed, на паузе — average speed. Все три официальных файла проверены Pillow: один PNG, два JPEG, по **1 кадру**; это не GIF/video и не доказательство анимационной физики.

**Готовая вставка:**

> Официальная справка дополнительно подтверждает двухрежимный recorder: карта и крупная статистика переключаются, а действия доступны из нижней sheet. В опубликованном iPhone Paused-screen жёлтая шапка явно кодирует остановку, показатели скорости/дистанции очень крупные; Resume и Finish — большие подписанные controls снизу. Finish ведёт к отдельной Save Activity форме со sticky нижней CTA. Скриншоты подтверждают иерархию, цвет статуса и размещение controls; motion открытия sheet и перехода к save в проверенном официальном материале отсутствует. [ST-D1]

### Strong — официальный log → rest → finish

**SR-D1:** [About Rest Timer — официальный Strong Help Center](https://help.strongapp.io/article/231-rest-timer), last updated **2021-02-08**, iPhone screenshots; инструкция также заявлена для Android. **SR-D2:** [How do I perform a workout with Strong?](https://help.strongapp.io/article/229-my-first-workout), last updated **2022-02-14**. Артефакты: `strong-official-rest.md`, `strong-official-rest-1.png`, `strong-official-rest-2.png`, `strong-official-rest-3.png`, `strong-official-workout.md`, `strong-official-workout-1.png`, `strong-official-workout-2.png`.

**Увидено [V,H, static]:** после отмеченного checkbox строка подхода окрашена светло-зелёным; сверху слева синий rest chip `1:59`, справа зелёный Finish. Развёрнутый Rest Timer — белая крупная modal card поверх затемнённого журнала: большое синее кольцо, жирный остаток `2:30`, меньшая исходная длительность `3:00`, нижние **−10s / +10s / Skip**. Настройка Auto Rest Timer разделяет Working/Warm-up и даёт wheel picker. Все скачанные пять изображений имеют по одному кадру; GIF/MP4 в проверенных статьях не найден.

**Документировано [D,H]:** timer автоматически запускается после completion set; его можно открыть в крупный режим и поправить длительность. Finish доступен до выполнения всех упражнений; workout затем находится в History и может быть сохранён как template. Это закрывает причинную UX-цепочку документацией, но **не** timing/easing/автоанимацию текущего приложения. Старые синие/зелёные controls нельзя автоматически считать токенами последней сборки.

**Готовая вставка:**

> Официальная документация 2021–2022 годов подтверждает связь checkbox подхода с автозапуском rest timer и два размера его представления: компактный chip в журнале и крупная modal card с кольцом, остатком, исходной длительностью, −10s/+10s и Skip. Working и Warm-up получают отдельные настройки. Эти исторические реальные screenshots полезны как benchmark временной иерархии; сама анимация текущего rest countdown или перехода в modal не наблюдалась. [SR-D1; SR-D2]

### Lyfta — официальный маршрут проверен, marketing не засчитан как real-session motion

**LY-D1:** [New Features Alert: Import/Export & Rest Timer! — Lyfta](https://www.lyfta.app/whats-new/ios/new-features-alert-importexport-rest-timer-2023-09-09), дата **2023-09-09**, явно iOS. Документирует появление live rest countdown, но не содержит GIF/MP4 или последовательности реального журнала. Сохранён `lyfta-official-rest.md`.

**LY-V1 — ограниченный/отклонённый источник motion:** [Lyfta Workout tracker](https://www.youtube.com/watch?v=rYDWUjfMCeM), канал **Lyfta**, опубликовано **2026-09-29**, 15 секунд. Официальность канала проверена ссылкой на `youtube.com/@lyfta` с [Lyfta Usage](https://www.lyfta.app/usage). Скачаны `lyfta-official-rYDWUjfMCeM.mp4`, `.info.json`, contact sheets и покадровые jpg. Это **рекламная композиция** с телефоном, заголовками Tracking/Progress и вынесенными наружу графиками/record badge. В 00:03–00:06 показано последовательное закрашивание строк подходов и reward, но нет достаточного основания считать это непрерывной записью реального взаимодействия приложения. Поэтому оно **не засчитано** как наблюдение logging/rest motion.

**Готовая вставка только для evidence boundary:**

> Дополнительный официальный release note подтверждает live rest countdown на iOS с сентября 2023 года. Найденный официальный ролик сентября 2026 года является рекламным монтажом и не закрывает проверку реального rest/logging flow. По текущим AppLlama-скриншотам можно оценивать состояния, по release note — наличие функции; физика перехода, actual countdown completion и поведение background timer остаются визуально непроверенными. [LY-D1; LY-V1 — только provenance, не UI-motion evidence]

### Журнал ограниченной дополнительной проверки

- Web-поиск официальных Strava/Strong Help и Lyfta rest timer → ST-D1, SR-D1, SR-D2, LY-D1. Все ссылки открыты и относящиеся к HUD изображения реально просмотрены.
- `https://www.lyfta.app/tutorials` возвращает 404; `https://www.lyfta.app/usage` доступен, но преимущественно содержит App Store artwork и маркетинговые описания. Эти иллюстрации не заменяют real-session recording.
- YouTube search `Lyfta app rest timer tutorial` и `Strava record activity mobile tutorial Strava` дал преимущественно сторонние how-to. В рамках ограниченного official-route scope они не скачивались.
- После подтверждения официального канала Lyfta с сайта просмотрены первые 35 публичных video titles. Наиболее релевантный 15-секундный app ролик LY-V1 скачан и разобран; он рекламный, остальные видимые titles преимущественно упражнения. Дальнейший широкий поиск остановлен по ограничению задачи.
- По Strava и Strong найден новый **официальный static/documented evidence**, но не найден быстро доступный official GIF/MP4 на проверенных страницах. В отчёте это не должно называться закрытой motion-проверкой.
