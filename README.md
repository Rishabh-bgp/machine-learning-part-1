<div align="center">

# Machine Learning Part 1 — Heart Disease Classification & Insurance Cost Regression in Python (scikit-learn)

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9.1-F7931E?logo=scikitlearn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-3.0.6-150458?logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-notebooks-F37626?logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue)

</div>

Beginner-to-intermediate **machine learning in Python** with **scikit-learn**, pandas and seaborn: two complete,
executed Jupyter notebooks covering **exploratory data analysis (EDA)**, data cleaning, preprocessing pipelines,
**classification** (heart disease prediction) and **regression** (medical insurance cost prediction), with
cross-validation, evaluation metrics, plots and model interpretation.

> Practice work by **Rishabh Aryan**, written after the IIT Ropar guest lectures in the **6-Month Industrial Training & Certification Program in Artificial Intelligence and Machine Learning**, jointly offered by [IIT Ropar](https://www.iitrpr.ac.in/) and [NIELIT Ropar](https://www.nielit.gov.in/ropar/), under MeitY, Govt. of India.

---

## 📚 Topics and notebooks

| # | Notebook | Task | Topics | Models |
|---|---|---|---|---|
| 1 | [01_heart_disease_classification.ipynb](notebooks/01_heart_disease_classification.ipynb) | Binary classification | EDA, missing values, `ColumnTransformer` pipelines, one-hot encoding, scaling, stratified 10-fold CV, confusion matrix, ROC curve, permutation importance | Logistic regression, KNN, SVM (RBF), random forest, gradient boosting, majority baseline |
| 2 | [02_insurance_cost_regression.ipynb](notebooks/02_insurance_cost_regression.ipynb) | Regression | EDA, duplicates, skewed target, feature engineering (obesity, smoker × obesity), encoding, 10-fold CV, residual analysis, permutation importance | Linear regression, ridge, log-target linear regression, random forest, gradient boosting, mean baseline |

## 📈 Results (from the executed notebooks)

### Heart disease — 10-fold stratified CV (303 patients)
| Model | Accuracy (± SD) | F1 | ROC-AUC |
|---|---|---|---|
| Logistic regression | 0.845 ± 0.054 | 0.823 | **0.912** |
| SVM (RBF) | 0.838 ± 0.048 | 0.814 | 0.906 |
| Random forest | 0.815 ± 0.054 | 0.791 | 0.905 |
| K-nearest neighbours | 0.815 ± 0.055 | 0.788 | 0.901 |
| Gradient boosting | 0.815 ± 0.047 | 0.792 | 0.891 |
| Majority baseline | 0.541 ± 0.011 | 0.000 | 0.500 |

Hold-out (80/20) logistic regression: accuracy **0.869**, ROC-AUC **0.958** (61 test patients).
Top permutation-importance features: `ca`, `cp`, `slope`.

### Insurance charges — 10-fold CV (1,337 rows after removing 1 duplicate)
| Model | RMSE | MAE | R² (± SD) |
|---|---|---|---|
| Linear regression | 4,475 | 2,473 | **0.859** ± 0.035 |
| Ridge (α = 1) | 4,475 | 2,479 | 0.859 ± 0.035 |
| Gradient boosting | 4,611 | 2,521 | 0.851 ± 0.034 |
| Random forest | 4,626 | 2,587 | 0.850 ± 0.030 |
| Linear regression, log target | 8,714 | 4,111 | 0.454 ± 0.204 |
| Mean baseline | 12,078 | 9,094 | −0.003 |

Hold-out gradient boosting: RMSE **4,246**, MAE **2,485**, R² **0.902**.
Main cost drivers (permutation importance): `smoker_obese`, `smoker`, `age`.

More detail: [docs/results.md](docs/results.md).

## 🚀 How to run
```bash
git clone https://github.com/Rishabh-bgp/machine-learning-part-1.git
cd machine-learning-part-1
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/download_data.py                         # fetches insurance.csv (heart data is bundled)
jupyter notebook notebooks/
```
Re-run everything headlessly: `cd notebooks && jupyter nbconvert --to notebook --execute --inplace *.ipynb`

## 📂 Repository structure
```
notebooks/   two executed Jupyter notebooks
data/        processed.cleveland.data (UCI Heart Disease, CC BY 4.0)
scripts/     download_data.py
docs/        data, methodology, results, reproducing, FAQ
```

## 📖 Documentation
| Page | Contents |
|---|---|
| [docs/data.md](docs/data.md) | Dataset sources and licence decisions |
| [docs/methodology.md](docs/methodology.md) | Pipelines, models, validation |
| [docs/results.md](docs/results.md) | Full results and interpretation |
| [docs/reproducing.md](docs/reproducing.md) | Environment and commands |
| [docs/faq.md](docs/faq.md) | FAQ and limitations |

## ⚖️ Licence
Code and documentation: MIT © 2026 Rishabh Aryan. Data licences: see [docs/data.md](docs/data.md).
