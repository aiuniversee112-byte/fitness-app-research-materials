# Fitbod

## Onboarding questions

### Appllama recording — initial onboarding

The recorded branch skips calorie calculation and continues with email registration.

- Fitness goal — What's your top fitness goal?
- Training routine — Which best describes your current strength-training routine?
- Training location — Where do you primarily plan on training?
- Training frequency — How many days per week can you usually strength train?
- Notifications — Would you like a workout preview on training days? Allow or decline notifications.
- Calorie tracking — Do you want to calculate the calories you burn each workout? Connect Apple Health, enter details manually, or skip.
- Registration — Choose Apple, Google or email to save your workout program.
- Registration — What is your first name?
- Registration — What is your last name?
- Registration — What is your email address?
- Registration — Create a password with at least 6 characters.
- Consent — Do you agree to the Terms & Conditions and confirm that you are at least 13 years old?
- Trial reminder — Would you like a reminder before your trial ends?

### User recording — first-use and strength assessment

The recording starts inside an already configured account. It does not show the initial onboarding; the assessment is exited during exercise 2 of 3.

- Workout duration — Choose a duration for this workout or set it as your default.
- Apple Health — Would you like to sync body-composition and movement data with Apple Health?
- Strength assessment — Would you like to begin the 5-minute strength assessment or do it later?
- Exercise variation — Choose Plank Hold or Crunches; select the variation that challenges you most.
- Assessment result — Adjust your plank-hold time if needed, then log it.
- Exercise variation — Choose Burpee or Air Squat; select the variation that challenges you most.
- Assessment exit — Exit the assessment without saving, or keep going?

## Evidence index

Full step analysis is in [steps.json](../steps.json). These are observed states, not a claim that every state is a distinct linear onboarding step.

