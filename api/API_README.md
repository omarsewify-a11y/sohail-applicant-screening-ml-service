# API_README — Sohail Applicant Screening API

## Overview

This FastAPI application serves the Sohail Applicant Screening ML model as a real prediction API.
It loads the model and encoder trained by Khaled and exposes two endpoints:
- `GET /health` — check if the API is running
- `POST /predict` — predict whether an applicant should be shortlisted or reviewed later

---

## Project Structure

```
api/
├── main.py          # FastAPI application
├── model.joblib     # Trained model from Khaled (do NOT retrain)
├── encoder.joblib   # Fitted LabelEncoder from Khaled (do NOT refit)
└── API_README.md    # This file
```

---

## Requirements

Install dependencies:

```bash
pip install fastapi uvicorn pydantic scikit-learn joblib pandas
```

---

## How to Run

```bash
cd api
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

Interactive docs (Swagger UI): `http://127.0.0.1:8000/docs`

---

## Endpoints

### GET /health

Check if the API is running.

**Request:**
```bash
curl http://127.0.0.1:8000/health
```

**Response:**
```json
{
  "status": "ok",
  "message": "Applicant Screening API is running."
}
```

---

### POST /predict

Predict whether an applicant should be shortlisted or reviewed later.

**Input fields (JSON body):**

| Field | Type | Required | Description |
|---|---|---|---|
| gpa | float | Yes | Applicant GPA (0.0 – 4.0) |
| skills_count | int | Yes | Number of technical skills |
| prior_projects | int | Yes | Number of completed projects |
| track | string | Yes | Internship track: "AI", "Data", or "Web" |

**Response fields:**

| Field | Type | Description |
|---|---|---|
| prediction | string | "shortlist" or "review_later" |
| confidence | float | Model confidence score (0.0 – 1.0) |

---

## Example Requests

### Applicant 1 — Strong AI candidate

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"gpa": 3.8, "skills_count": 8, "prior_projects": 5, "track": "AI"}'
```

**Response:**
```json
{
  "prediction": "shortlist",
  "confidence": 0.9985
}
```

---

### Applicant 2 — Weak Web candidate

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"gpa": 2.5, "skills_count": 2, "prior_projects": 0, "track": "Web"}'
```

**Response:**
```json
{
  "prediction": "review_later",
  "confidence": 0.9923
}
```

---

### Applicant 3 — Average Data candidate

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"gpa": 3.2, "skills_count": 5, "prior_projects": 3, "track": "Data"}'
```

**Response:**
```json
{
  "prediction": "shortlist",
  "confidence": 0.7732
}
```

---

## Notes

- The model and encoder are loaded directly from Khaled's trained files — no retraining is done.
- The `track` column is encoded using Khaled's fitted `LabelEncoder` to ensure identical preprocessing.
- Input validation is handled by Pydantic — invalid inputs return a `422 Unprocessable Entity` error.
- The `confidence` value reflects how certain the model is about its prediction.

---

## Internship Project

AI Foundation Internship Program — Sohail Smart Solutions

Easa — Deployment & Prediction API Layer
