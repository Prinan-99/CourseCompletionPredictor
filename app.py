import streamlit as st
import pandas as pd
import joblib


model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")
selected_features = joblib.load("selected_features.pkl")
label_encoder = joblib.load("label_encoder.pkl")
course_default_map = joblib.load("course_default_map.pkl")
course_names = joblib.load("course_names.pkl")

st.title("🎓 Course Completion Predictor")


student_name = st.text_input("Student Name ")


selected_course = st.selectbox(
    "Select Course",
    course_names,
    placeholder="Search course..."
)

if not selected_course:
    st.stop()

st.write("---")


st.subheader("📘 Course Details")

course_info = course_default_map[selected_course]

for col, val in course_info.items():
    st.text(f"{col}: {val}")

st.write("---")


st.subheader("🧍 Student Inputs (Manual Entry)")

student_inputs = {}

for feature in selected_features:

    # Skip course-level features (auto imported)
    if feature in course_info:
        continue

    # Conditional visibility (example)
    if feature == "Discount_Used" and student_inputs.get("Fees_Paid") != 1:
        continue

    # Detect numeric features
    if any(key in feature.lower() for key in [
        "age", "duration", "frequency", "hours", "score",
        "percentage", "submitted", "missed", "rating", "count",
        "rate", "login"
    ]):
        # Default slider ranges
        min_val = 0
        max_val = 200
        default_val = 0

        # Special ranges
        if "age" in feature.lower():
            min_val, max_val, default_val = 15, 60, 20

        elif "rating" in feature.lower():
            min_val, max_val, default_val = 0, 5, 3

        elif "percentage" in feature.lower() or "rate" in feature.lower():
            min_val, max_val, default_val = 0, 100, 50

        student_inputs[feature] = st.slider(
            feature,
            min_value=float(min_val),
            max_value=float(max_val),
            value=float(default_val)
        )

    # Categorical Yes/No → convert to 0/1
    else:
        choice = st.selectbox(feature, ["Yes", "No"])
        student_inputs[feature] = 1 if choice == "Yes" else 0

st.write("---")


final_input = {}

# Add course-level features
for f in selected_features:
    if f in course_info:
        val = course_info[f]
        # If course fields contain Yes/No convert
        if isinstance(val, str) and val in ["Yes", "No"]:
            val = 1 if val == "Yes" else 0
        final_input[f] = val

# Add student inputs
for f, v in student_inputs.items():
    final_input[f] = v

for col in selected_features:
    if col not in final_input:
        final_input[col] = 0  # missing dummy column → set to 0

# Convert to DataFrame
input_df = pd.DataFrame([final_input])


num_cols = input_df.select_dtypes(include=["int64", "float64"]).columns
input_df[num_cols] = scaler.transform(input_df[num_cols])


if st.button("Predict Completion"):
    pred = model.predict(input_df)[0]
    result = label_encoder.inverse_transform([pred])[0]

    if result == "Completed":
        msg = "✅ Completed"
    else:
        msg = "❌ Not Completed"

    if student_name.strip():
        st.success(f"🎯 Prediction for **{student_name}**: {msg}")
    else:
        st.success(f"🎯 Course Completion Prediction: {msg}")