| Step ID | Source | Time (s) | Screen | Description |
|---|---|---:|---|---|
| `spl_9dwou` | static |  | [PNG](../../Fitbod/spl_9dwou.png) | Заставка бренда |
| `onb_zwp0a` | static |  | [PNG](../../Fitbod/onb_zwp0a.png) | Вход в персональный тренинг |
| `onb_fzlcn` | static |  | [PNG](../../Fitbod/onb_fzlcn.png) | Главная цель |
| `onb_ts1nm` | static |  | [PNG](../../Fitbod/onb_ts1nm.png) | Текущая силовая привычка |
| `onb_vwf3p` | static |  | [PNG](../../Fitbod/onb_vwf3p.png) | Место и доступное оборудование |
| `onb_i7trw` | static |  | [PNG](../../Fitbod/onb_i7trw.png) | Частота тренировок |
| `onb_kbblk` | static |  | [PNG](../../Fitbod/onb_kbblk.png) | Разрешение напоминаний с пользой |
| `onb_6fopo` | static |  | [PNG](../../Fitbod/onb_6fopo.png) | Калории и Apple Health |
| `onb_wjhjt` | static |  | [PNG](../../Fitbod/onb_wjhjt.png) | Создание профиля |
| `onb_j2xtk` | static |  | [PNG](../../Fitbod/onb_j2xtk.png) | Промежуточное подтверждение готовности |
| `onb_klap0` | static |  | [PNG](../../Fitbod/onb_klap0.png) | Обоснование готового плана |
| `onb_3dem3` | static |  | [PNG](../../Fitbod/onb_3dem3.png) | Сохранить готовую программу через аккаунт |
| `onb_1ccos` | static |  | [PNG](../../Fitbod/onb_1ccos.png) | Регистрация по email |
| `onb_5bl5t` | static |  | [PNG](../../Fitbod/onb_5bl5t.png) | Принятие условий |
| `onb_tffef` | static |  | [PNG](../../Fitbod/onb_tffef.png) | Синхронизация данных |
| `pay_oa5kx` | static |  | [PNG](../../Fitbod/pay_oa5kx.png) | Годовая подписка с семидневным триалом |
| `pay_f5i0t` | static |  | [PNG](../../Fitbod/pay_f5i0t.png) | Месячная подписка с тем же триалом |
| `welcome-screen-001-spl_bn0gt-step-01` | mcp_video | 2.5 | [PNG](../../onboarding/frames/fitbod/welcome-screen-001-spl_bn0gt-step-01.png) | Переход из заставки к hero |
| `welcome-screen-001-spl_bn0gt-step-02` | mcp_video | 3 | [PNG](../../onboarding/frames/fitbod/welcome-screen-001-spl_bn0gt-step-02.png) | Вход в персональный тренинг |
| `onboarding-001-onb_u6lbw-step-01` | mcp_video | 0 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-01.png) | Hero с движущимся фоном |
| `onboarding-001-onb_u6lbw-step-02` | mcp_video | 10 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-02.png) | Главная цель |
| `onboarding-001-onb_u6lbw-step-03` | mcp_video | 14.5 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-03.png) | Текущая силовая привычка |
| `onboarding-001-onb_u6lbw-step-04` | mcp_video | 22.5 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-04.png) | Место и доступное оборудование |
| `onboarding-001-onb_u6lbw-step-05` | mcp_video | 29.5 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-05.png) | Частота тренировок |
| `onboarding-001-onb_u6lbw-step-06` | mcp_video | 34 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-06.png) | Разрешение напоминаний с пользой |
| `onboarding-001-onb_u6lbw-step-07` | mcp_video | 34.5 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-07.png) | Системное разрешение уведомлений Fitbod |
| `onboarding-001-onb_u6lbw-step-08` | mcp_video | 40 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-08.png) | Предложение калорий и отказ Maybe later |
| `onboarding-001-onb_u6lbw-step-09` | mcp_video | 47 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-09.png) | Три сообщения генерации |
| `onboarding-001-onb_u6lbw-step-10` | mcp_video | 49 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-10.png) | Промежуточное подтверждение готовности |
| `onboarding-001-onb_u6lbw-step-11` | mcp_video | 52 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-11.png) | Обоснование готового плана |
| `onboarding-001-onb_u6lbw-step-12` | mcp_video | 54.5 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-12.png) | Сохранить готовую программу через аккаунт |
| `onboarding-001-onb_u6lbw-step-13` | mcp_video | 74.5 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-13.png) | Заполненная регистрация по email |
| `onboarding-001-onb_u6lbw-step-14` | mcp_video | 76 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-14.png) | Принятие условий |
| `onboarding-001-onb_u6lbw-step-15` | mcp_video | 86.5 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-15.png) | Создание аккаунта и несколько фаз синхронизации |
| `onboarding-001-onb_u6lbw-step-16` | mcp_video | 99.5 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-16.png) | Годовая подписка с семидневным триалом |
| `onboarding-001-onb_u6lbw-step-17` | mcp_video | 104 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-17.png) | Месячная подписка с тем же триалом |
| `onboarding-001-onb_u6lbw-step-18` | mcp_video | 105 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-18.png) | Годовая подписка с семидневным триалом |
| `onboarding-001-onb_u6lbw-step-19` | mcp_video | 106.5 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-19.png) | Месячная подписка с тем же триалом |
| `onboarding-001-onb_u6lbw-step-20` | mcp_video | 108.5 | [PNG](../../onboarding/frames/fitbod/onboarding-001-onb_u6lbw-step-20.png) | Системное подтверждение месячной подписки |
| `U01-0001` | user_video | 0.5 | [PNG](../../onboarding/frames/fitbod/U01-0001.png) | Объяснение начальных весов |
| `U01-0005` | user_video | 3.5 | [PNG](../../onboarding/frames/fitbod/U01-0005.png) | Настройка длительности с двумя областями применения |
| `U01-0075` | user_video | 83.5 | [PNG](../../onboarding/frames/fitbod/U01-0075.png) | Нет оценки до трёх тренировок и предложение Health |
| `U01-0091` | user_video | 139 | [PNG](../../onboarding/frames/fitbod/U01-0091.png) | Пустая статистика конкретной мышцы |
| `U01-0205` | user_video | 217.5 | [PNG](../../onboarding/frames/fitbod/U01-0205.png) | Состояние уже активного триала |
| `U01-0311` | user_video | 326 | [PNG](../../onboarding/frames/fitbod/U01-0311.png) | Подсказка о частоте рекомендации упражнения |
| `U01-0388` | user_video | 434.5 | [PNG](../../onboarding/frames/fitbod/U01-0388.png) | Предупреждение о незалогированных сетах |
| `U01-0425` | user_video | 465 | [PNG](../../onboarding/frames/fitbod/U01-0425.png) | Введение в калибровку силы |
| `U01-0429` | user_video | 468 | [PNG](../../onboarding/frames/fitbod/U01-0429.png) | 1/3 — выбор планки или скручиваний |
| `U01-0430` | user_video | 470.5 | [PNG](../../onboarding/frames/fitbod/U01-0430.png) | Подготовка к таймеру |
| `U01-0434` | user_video | 481 | [PNG](../../onboarding/frames/fitbod/U01-0434.png) | Остановка и фиксация времени |
| `U01-0436` | user_video | 482 | [PNG](../../onboarding/frames/fitbod/U01-0436.png) | Коррекция результата |
| `U01-0438` | user_video | 483 | [PNG](../../onboarding/frames/fitbod/U01-0438.png) | Положительная обратная связь после теста |
| `U01-0446` | user_video | 508 | [PNG](../../onboarding/frames/fitbod/U01-0446.png) | 2/3 — выбор бёрпи или приседаний |
| `U01-0448` | user_video | 509.5 | [PNG](../../onboarding/frames/fitbod/U01-0448.png) | Выход из незавершённой калибровки |
