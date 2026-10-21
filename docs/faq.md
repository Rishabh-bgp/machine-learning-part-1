# FAQ and limitations

**Why isn't `insurance.csv` in the repo?**  No explicit licence was found at its source, so it is downloaded by
`scripts/download_data.py` instead of being redistributed.

**Can I use the heart model clinically?**  No. 303 patients from one centre; this is a learning exercise.

**Why is the hold-out score higher than CV?**  One 61-patient split is noisy; trust the 10-fold CV averages.

## Limitations
* Small, old, single-source datasets; no external validation.
* Hyperparameters are fixed, not tuned.
* The insurance data has only six attributes, so large residuals remain for some people.
