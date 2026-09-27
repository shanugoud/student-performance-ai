import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model/performance_model.pkl")

st.set_page_config(
    page_title="AI Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Student Performance Predictor")

st.write(
    "Enter student details below to predict the expected final score "
    "using a trained Machine Learning model."
)

st.divider()

st.subheader("Student Information")

study_hours = st.number_input(
    "Study Hours per Day",
    min_value=0.0,
    max_value=12.0,
    value=5.0,
    step=0.5
)

attendance = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=80.0,
    step=1.0
)

previous_score = st.number_input(
    "Previous Score",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)

assignments_completed = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=10,
    value=8,
    step=1
)

sleep_hours = st.number_input(
    "Sleep Hours per Day",
    min_value=0.0,
    max_value=12.0,
    value=7.0,
    step=0.5
)

participation = st.number_input(
    "Class Participation Percentage",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)

st.divider()

if st.button("Predict Final Score"):
    input_data = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_score": previous_score,
        "assignments_completed": assignments_completed,
        "sleep_hours": sleep_hours,
        "participation": participation
    }])

    prediction = model.predict(input_data)[0]
    prediction = max(0, min(100, prediction))

    if prediction >= 75:
        category = "Excellent"
        advice = "Great performance! Continue maintaining consistent study habits."
    elif prediction >= 60:
        category = "Good"
        advice = "Your performance is on a good track. Increasing study time and assignment completion may help."
    elif prediction >= 40:
        category = "Average"
        advice = "Try to increase study time, attendance, and assignment completion."
    else:
        category = "Needs Improvement"
        advice = "Focus on regular study, attendance, assignments, and class participation."

    st.subheader("Prediction Result")

    st.write("### Predicted Final Score")
    st.write(f"## {prediction:.2f}/100")

    st.write(f"**Performance Category:** {category}")

    st.info(f"**Study Advice:** {advice}")

st.divider()

st.caption(
    "This project uses a synthetic student-performance dataset "
    "for educational purposes."
)