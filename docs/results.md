# Results

All numbers are copied from the saved outputs of the executed notebooks.

## Heart disease
See the README table for 10-fold CV. Hold-out logistic regression (61 patients):

| Class | Precision | Recall | F1 |
|---|---|---|---|
| no disease | 0.931 | 0.818 | 0.871 |
| disease | 0.812 | 0.929 | 0.867 |

Accuracy 0.869, ROC-AUC 0.958. Permutation importance (drop in ROC-AUC): ca 0.096, cp 0.035, slope 0.017,
oldpeak 0.012, thal 0.012, exang 0.011.

**Interpretation.** Every model clearly beats the majority baseline (0.541). Differences among the real models
(accuracy 0.815–0.845) are smaller than the fold-to-fold SD (≈ 0.05), so the simple, interpretable logistic regression
is a sensible choice. The single hold-out split is small, so its numbers are noisier than the CV estimates.

## Insurance charges
See the README table for 10-fold CV. Hold-out gradient boosting: RMSE 4,246, MAE 2,485, R² 0.902.

Smokers: median charges 34,456 vs 7,346 for non-smokers (274 vs 1,063 people).
Permutation importance (drop in R²): smoker_obese 0.572, smoker 0.311, age 0.163, bmi 0.066, children 0.016,
region 0.003, sex 0.000, obese 0.000.

**Interpretation.** With the engineered `smoker_obese` feature, plain linear regression (R² 0.859) matches or slightly
beats the tree ensembles (0.850–0.851). Modelling log(charges) linearly does much worse (R² 0.454), because the
smoker × obesity effect is additive in cost, not multiplicative.
