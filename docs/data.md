# Data and licence decisions

## 1. UCI Heart Disease (Cleveland subset) — bundled
* File: `data/processed.cleveland.data` (303 rows, 14 columns, `?` = missing).
* Source: Janosi A., Steinbrunn W., Pfisterer M., Detrano R. (1989). *Heart Disease*. UCI Machine Learning Repository.
  doi:[10.24432/C52P4X](https://doi.org/10.24432/C52P4X) — https://archive.ics.uci.edu/dataset/45/heart+disease
* Licence: **Creative Commons Attribution 4.0 International (CC BY 4.0)**, as stated on the UCI page →
  redistribution with attribution is allowed, so the file is included.
* Missing values: `ca` (4), `thal` (2). Target: `num > 0` → disease (139) vs none (164).

## 2. Medical Cost Personal dataset (`insurance.csv`) — downloaded, not bundled
* Fetched by `scripts/download_data.py` from
  https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv
  (dataset from Brett Lantz, *Machine Learning with R*; also mirrored on Kaggle as "Medical Cost Personal Datasets").
* Licence: **no explicit licence was found** at that source, so the file is **not redistributed** in this repository.
* 1,338 rows, 7 columns (age, sex, bmi, children, smoker, region, charges); 0 missing values, 1 duplicate row (removed).
