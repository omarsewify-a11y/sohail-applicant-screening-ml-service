import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal

# Load model and encoder trained by Khaled — never retrain
model = joblib.load("model.joblib")
encoder = joblib.load("encoder.joblib")

app = FastAPI(
    title="Sohail Applicant Screening API",
    description="Predicts whether an internship applicant should be Shortlisted or Reviewed Later.",
    version="1.0.0"
)

# Input schema based on Khaled's DATA_SCHEMA.md
class ApplicantInput(BaseModel):
    gpa: float = Field(..., ge=0.0, le=4.0, description="Applicant GPA (0.0 - 4.0)")
    skills_count: int = Field(..., ge=0, description="Number of technical skills")
    prior_projects: int = Field(..., ge=0, description="Number of completed projects")
    track: Literal["AI", "Data", "Web"] = Field(..., description="Internship track: AI, Data, or Web")

# Output schema
class PredictionOutput(BaseModel):
    prediction: str
    confidence: float


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Applicant Screening API is running."}


@app.post("/predict", response_model=PredictionOutput)
def predict(applicant: ApplicantInput):
    # Apply the SAME preprocessing Khaled used — encode track with his fitted encoder
    track_encoded = encoder.transform([applicant.track])[0]

    # Build feature DataFrame in the same order and column names as training
    features = pd.DataFrame([{
        "gpa": applicant.gpa,
        "skills_count": applicant.skills_count,
        "prior_projects": applicant.prior_projects,
        "track": track_encoded
    }])

    # Predict
    prediction_int = model.predict(features)[0]
    confidence = float(max(model.predict_proba(features)[0]))

    # Map to human-readable label
    prediction_label = "shortlist" if prediction_int == 1 else "review_later"

    return PredictionOutput(prediction=prediction_label, confidence=round(confidence, 4))
