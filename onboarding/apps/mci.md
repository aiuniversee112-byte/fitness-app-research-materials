# MCI – Personal Training AI

## Onboarding questions

### Appllama recording — initial onboarding

This route has no training experience and edits the estimated body-fat percentage. The recording ends at the PRO offers; no registration form is shown.

- Goals — Before we start, what brings you here? Choose up to three goals.
- Apple Health — Would you like to connect Apple Health?
- Basic profile — Choose your gender.
- Basic profile — When is your birthday?
- Body data — How tall are you?
- Body data — How much do you weigh?
- Body composition — Estimate your body-fat percentage.
- Training experience — How long have you been consistently doing strength training?
- Body-composition goal — What are you aiming for: weight loss, muscle gain, maintenance or recomposition?
- Training frequency — How often do you want to train?
- Split confirmation — Continue despite the warning that the training volume may not suit your experience?
- Training split — Choose your training split.
- Schedule — On which days would you like to place your training sessions?
- Workout duration — How long should each session last?
- Rest reminders — Would you like reminders when your rest is over?
- Notifications — Allow MCI to send notifications?
- Training location — Where will you train?
- Equipment — Confirm or edit the equipment available at your training location.
- Pain — Do you feel any pain? Select the body area and its severity.
- Daily activity — How active are you in your free time, apart from strength training?
- Work activity — What's your position and physical activity during work?
- Promo code — Do you have a promo code?

### User recording — experienced-user onboarding

A separate branch with muscle gain, self-rated experience and priority muscle groups. Registration occurs after the trial is activated.

- Tracking permission — Allow MCI to track your activity across other companies’ apps and websites?
- Goals — Before we start, what brings you here?
- Apple Health — Would you like to connect Apple Health?
- Basic profile — Choose your gender.
- Basic profile — When is your birthday?
- Body data — How tall are you?
- Body data — How much do you weigh?
- Body composition — Estimate your body-fat percentage.
- Training consistency — Have you been training continuously for the last 3 months?
- Training experience — How would you rate yourself?
- Body-composition goal — What are you aiming for?
- Muscle priorities — Where is your focus? Select up to two muscle groups.
- Training frequency — How often do you want to train?
- Training split — Choose your training split.
- Schedule — On which days would you like to place your training sessions?
- Workout duration — How long should each session last?
- Rest reminders — Would you like reminders when your rest is over?
- Training location — Where will you train?
- Equipment — Confirm or edit the equipment available at your training location.
- Pain — Do you feel any pain? Select the affected body areas.
- Daily activity — How active are you in your free time, apart from strength training?
- Work activity — What's your position and physical activity during work?
- Promo code — Do you have a promo code?
- Consent — Do you agree to the terms of use?
- Registration — Choose Google, Apple or email to save your progress.

### User recording — camera and first-workout setup

Later feature onboarding, after the initial dashboard. Camera-positioning instructions and warm-up explanations remain in the full screen-by-screen report.

- Camera permission — Allow MCI to access the camera for movement analysis and barcode scanning?
- First workout — Start a guided workout or skip because you already know MCI.
- Exercise notes — Add any notes about the exercise.
- Energy — How would you rate your energy level today?
- Soreness — Are your muscles sore? Select the affected muscles and rate the soreness.
- Strength test — Choose a challenging weight and enter your repetitions and weight.
- Reps in reserve — How many more repetitions could you have completed with proper form at the end of the set?
- Notifications — Allow MCI to send notifications?

## Evidence index

Full step analysis is in [steps.json](../steps.json). These are observed states, not a claim that every state is a distinct linear onboarding step.

