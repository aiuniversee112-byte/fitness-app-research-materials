# MacroFactor

## Onboarding questions

### Appllama recording — Basics, Goal and Program

This is the nutrition app onboarding. Optional explanatory-chat responses are included; informational questions such as “How was your program designed?” are not requests for user data.

- Consent — Do you accept the Terms of Service and Privacy Policy?
- Apple Health — Would you like to sync your data with Apple Health?
- Basic profile — What is your sex?
- Basic profile — When were you born?
- Body data — What is your height?
- Body data — What is your weight?
- Weight history — Have you ever weighed more than 100 kilograms?
- Weight trend — How has your weight trended over the past few weeks?
- Body composition — What is your body-fat level?
- Exercise frequency — How often do you exercise?
- Daily activity — How active are you outside exercise, during work and leisure?
- Training experience — What is your experience level with lifting?
- Training experience — What is your experience level with cardio?
- Calorie estimate — Acknowledge the estimate or ask how it was calculated.
- Calorie education — Confirm your understanding or ask why expenditure matters and whether the estimate is right.
- Adaptive coaching — Confirm your understanding or ask about the advanced algorithm.
- Attribution — How did you learn about us?
- Affiliate referral — If an affiliate referred you, enter their code.
- Weight goal — What is your goal: lose, maintain or gain weight?
- Weight goal — What is your target weight?
- Goal pace — What is your target rate of weight change?
- Diet — What is your preferred diet?
- Calorie floor — What calorie floor do you prefer?
- Training plan — What training will you do during this program?
- Weekly calories — How would you like to distribute calories throughout the week?
- Protein — What is your preferred protein intake?

### User recording — later food-logging preference

The recording begins in an existing account; it does not show initial registration or the onboarding questionnaire.

- Food logging — Choose how to add food to an hour: a persistent plus button or a long-press shortcut.

## Evidence index

Full step analysis is in [steps.json](../steps.json). These are observed states, not a claim that every state is a distinct linear onboarding step.

