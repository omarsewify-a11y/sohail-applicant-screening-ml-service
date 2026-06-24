# Evaluation Module — Applicant Screening ML Service

## Overview

This module is responsible for evaluating the performance of the trained applicant screening model without retraining it.

It checks whether the model is suitable for deployment by analyzing its predictions on a test dataset.

---

## What This Module Does

- Loads the pre-trained model (`model.joblib`)
- Loads the dataset (`applicants.csv`)
- Reproduces the same train/test split using `random_state=42`
- Generates predictions on the test set
- Evaluates performance using:
  - Accuracy
  - Confusion Matrix
  - Precision, Recall, F1-score
- Plots and saves the confusion matrix as an image
- Provides a final business verdict: **GO or NEEDS WORK**

---

## Files in this Folder

- `evaluate_model.py` → main evaluation script
- `confusion_matrix.png` → visual evaluation output
- `EVALUATION_REPORT.md` → detailed business interpretation

---

## How to Run

Make sure you are in the project root directory, then run:

```bash
python evaluation/evaluate_model.py
