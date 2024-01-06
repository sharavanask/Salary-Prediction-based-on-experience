import streamlit as st
import joblib
lr_poly = joblib.load('lr_poly2.joblib')
def predict_salary(experience):
    predicted_salary = lr_poly.predict([[experience]])
    return predicted_salary[0]
st.title('Employee Salary Prediction')
experience = st.number_input('Enter years of experience', min_value=0.0, max_value=50.0, step=0.1)
if st.button('Predict Salary'):
    predicted_salary = predict_salary(experience)
    st.success(f"The predicted salary based on {experience} years of experience is {predicted_salary:.2f} .Rs")
