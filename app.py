import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ============================
# LOAD SCALER AND MODEL
# ============================
scaler = joblib.load("scaler.pkl")
model = joblib.load("xgb_model.pkl")

# FINAL SELECTED FEATURES
selected_features = [
    'Login_Frequency',
    'Time_Spent_Hours',
    'Assignments_Submitted',
    'Assignments_Missed',
    'Progress_Percentage',
    'Gender_Male',
    'Education_Level_Master',
    'Employment_Status_Student',
    'Internet_Connection_Quality_Medium',
    'Category_Programming'
]

st.title("🎓 Course Completion Prediction App")

st.write("Enter the student details below to predict whether they will complete the course.")

# ============================
# USER INPUTS
# ============================

# Numeric inputs
Login_Frequency = st.slider("Login Frequency", 0, 50, 10)
Time_Spent_Hours = st.slider("Time Spent (Hours)", 0, 200, 20)
Assignments_Submitted = st.slider("Assignments Submitted", 0, 20, 5)
Assignments_Missed = st.slider("Assignments Missed", 0, 20, 1)
Progress_Percentage = st.slider("Progress Percentage (%)", 0, 100, 50)

# Binary categorical (already converted to 0/1 in training)
Gender_Male = st.selectbox("Gender", ["Female", "Male"])
Gender_Male = 1 if Gender_Male == "Male" else 0

Education_Level_Master = st.selectbox(
    "Education Level (Master?)",
    ["No", "Yes"]
)
Education_Level_Master = 1 if Education_Level_Master == "Yes" else 0

Employment_Status_Student = st.selectbox(
    "Employment Status (Student?)",
    ["No", "Yes"]
)
Employment_Status_Student = 1 if Employment_Status_Student == "Yes" else 0

Internet_Connection_Quality_Medium = st.selectbox(
    "Internet Quality Medium?",
    ["No", "Yes"]
)
Internet_Connection_Quality_Medium = 1 if Internet_Connection_Quality_Medium == "Yes" else 0

Category_Programming = st.selectbox(
    "Course Category = Programming?",
    ["No", "Yes"]
)
Category_Programming = 1 if Category_Programming == "Yes" else 0

# ============================
# CREATE INPUT DATAFRAME
# ============================

input_data = pd.DataFrame([[
    Login_Frequency,
    Time_Spent_Hours,
    Assignments_Submitted,
    Assignments_Missed,
    Progress_Percentage,
    Gender_Male,
    Education_Level_Master,
    Employment_Status_Student,
    Internet_Connection_Quality_Medium,
    Category_Programming
]], columns=selected_features)

# ============================
# SCALE FEATURES
# ============================
scaled_input = scaler.transform(input_data)

# ============================
# PREDICT
# ============================
if st.button("Predict"):
    prediction = model.predict(scaled_input)[0]

    st.subheader("🔮 Prediction Result")
    if prediction == 1:
        st.success("✔ The student is likely to COMPLETE the course.")
    else:
        st.error("✘ The student is likely to DROP OUT.")
