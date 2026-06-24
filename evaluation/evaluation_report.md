# Model Evaluation Report

## Objective

Evaluate Khaled's trained applicant screening model without retraining it.

---

## Evaluation Method

- Loaded the pre-trained model from `model.joblib`
- Used the same dataset (`applicants.csv`)
- Reproduced the same train/test split using `random_state=42`
- Evaluated using:
  - Accuracy
  - Confusion Matrix
  - Precision
  - Recall
  - F1-Score

---

## Results

### Accuracy

1.00 (100%)

### Confusion Matrix

```
[[4]]
```

### Classification Report

```
              precision    recall  f1-score   support

           1       1.00      1.00      1.00         4

    accuracy                           1.00         4
   macro avg       1.00      1.00      1.00         4
weighted avg       1.00      1.00      1.00         4
```

---

## Why Accuracy Alone Is Not Enough

Accuracy can be misleading when datasets are imbalanced. A model may achieve high accuracy while still making poor decisions for minority classes.

For this reason, the model was also evaluated using:
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## Business Interpretation

- True Positive: Good applicant correctly shortlisted.
- True Negative: Poor applicant correctly rejected.
- False Positive: Poor applicant incorrectly accepted.
- False Negative: Good applicant incorrectly rejected.

In applicant screening, false negatives can be costly because qualified applicants may be missed.

The evaluation showed no misclassifications in the test set.

---

## Precision vs Recall

- Precision = 1.00
- Recall = 1.00
- F1-Score = 1.00

This means all shortlisted applicants in the test set were correctly identified.

---

## Final Verdict

### GO

The model achieved 100% accuracy, precision, recall, and F1-score on the provided test set and produced no classification errors during evaluation.

However, the dataset used for testing is very small (4 samples in the test set), so additional testing on a larger dataset is recommended before real-world deployment.