| Step ID | Source | Time (s) | Screen | Description |
|---|---|---:|---|---|
| `spl_qafbw` | static |  | [PNG](../../MacroFactor/spl_qafbw.png) | Научный подход и простой ввод еды |
| `onb_dlw0x` | static |  | [PNG](../../MacroFactor/onb_dlw0x.png) | Обещание приватности |
| `onb_y9p7y` | static |  | [PNG](../../MacroFactor/onb_y9p7y.png) | Карта из трёх этапов: Basics |
| `onb_d55h0` | static |  | [PNG](../../MacroFactor/onb_d55h0.png) | Необязательная синхронизация Apple Health |
| `onb_lp23s` | static |  | [PNG](../../MacroFactor/onb_lp23s.png) | Пол для расчёта |
| `onb_l5x1m` | static |  | [PNG](../../MacroFactor/onb_l5x1m.png) | Дата рождения |
| `onb_5v8fl` | static |  | [PNG](../../MacroFactor/onb_5v8fl.png) | Рост и единицы |
| `onb_1ocml` | static |  | [PNG](../../MacroFactor/onb_1ocml.png) | Текущий вес |
| `onb_yiihn` | static |  | [PNG](../../MacroFactor/onb_yiihn.png) | История высокого веса |
| `onb_vwfos` | static |  | [PNG](../../MacroFactor/onb_vwfos.png) | Последняя динамика веса |
| `onb_k922v` | static |  | [PNG](../../MacroFactor/onb_k922v.png) | Визуальная оценка процента жира |
| `onb_mezp9` | static |  | [PNG](../../MacroFactor/onb_mezp9.png) | Частота упражнений |
| `onb_h9m4g` | static |  | [PNG](../../MacroFactor/onb_h9m4g.png) | Активность вне тренировок |
| `onb_2066l` | static |  | [PNG](../../MacroFactor/onb_2066l.png) | Опыт силовых занятий |
| `onb_u417w` | static |  | [PNG](../../MacroFactor/onb_u417w.png) | Опыт кардио |
| `onb_8o7y2` | static |  | [PNG](../../MacroFactor/onb_8o7y2.png) | Объяснение расхода калорий в чате |
| `onb_bvoml` | static |  | [PNG](../../MacroFactor/onb_bvoml.png) | Как алгоритм уточняет расход |
| `onb_0xc2g` | static |  | [PNG](../../MacroFactor/onb_0xc2g.png) | Отзывы после объяснения алгоритма |
| `onb_zdllr` | static |  | [PNG](../../MacroFactor/onb_zdllr.png) | Источник привлечения |
| `onb_fewcl` | static |  | [PNG](../../MacroFactor/onb_fewcl.png) | Переход к этапу Goal |
| `onb_3rnj3` | static |  | [PNG](../../MacroFactor/onb_3rnj3.png) | Цель веса |
| `onb_1op3x` | static |  | [PNG](../../MacroFactor/onb_1op3x.png) | Целевой вес и скорость |
| `onb_ncgp9` | static |  | [PNG](../../MacroFactor/onb_ncgp9.png) | Сводка выбранной цели |
| `onb_1yvtn` | static |  | [PNG](../../MacroFactor/onb_1yvtn.png) | Переход к этапу Program |
| `onb_ooart` | static |  | [PNG](../../MacroFactor/onb_ooart.png) | Предпочитаемая диета |
| `onb_50ds1` | static |  | [PNG](../../MacroFactor/onb_50ds1.png) | Минимальный калорийный порог |
| `onb_9e4q4` | static |  | [PNG](../../MacroFactor/onb_9e4q4.png) | Вид тренировок в программе |
| `onb_zl10y` | static |  | [PNG](../../MacroFactor/onb_zl10y.png) | Распределение калорий по неделе |
| `onb_nf3d6` | static |  | [PNG](../../MacroFactor/onb_nf3d6.png) | Предпочтение по белку |
| `onb_1qmef` | static |  | [PNG](../../MacroFactor/onb_1qmef.png) | План готов: переходное состояние |
| `onb_ofpsm` | static |  | [PNG](../../MacroFactor/onb_ofpsm.png) | Итоговая макропрограмма |
| `onb_vawl3` | static |  | [PNG](../../MacroFactor/onb_vawl3.png) | Презентация функции Strategy |
| `onb_crcho` | static |  | [PNG](../../MacroFactor/onb_crcho.png) | Что входит в продукт |
| `onb_a0y3s` | static |  | [PNG](../../MacroFactor/onb_a0y3s.png) | Награда за просмотр длинной презентации |
| `pay_lxt3u` | static |  | [PNG](../../MacroFactor/pay_lxt3u.png) | Три тарифа и бесплатная неделя |
| `onb_jmt6w-0003` | mcp_video | 3.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0003.png) | Научный подход и простой ввод еды |
| `onb_jmt6w-0005` | mcp_video | 7.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0005.png) | Обещание приватности |
| `onb_jmt6w-0007` | mcp_video | 8.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0007.png) | Карта из трёх этапов: Basics |
| `onb_jmt6w-0009` | mcp_video | 10.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0009.png) | Необязательная синхронизация Apple Health |
| `onb_jmt6w-0013` | mcp_video | 12.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0013.png) | Пол для расчёта |
| `onb_jmt6w-0017` | mcp_video | 19.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0017.png) | Дата рождения |
| `onb_jmt6w-0021` | mcp_video | 21.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0021.png) | Рост и единицы |
| `onb_jmt6w-0032` | mcp_video | 30.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0032.png) | Текущий вес |
| `onb_jmt6w-0035` | mcp_video | 34.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0035.png) | История высокого веса |
| `onb_jmt6w-0039` | mcp_video | 40.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0039.png) | Последняя динамика веса |
| `onb_jmt6w-0046` | mcp_video | 49.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0046.png) | Визуальная оценка процента жира |
| `onb_jmt6w-0049` | mcp_video | 51.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0049.png) | Частота упражнений |
| `onb_jmt6w-0053` | mcp_video | 55.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0053.png) | Активность вне тренировок |
| `onb_jmt6w-0057` | mcp_video | 59.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0057.png) | Опыт силовых занятий |
| `onb_jmt6w-0060` | mcp_video | 61.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0060.png) | Опыт кардио |
| `onb_jmt6w-0066` | mcp_video | 69.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0066.png) | Начальная ветка обучающего чата |
| `onb_jmt6w-0070` | mcp_video | 74.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0070.png) | Объяснение расхода калорий в чате |
| `onb_jmt6w-0084` | mcp_video | 84.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0084.png) | Как алгоритм уточняет расход |
| `onb_jmt6w-0089` | mcp_video | 88.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0089.png) | Отзывы после объяснения алгоритма |
| `onb_jmt6w-0090` | mcp_video | 88.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0090.png) | Дополнительные отзывы: Bárbara, Michael, Julie |
| `onb_jmt6w-0091` | mcp_video | 89.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0091.png) | Дополнительные отзывы: Mike и Sergio |
| `onb_jmt6w-0093` | mcp_video | 91.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0093.png) | Источник привлечения |
| `onb_jmt6w-0095` | mcp_video | 93.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0095.png) | Переход к этапу Goal |
| `onb_jmt6w-0099` | mcp_video | 97.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0099.png) | Цель веса |
| `onb_jmt6w-0102` | mcp_video | 99.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0102.png) | Целевой вес и скорость |
| `onb_jmt6w-0104` | mcp_video | 103.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0104.png) | Сводка выбранной цели |
| `onb_jmt6w-0108` | mcp_video | 106.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0108.png) | Полный текст прогноза даты |
| `onb_jmt6w-0110` | mcp_video | 107.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0110.png) | Переход к этапу Program |
| `onb_jmt6w-0113` | mcp_video | 112.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0113.png) | Предпочитаемая диета |
| `onb_jmt6w-0116` | mcp_video | 116.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0116.png) | Минимальный калорийный порог |
| `onb_jmt6w-0125` | mcp_video | 126.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0125.png) | Вид тренировок в программе |
| `onb_jmt6w-0127` | mcp_video | 128.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0127.png) | Распределение калорий по неделе |
| `onb_jmt6w-0130` | mcp_video | 132.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0130.png) | Предпочтение по белку |
| `onb_jmt6w-0134` | mcp_video | 134.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0134.png) | Последовательность расчёта макроплана |
| `onb_jmt6w-0136` | mcp_video | 135.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0136.png) | План готов: переходное состояние |
| `onb_jmt6w-0137` | mcp_video | 138.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0137.png) | Итоговая макропрограмма |
| `onb_jmt6w-0139` | mcp_video | 139.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0139.png) | Нижняя часть объяснения макроплана |
| `onb_jmt6w-0141` | mcp_video | 140.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0141.png) | Переход к этапу Program |
| `onb_jmt6w-0143` | mcp_video | 141.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0143.png) | Презентация функции Strategy |
| `onb_jmt6w-0146` | mcp_video | 143.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0146.png) | Что входит в продукт |
| `onb_jmt6w-0147` | mcp_video | 143.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0147.png) | Презентация: наука и прогресс |
| `onb_jmt6w-0148` | mcp_video | 144.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0148.png) | Презентация: персональная технология |
| `onb_jmt6w-0149` | mcp_video | 144.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0149.png) | Презентация: регулярность логирования |
| `onb_jmt6w-0152` | mcp_video | 147.0 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0152.png) | Награда за просмотр длинной презентации |
| `onb_jmt6w-0153` | mcp_video | 147.5 | [PNG](../../onboarding/frames/macrofactor/onb_jmt6w-0153.png) | Три тарифа и бесплатная неделя |
| `spl_dqoub-0006` | mcp_video | 4.0 | [PNG](../../onboarding/frames/macrofactor/spl_dqoub-0006.png) | Научный подход и простой ввод еды |
| `U07-0023` | user_video | 13.0 | [PNG](../../onboarding/frames/macrofactor/U07-0023.png) | Tutorial: роль расхода энергии |
| `U07-0038` | user_video | 22.0 | [PNG](../../onboarding/frames/macrofactor/U07-0038.png) | Tutorial: тренд вместо шума веса |
| `U07-0068` | user_video | 44.0 | [PNG](../../onboarding/frames/macrofactor/U07-0068.png) | Tutorial: поддержка цели |
| `U07-0111` | user_video | 77.0 | [PNG](../../onboarding/frames/macrofactor/U07-0111.png) | Tutorial: ввод фактического веса |
| `U07-0156` | user_video | 121.0 | [PNG](../../onboarding/frames/macrofactor/U07-0156.png) | Подсказка Daily Step Count |
| `U07-0321` | user_video | 270.5 | [PNG](../../onboarding/frames/macrofactor/U07-0321.png) | Управление активной EUR-подпиской |
| `U07-0324` | user_video | 272.5 | [PNG](../../onboarding/frames/macrofactor/U07-0324.png) | EUR: варианты смены тарифа и Bundle |
| `U07-0381` | user_video | 321.5 | [PNG](../../onboarding/frames/macrofactor/U07-0381.png) | Объяснение жеста добавления еды |
| `U07-0641` | user_video | 550.5 | [PNG](../../onboarding/frames/macrofactor/U07-0641.png) | Повторное включение обучения |
