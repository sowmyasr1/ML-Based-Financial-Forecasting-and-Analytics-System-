import streamlit as st
import pandas as pd
from joblib import load
import os

# Load the trained model
model_path = os.path.join("models", "rf_model.pkl")
model = load(model_path)

st.title("Employee Attrition Prediction System")
st.write("Enter employee details below to predict attrition:")

# Input fields for features
age = st.slider("Age", 18, 60, 30)
monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=100000, value=5000, step=500)
job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
years_at_company = st.slider("Years at Company", 0, 40, 5)
overtime = st.selectbox("OverTime", ["No", "Yes"])
distance_from_home = st.slider("Distance From Home (km)", 1, 50, 10)
education = st.slider("Education (1-5)", 1, 5, 3)
environment_satisfaction = st.slider("Environment Satisfaction (1-4)", 1, 4, 3)
work_life_balance = st.slider("Work Life Balance (1-4)", 1, 4, 3)
num_companies_worked = st.slider("Number of Companies Worked", 0, 10, 2)

# Convert categorical 'OverTime' to numeric (same encoding as training)
overtime_encoded = 1 if overtime == "Yes" else 0

# Create dataframe for prediction
input_data = pd.DataFrame([[
    age, monthly_income, job_satisfaction, years_at_company,
    overtime_encoded, distance_from_home, education,
    environment_satisfaction, work_life_balance, num_companies_worked
]], columns=[
    "Age", "MonthlyIncome", "JobSatisfaction", "YearsAtCompany",
    "OverTime", "DistanceFromHome", "Education",
    "EnvironmentSatisfaction", "WorkLifeBalance", "NumCompaniesWorked"
])

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error(" This employee is likely to leave (Attrition = Yes).")
    else:
        st.success(" This employee is likely to stay (Attrition = No).")
