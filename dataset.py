import pandas as pd
import numpy as np


# 1. Reproducibility

np.random.seed(42)

num_students = 1000
rows = []


# 2. Generate Student Records

for i in range(num_students):
    # Unique student ID
    student_id = i + 1

    # Academic & behavioral features
    attendance_pct = np.random.uniform(50, 100)        # Attendance %
    avg_marks = np.random.uniform(40, 95)              # Average marks
    previous_failures = np.random.randint(0, 5)        # Past failed subjects
    student_backlogs = np.random.randint(0, 6)         # Current backlogs
    study_hours_per_week = np.random.randint(3, 25)    # Weekly study hours

    # Skill level abstraction
    skill_level = np.random.choice(
        ["Low", "Medium", "High"],
        p=[0.35, 0.40, 0.25]
    )

    # 3. Risk Score Calculation

    risk_score = 0.0

    if attendance_pct < 70:
        risk_score += 0.25
    if avg_marks < 60:
        risk_score += 0.25
    if previous_failures >= 2:
        risk_score += 0.15
    if student_backlogs >= 2:
        risk_score += 0.15
    if study_hours_per_week < 8:
        risk_score += 0.10
    if skill_level == "Low":
        risk_score += 0.10


    # 4. Convert Risk Score → Risk Level
 
    if risk_score >= 0.65:
        risk_level = "High"
    elif risk_score >= 0.35:
        risk_level = "Medium"
    else:
        risk_level = "Low"


    # 5. Append Row
 
    rows.append([
        student_id,
        attendance_pct,
        avg_marks,
        previous_failures,
        student_backlogs,
        study_hours_per_week,
        skill_level,
        risk_level
    ])


# 6. Create DataFrame

df = pd.DataFrame(rows, columns=[
    "student_id",
    "attendance_pct",
    "avg_marks",
    "previous_failures",
    "student_backlogs",
    "study_hours_per_week",
    "skill_level",
    "risk_level"
])


# 7. Save Dataset

df.to_csv("student_risk_data.csv", index=False)
print("Student risk dataset created successfully!")
