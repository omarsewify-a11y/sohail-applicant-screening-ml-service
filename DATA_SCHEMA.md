Dataset Description

This dataset is used to predict whether an internship applicant should be shortlisted or reviewed later.

Columns

gpa

Type: Float
Range: 0.0 – 4.0
Example: 3.8
skills_count

Type: Integer
Range: 0+
Example: 8
prior_projects

Type: Integer
Range: 0+
Example: 5
track

Type: Categorical (String)
Allowed Values:

AI
Data
Web
Example:

AI
shortlisted

Type: Integer
Target Variable
Values:

1 = Shortlisted
0 = Review Later
Features (X)

gpa
skills_count
prior_projects
track
Target (y)

shortlisted
Preprocessing

The track column is encoded using LabelEncoder before model training.

Reproducibility

All train/test splits use:

random_state = 42

How to Load the Model

import joblib

model = joblib.load("model.joblib")
