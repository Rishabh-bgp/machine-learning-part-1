"""Download the datasets used by the notebooks into ../data/.

* UCI Heart Disease (Cleveland subset) - CC BY 4.0, also bundled in data/.
* Medical Cost Personal dataset (insurance.csv) - no explicit licence was found
  at the source, so it is NOT redistributed here; this script fetches it.
"""
from pathlib import Path
import urllib.request

DATA = Path(__file__).resolve().parent.parent / "data"
SOURCES = {
    "processed.cleveland.data":
        "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data",
    "insurance.csv":
        "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv",
}

def main() -> None:
    DATA.mkdir(exist_ok=True)
    for name, url in SOURCES.items():
        target = DATA / name
        if target.exists():
            print(f"[skip] {name} already present")
            continue
        print(f"[get ] {name} <- {url}")
        urllib.request.urlretrieve(url, target)
    print("done")

if __name__ == "__main__":
    main()
