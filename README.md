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

## 🔗 Other repositories by Rishabh Aryan

| Repository | Description | Live |
|---|---|---|
| [100-days-of-python](https://github.com/Rishabh-bgp/100-days-of-python) | My original, offline, no-API-key solutions to all 100 projects of the 100 Days of Code Python bootcamp curriculum… | — |
| [Agentic-Engineering-Ebook](https://github.com/Rishabh-bgp/Agentic-Engineering-Ebook) | Agentic Engineering is a practical notebook-book on specifying, generating, verifying, and refining multi-tenant… | — |
| [beed-ml-study](https://github.com/Rishabh-bgp/beed-ml-study) | Provenance audit and leakage-aware benchmark of seizure-type classifiers on the Bangalore EEG Epilepsy Dataset — IIT… | — |
| [boston-house-price-prediction](https://github.com/Rishabh-bgp/boston-house-price-prediction) | Boston house price prediction with machine learning: scikit-learn gradient boosting, repeated K-fold CV, race… | [open](https://rishabh-bgp.github.io/boston-house-price-prediction/) |
| [Brain-Computer-Interfaces-and-Cognitive-Computing-An-Introduction](https://github.com/Rishabh-bgp/Brain-Computer-Interfaces-and-Cognitive-Computing-An-Introduction) | Brain–computer interfaces (BCIs) link neural activity to external devices, translating brain signals via algorithms… | — |
| [building-a-virtual-cell-in-python](https://github.com/Rishabh-bgp/building-a-virtual-cell-in-python) | A cell has a normal gene-activity pattern. Knock out one gene and that pattern changes. This project trains a small… | — |
| [Chronic-Kidney-Disease-Stage-Identification-in-HIV-Infected-Patients-Using-Supervised-ML](https://github.com/Rishabh-bgp/Chronic-Kidney-Disease-Stage-Identification-in-HIV-Infected-Patients-Using-Supervised-ML) | ML is transforming Chronic Kidney Disease (CKD) detection in HIV patients, catching early asymptomatic stages to… | — |
| [cobratate](https://github.com/Rishabh-bgp/cobratate) | Cobratate, an esoteric imperative programming language. Tate-flavored syntax, ordinary semantics, and a Python… | [open](https://rishabh-bgp.github.io/cobratate/) |
| [coda-synth](https://github.com/Rishabh-bgp/coda-synth) | CoDA-Synth: stylometric detection of LLM-rewritten dark-web documents with sparse TF-IDF + LinearSVC. Research lab,… | [open](https://shale-ember-delta-kite.grok.me/) |
| [IIT-ROPAR-GENAI-FOUNDATIONS](https://github.com/Rishabh-bgp/IIT-ROPAR-GENAI-FOUNDATIONS) | Free open-source Generative AI foundations ebooks (2026) covering Claude, Grok, Gemini, Cursor, OpenAI and more —… | — |
| [iris-classification](https://github.com/Rishabh-bgp/iris-classification) | Iris flower classification in Python: scikit-learn model comparison, tuning and evaluation, FastAPI /predict API,… | [open](https://rishabh-bgp.github.io/iris-classification/) |
| [kbc-game](https://github.com/Rishabh-bgp/kbc-game) | Kaun Banega Crorepati (KBC) quiz game for the terminal in Python: 16-question prize ladder, safe levels and 4… | — |
| [knn-classifier](https://github.com/Rishabh-bgp/knn-classifier) | Simple K-Nearest Neighbors classifier on the classic Iris dataset using scikit-learn. Loads data, trains the model,… | — |
| [linear-regression-model-](https://github.com/Rishabh-bgp/linear-regression-model-) | Supervised linear regression on the scikit-learn diabetes dataset. A single feature (BMI) is used to predict… | — |
| [logistic-regression](https://github.com/Rishabh-bgp/logistic-regression) | This graduate capstone applies multi-class logistic regression to the Iris dataset. It includes EDA, stratified… | — |
| [logistics-website-capstone](https://github.com/Rishabh-bgp/logistics-website-capstone) | Logistics website capstone: Kargonaut Logistics, a premium freight site mixing claymorphism, glassmorphism and… | [open](https://rishabh-bgp.github.io/logistics-website-capstone/) |
| [lovelight-leap](https://github.com/Rishabh-bgp/lovelight-leap) | 💖 Lovelight Leap: a love-themed 2D platformer in vanilla JS canvas. 4 worlds, a boss you cheer up, original… | [open](https://rishabh-bgp.github.io/lovelight-leap/) |
| [Meeting-of-Machines-Consumer-Agents-Seller-Agents-and-Hidden-Fulfilment-Risk-in-Online-Retail](https://github.com/Rishabh-bgp/Meeting-of-Machines-Consumer-Agents-Seller-Agents-and-Hidden-Fulfilment-Risk-in-Online-Retail) | Agentic commerce lets shopping and seller agents place orders without showing operational truth. This IS case argues… | — |
| [morocco-city-aware-load-forecasting](https://github.com/Rishabh-bgp/morocco-city-aware-load-forecasting) | City-aware short-term load forecasting and peak detection on high-resolution Moroccan smart-meter data (5 zones).… | — |
| [NIELIT-DATA-SCIENCE](https://github.com/Rishabh-bgp/NIELIT-DATA-SCIENCE) | Hands-on NumPy, Pandas, and Matplotlib Jupyter notebooks for the NIELIT Data Science curriculum — practical,… | — |
| [NIELIT-MACHINE-LEARNING-PROJECTS](https://github.com/Rishabh-bgp/NIELIT-MACHINE-LEARNING-PROJECTS) | Nineteen end-to-end machine learning projects: classification, regression, clustering, and recommendation, with… | — |
| [NIELIT-PYTHON-](https://github.com/Rishabh-bgp/NIELIT-PYTHON-) | Open-source Python teaching notebooks: a language reference and five capstone programs, with detailed documentation.… | — |
| [pan-cancer-classification](https://github.com/Rishabh-bgp/pan-cancer-classification) | Leakage, equivalence, conformal reliability and data efficiency on the UCI TCGA Pan-Cancer RNA-Seq dataset — IIT… | — |
| [Predicting-Hot-Events-in-the-Early-Period-through-Bayesian-Model-for-Social-Networks](https://github.com/Rishabh-bgp/Predicting-Hot-Events-in-the-Early-Period-through-Bayesian-Model-for-Social-Networks) | This notebook details the implementation and evaluation of a Bayesian perspective Early stage Event Prediction… | — |
| [prediction-as-power](https://github.com/Rishabh-bgp/prediction-as-power) | Laboratory and working paper on prediction as power in European electricity markets. A DE-like hourly simulator… | — |
| [real-estate-valuation-taiwan](https://github.com/Rishabh-bgp/real-estate-valuation-taiwan) | Taiwan real estate valuation (Xindian, New Taipei): house price per ping prediction with scikit-learn gradient… | [open](https://rishabh-bgp.github.io/real-estate-valuation-taiwan/) |
| [snakes-and-ladders](https://github.com/Rishabh-bgp/snakes-and-ladders) | 🐍🪜 Original Snakes & Ladders browser game: hand-drawn SVG snakes and ladders, 3D dice, 2-4 humans or bots, sound,… | [open](https://rishabh-bgp.github.io/snakes-and-ladders/) |
| [spam-scan](https://github.com/Rishabh-bgp/spam-scan) | Explainable spam, phishing & Indian-scam detector for SMS/email (English, Hindi, Hinglish): TF-IDF + Logistic… | [open](https://spam-scan.onrender.com) |
| [vedic-math-hybrid-kt](https://github.com/Rishabh-bgp/vedic-math-hybrid-kt) | Hybrid Vedic Math AI: rule-based sutras (Urdhva-Tiryagbhyam, Nikhilam, Yavadunam) plus RF classifier that cleans… | — |
| [wind-turbine-power-model](https://github.com/Rishabh-bgp/wind-turbine-power-model) | Single-turbine power curves + wind-farm simulation. Weibull wind stats, hourly NASA-style speed data, and… | — |
| [zoo-website-capstone](https://github.com/Rishabh-bgp/zoo-website-capstone) | Capstone project: a fictional zoo website built twice — a beginner-style simple version and a cinematic advanced… | [open](https://rishabh-bgp.github.io/zoo-website-capstone/) |
