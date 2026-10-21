# Methodology

## Common principles
* All preprocessing lives inside scikit-learn `Pipeline` / `ColumnTransformer` objects, so it is fitted on training
  folds only (no data leakage).
* A trivial baseline (majority class / mean) is always reported.
* Fixed random seed `SEED = 42`.

## Heart disease classification
* Target: presence (`num` 1–4) vs absence (0).
* Numeric (`age, trestbps, chol, thalach, oldpeak, ca`): median imputation + standard scaling.
* Categorical (`sex, cp, fbs, restecg, exang, slope, thal`): most-frequent imputation + one-hot encoding.
* Models: logistic regression, KNN (k = 15), SVM (RBF), random forest (400 trees), gradient boosting.
* Validation: stratified 10-fold CV (accuracy, F1, ROC-AUC) + one stratified 80/20 hold-out for confusion matrix,
  ROC curve and permutation importance (30 repeats, ROC-AUC).

## Insurance cost regression
* Engineered features: `obese` (BMI ≥ 30) and `smoker_obese` (smoker and obese).
* Numeric: standard scaling; categorical (`sex, smoker, region`): one-hot encoding (drop first).
* Models: linear regression, ridge (α = 1), linear regression on log(charges), random forest (400 trees,
  min leaf 3), gradient boosting (depth 3, lr 0.05, 300 trees).
* Validation: 10-fold CV (RMSE, MAE, R²) + one 80/20 hold-out for predicted-vs-actual, residuals and permutation
  importance.