| Step ID | Source | Time (s) | Screen | Description |
|---|---|---:|---|---|
| `spl_zejat` | static |  | [PNG](../../MCI/spl_zejat.png) | Заставка MCI |
| `onb_3qqpb` | static |  | [PNG](../../MCI/onb_3qqpb.png) | Персональный фитнес-тренер |
| `onb_yi6fa` | static |  | [PNG](../../MCI/onb_yi6fa.png) | Указание поддержки инновации |
| `onb_hnbaa` | static |  | [PNG](../../MCI/onb_hnbaa.png) | Причины прихода: несколько целей |
| `onb_9yfi2` | static |  | [PNG](../../MCI/onb_9yfi2.png) | Обещание достичь цели быстрее |
| `onb_yierk` | static |  | [PNG](../../MCI/onb_yierk.png) | Подключение Apple Health |
| `onb_brkeu` | static |  | [PNG](../../MCI/onb_brkeu.png) | Профиль: выбор пола |
| `onb_k8ahi` | static |  | [PNG](../../MCI/onb_k8ahi.png) | Профиль: дата рождения |
| `onb_xb4e0` | static |  | [PNG](../../MCI/onb_xb4e0.png) | Профиль: рост |
| `onb_fxkni` | static |  | [PNG](../../MCI/onb_fxkni.png) | Профиль: вес |
| `onb_t10h9` | static |  | [PNG](../../MCI/onb_t10h9.png) | Профиль: оценка процента жира |
| `onb_l98wu` | static |  | [PNG](../../MCI/onb_l98wu.png) | Переход от профиля к целям |
| `onb_euh27` | static |  | [PNG](../../MCI/onb_euh27.png) | Стаж силовых тренировок |
| `onb_1jv1o` | static |  | [PNG](../../MCI/onb_1jv1o.png) | Конкретный режим композиции тела |
| `onb_tbnw5` | static |  | [PNG](../../MCI/onb_tbnw5.png) | Социальное доказательство 91% |
| `onb_77x00` | static |  | [PNG](../../MCI/onb_77x00.png) | Переход к потребностям |
| `onb_3nud2` | static |  | [PNG](../../MCI/onb_3nud2.png) | Желаемая частота: два раза |
| `onb_ckdms` | static |  | [PNG](../../MCI/onb_ckdms.png) | Предупреждение о сплите |
| `onb_f0rxz` | static |  | [PNG](../../MCI/onb_f0rxz.png) | Желаемая частота: четыре раза |
| `onb_c8kcs` | static |  | [PNG](../../MCI/onb_c8kcs.png) | Выбор тренировочного сплита |
| `onb_k630u` | static |  | [PNG](../../MCI/onb_k630u.png) | Недельное планирование и время |
| `onb_kzsyv` | static |  | [PNG](../../MCI/onb_kzsyv.png) | Напоминание об окончании отдыха |
| `onb_2diqf` | static |  | [PNG](../../MCI/onb_2diqf.png) | Разрешение уведомлений iOS |
| `onb_9e4gb` | static |  | [PNG](../../MCI/onb_9e4gb.png) | Место занятий и оборудование |
| `onb_l4g3k` | static |  | [PNG](../../MCI/onb_l4g3k.png) | Боль по зонам на модели тела |
| `onb_u4zu0` | static |  | [PNG](../../MCI/onb_u4zu0.png) | Активность в свободное время |
| `onb_3dno2` | static |  | [PNG](../../MCI/onb_3dno2.png) | Поза и нагрузка на работе |
| `onb_lhz05` | static |  | [PNG](../../MCI/onb_lhz05.png) | Финальный расчёт |
| `onb_tpz5c` | static |  | [PNG](../../MCI/onb_tpz5c.png) | Промо PRO перед ценой |
| `pay_y41jm` | static |  | [PNG](../../MCI/pay_y41jm.png) | Три срока подписки и семидневная проба |
| `onb_bh4bf-0001` | mcp_video | 0.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0001.png) | Персональный фитнес-тренер |
| `onb_bh4bf-0005` | mcp_video | 3.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0005.png) | Указание поддержки инновации |
| `onb_bh4bf-0007` | mcp_video | 6.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0007.png) | Причины прихода: несколько целей |
| `onb_bh4bf-0009` | mcp_video | 8.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0009.png) | Ограничение числа целей |
| `onb_bh4bf-0013` | mcp_video | 11.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0013.png) | Обещание достичь цели быстрее |
| `onb_bh4bf-0014` | mcp_video | 13.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0014.png) | Подключение Apple Health |
| `onb_bh4bf-0016` | mcp_video | 14.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0016.png) | Профиль: выбор пола |
| `onb_bh4bf-0027` | mcp_video | 23.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0027.png) | Профиль: дата рождения |
| `onb_bh4bf-0030` | mcp_video | 27.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0030.png) | Профиль: рост |
| `onb_bh4bf-0032` | mcp_video | 29.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0032.png) | Профиль: вес |
| `onb_bh4bf-0033` | mcp_video | 31.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0033.png) | Начальная оценка жира: 25% |
| `onb_bh4bf-0036` | mcp_video | 33.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0036.png) | Профиль: оценка процента жира |
| `onb_bh4bf-0039` | mcp_video | 36.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0039.png) | Переход от профиля к целям |
| `onb_bh4bf-0044` | mcp_video | 40.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0044.png) | Стаж силовых тренировок |
| `onb_bh4bf-0045` | mcp_video | 42.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0045.png) | Конкретный режим композиции тела |
| `onb_bh4bf-0046` | mcp_video | 43.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0046.png) | Предупреждение при выборе набора мышц |
| `onb_bh4bf-0048` | mcp_video | 44.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0048.png) | Конкретный режим композиции тела |
| `onb_bh4bf-0056` | mcp_video | 48.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0056.png) | Социальное доказательство 91% |
| `onb_bh4bf-0058` | mcp_video | 51.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0058.png) | Переход к потребностям |
| `onb_bh4bf-0060` | mcp_video | 53.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0060.png) | Желаемая частота: два раза |
| `onb_bh4bf-0061` | mcp_video | 53.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0061.png) | Предупреждение о сплите |
| `onb_bh4bf-0064` | mcp_video | 56.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0064.png) | Желаемая частота: четыре раза |
| `onb_bh4bf-0065` | mcp_video | 59.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0065.png) | Выбор тренировочного сплита |
| `onb_bh4bf-0066` | mcp_video | 60.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0066.png) | Недельное планирование и время |
| `onb_bh4bf-0071` | mcp_video | 66.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0071.png) | Напоминание об окончании отдыха |
| `onb_bh4bf-0072` | mcp_video | 67.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0072.png) | Разрешение уведомлений iOS |
| `onb_bh4bf-0074` | mcp_video | 69.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0074.png) | Место занятий и оборудование |
| `onb_bh4bf-0079` | mcp_video | 74.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0079.png) | Боль по зонам на модели тела |
| `onb_bh4bf-0087` | mcp_video | 80.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0087.png) | Активность в свободное время |
| `onb_bh4bf-0091` | mcp_video | 87.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0091.png) | Поза и нагрузка на работе |
| `onb_bh4bf-0094` | mcp_video | 90.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0094.png) | Финальный расчёт |
| `onb_bh4bf-0098` | mcp_video | 94.5 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0098.png) | Промо PRO перед ценой |
| `onb_bh4bf-0102` | mcp_video | 97.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0102.png) | Три срока подписки и семидневная проба |
| `onb_bh4bf-0103` | mcp_video | 99.0 | [PNG](../../onboarding/frames/mci/onb_bh4bf-0103.png) | Промо PRO перед ценой |
| `spl_qpr9u-0001` | mcp_video | 0.0 | [PNG](../../onboarding/frames/mci/spl_qpr9u-0001.png) | Заставка MCI |
| `U10-0003` | user_video | 1.0 | [PNG](../../onboarding/frames/mci/U10-0003.png) | Заставка MCI |
| `U10-0004` | user_video | 1.5 | [PNG](../../onboarding/frames/mci/U10-0004.png) | Рекламное отслеживание до welcome |
| `U10-0008` | user_video | 3.5 | [PNG](../../onboarding/frames/mci/U10-0008.png) | Персональный фитнес-тренер |
| `U10-0011` | user_video | 6.5 | [PNG](../../onboarding/frames/mci/U10-0011.png) | Указание поддержки инновации |
| `U10-0013` | user_video | 10.0 | [PNG](../../onboarding/frames/mci/U10-0013.png) | Причины прихода: несколько целей |
| `U10-0015` | user_video | 12.0 | [PNG](../../onboarding/frames/mci/U10-0015.png) | Обещание достичь цели быстрее |
| `U10-0016` | user_video | 13.5 | [PNG](../../onboarding/frames/mci/U10-0016.png) | Подключение Apple Health |
| `U10-0021` | user_video | 17.5 | [PNG](../../onboarding/frames/mci/U10-0021.png) | Профиль: выбор пола |
| `U10-0022` | user_video | 20.5 | [PNG](../../onboarding/frames/mci/U10-0022.png) | Профиль: дата рождения |
| `U10-0044` | user_video | 35.5 | [PNG](../../onboarding/frames/mci/U10-0044.png) | Профиль: рост |
| `U10-0047` | user_video | 39.0 | [PNG](../../onboarding/frames/mci/U10-0047.png) | Профиль: вес |
| `U10-0048` | user_video | 42.0 | [PNG](../../onboarding/frames/mci/U10-0048.png) | Процент жира: средний диапазон |
| `U10-0053` | user_video | 44.5 | [PNG](../../onboarding/frames/mci/U10-0053.png) | Процент жира: низкие диапазоны |
| `U10-0055` | user_video | 45.5 | [PNG](../../onboarding/frames/mci/U10-0055.png) | Процент жира: высокие диапазоны |
| `U10-0081` | user_video | 83.5 | [PNG](../../onboarding/frames/mci/U10-0081.png) | Переход от профиля к целям |
| `U10-0085` | user_video | 91.5 | [PNG](../../onboarding/frames/mci/U10-0085.png) | Стаж силовых тренировок |
| `U10-0087` | user_video | 94.5 | [PNG](../../onboarding/frames/mci/U10-0087.png) | Самооценка опытного пользователя |
| `U10-0088` | user_video | 95.5 | [PNG](../../onboarding/frames/mci/U10-0088.png) | Ветка набора мышц |
| `U10-0120` | user_video | 111.5 | [PNG](../../onboarding/frames/mci/U10-0120.png) | Социальное доказательство 91% |
| `U10-0122` | user_video | 118.0 | [PNG](../../onboarding/frames/mci/U10-0122.png) | Фокус на двух мышечных группах |
| `U10-0125` | user_video | 121.5 | [PNG](../../onboarding/frames/mci/U10-0125.png) | Лимит фокусных мышц |
| `U10-0131` | user_video | 137.0 | [PNG](../../onboarding/frames/mci/U10-0131.png) | Переход к потребностям |
| `U10-0134` | user_video | 140.0 | [PNG](../../onboarding/frames/mci/U10-0134.png) | Желаемая частота: два раза |
| `U10-0135` | user_video | 142.5 | [PNG](../../onboarding/frames/mci/U10-0135.png) | Сплиты для трёх занятий |
| `U10-0136` | user_video | 143.0 | [PNG](../../onboarding/frames/mci/U10-0136.png) | Full body выбран |
| `U10-0140` | user_video | 150.5 | [PNG](../../onboarding/frames/mci/U10-0140.png) | Недельное планирование и время |
| `U10-0141` | user_video | 156.5 | [PNG](../../onboarding/frames/mci/U10-0141.png) | Напоминание об окончании отдыха |
| `U10-0143` | user_video | 158.0 | [PNG](../../onboarding/frames/mci/U10-0143.png) | Место занятий и оборудование |
| `U10-0145` | user_video | 161.0 | [PNG](../../onboarding/frames/mci/U10-0145.png) | Боль по зонам на модели тела |
| `U10-0147` | user_video | 163.0 | [PNG](../../onboarding/frames/mci/U10-0147.png) | Карта боли: поворот назад |
| `U10-0151` | user_video | 173.0 | [PNG](../../onboarding/frames/mci/U10-0151.png) | Активность в свободное время |
| `U10-0153` | user_video | 178.5 | [PNG](../../onboarding/frames/mci/U10-0153.png) | Поза и нагрузка на работе |
| `U10-0157` | user_video | 180.5 | [PNG](../../onboarding/frames/mci/U10-0157.png) | Рабочие нагрузки: дополнительные варианты |
| `U10-0161` | user_video | 183.5 | [PNG](../../onboarding/frames/mci/U10-0161.png) | Финальный расчёт |
| `U10-0162` | user_video | 188.0 | [PNG](../../onboarding/frames/mci/U10-0162.png) | Промо PRO перед ценой |
| `U10-0164` | user_video | 191.0 | [PNG](../../onboarding/frames/mci/U10-0164.png) | Пейволл U10 в евро |
| `U10-0166` | user_video | 192.0 | [PNG](../../onboarding/frames/mci/U10-0166.png) | Пейволл: состав покупки |
| `U10-0171` | user_video | 196.0 | [PNG](../../onboarding/frames/mci/U10-0171.png) | Пейволл: before/after-кейсы |
| `U10-0177` | user_video | 215.0 | [PNG](../../onboarding/frames/mci/U10-0177.png) | Пейволл: анализ техники |
| `U10-0180` | user_video | 218.5 | [PNG](../../onboarding/frames/mci/U10-0180.png) | Системные условия трёхмесячного триала |
| `U10-0191` | user_video | 234.5 | [PNG](../../onboarding/frames/mci/U10-0191.png) | Успешная активация подписки |
| `U10-0194` | user_video | 239.5 | [PNG](../../onboarding/frames/mci/U10-0194.png) | Аккаунт после подписки |
| `U10-0196` | user_video | 240.5 | [PNG](../../onboarding/frames/mci/U10-0196.png) | Sign in with Apple: переход |
| `U10-0205` | user_video | 249.5 | [PNG](../../onboarding/frames/mci/U10-0205.png) | Первый Dashboard |
| `U10-0225` | user_video | 355.5 | [PNG](../../onboarding/frames/mci/U10-0225.png) | Начало анализа подвижности |
| `U10-0227` | user_video | 358.5 | [PNG](../../onboarding/frames/mci/U10-0227.png) | Камера 1/5: установка телефона |
| `U10-0247` | user_video | 368.5 | [PNG](../../onboarding/frames/mci/U10-0247.png) | Камера 2/5: позиция человека |
| `U10-0266` | user_video | 378.0 | [PNG](../../onboarding/frames/mci/U10-0266.png) | Камера 3/5: фон и свет |
| `U10-0276` | user_video | 389.0 | [PNG](../../onboarding/frames/mci/U10-0276.png) | Камера 4/5: одежда |
| `U10-0277` | user_video | 391.5 | [PNG](../../onboarding/frames/mci/U10-0277.png) | Камера 5/5: звук |
| `U10-0280` | user_video | 394.5 | [PNG](../../onboarding/frames/mci/U10-0280.png) | Инструкция теста Finger-Floor-Distance |
| `U10-0282` | user_video | 396.0 | [PNG](../../onboarding/frames/mci/U10-0282.png) | Разрешение камеры |
| `U10-0381` | user_video | 614.0 | [PNG](../../onboarding/frames/mci/U10-0381.png) | Первый запуск сканера еды |
| `U10-0470` | user_video | 808.0 | [PNG](../../onboarding/frames/mci/U10-0470.png) | Первая тренировка: guided mode |
| `U10-0479` | user_video | 828.5 | [PNG](../../onboarding/frames/mci/U10-0479.png) | Заметки об упражнении |
| `U10-0483` | user_video | 834.0 | [PNG](../../onboarding/frames/mci/U10-0483.png) | Strength Test 1/5: энергия |
| `U10-0487` | user_video | 843.0 | [PNG](../../onboarding/frames/mci/U10-0487.png) | Strength Test 2/5: болезненность |
| `U10-0490` | user_video | 845.0 | [PNG](../../onboarding/frames/mci/U10-0490.png) | Strength Test 3/5: разминка |
| `U10-0492` | user_video | 849.5 | [PNG](../../onboarding/frames/mci/U10-0492.png) | Strength Test 4/5: нагрузка и повторения |
| `U10-0501` | user_video | 876.5 | [PNG](../../onboarding/frames/mci/U10-0501.png) | Strength Test 5/5: обучение RIR |
| `U10-0502` | user_video | 877.0 | [PNG](../../onboarding/frames/mci/U10-0502.png) | Корректировка после теста |
| `U10-0505` | user_video | 880.0 | [PNG](../../onboarding/frames/mci/U10-0505.png) | Реальный запрос push после теста |
| `U10-0509` | user_video | 885.5 | [PNG](../../onboarding/frames/mci/U10-0509.png) | Подсказка пропуска отдыха |
