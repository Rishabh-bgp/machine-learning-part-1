# Reproducing

Environment used: Linux, Python 3.13.5; pinned packages in `requirements.txt`.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/download_data.py
cd notebooks && jupyter nbconvert --to notebook --execute --inplace *.ipynb
```
Both notebooks run in well under a minute on a laptop CPU. Seeds are fixed, so results should match up to small
library-version differences. scikit-learn 1.9 prints a FutureWarning about `SVC(probability=True)`; it is harmless.
