import pandas as pd 
import streamlit as st
from joblib import load
import numpy as np

st.set_page_config(layout="wide")
# Load the dataset
df = pd.read_csv("C:/Users/DELL/Downloads/DataSets/diabetes_prediction_dataset.csv")

#st.title(' :black[Diabetes Checking App]')
st.markdown(
    "<h1 style='text-align: center; color: blue;'>&#x1F489 Diabetes Prediction Web App </h1>",
    unsafe_allow_html=True)

st.header(' :white[Fill the below details to find diabetes]')

st.markdown(f""" <style>.stApp {{
                    background: url('https://t3.ftcdn.net/jpg/02/39/68/72/240_F_239687219_PLbiqAuTtNEneUlAZscznUPwXmS7BqxR.jpg');   
                    background-size: cover}}
                 </style> """,unsafe_allow_html=True)

# Create an empty DataFrame to store user inputs
user_data = pd.DataFrame(columns=['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level'])

with st.form('Regression'):
    col1,col2= st.columns(2)
    with col1:
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            gender = st.selectbox('Select Gender', ('Male', 'Female',"Other"))
            age = st.number_input('Select Age', min_value=0, max_value=150, value=25)  # Number input
            hypertension = st.selectbox('You have Hypertension?', ('Yes', 'No'))
            heart_disease = st.selectbox('You have Heart Disease?', ('Yes', 'No'))
            button = st.form_submit_button(label='SUBMIT')
        with sub_col2:
            bmi = st.number_input('Select Your BMI value', min_value=10.0, max_value=70.0, value=25.0, step=0.1)  # BMI range
            HBA1c_Level = st.number_input('Select HBA1C Level',min_value=0.0, max_value=20.0, value=5.0, step=0.1)  # HbA1c level range
            blood_glucose_level = st.number_input('Select Blood glucose Level', min_value=0.0, max_value=500.0, value=100.0, step=1.0)  # Blood glucose level range
            smoking_history = st.selectbox('Select Your Smoking History', ('Never Smoked', 'No info', 'Currently Smoke','former','Ever Smoked', 'Not currently'))
            
col1,col2 = st.columns([0.65,0.35])
with col2:
    st.caption(body='*Min and Max values are reference only')
    


if button:
    # Convert quantity to string       
    file_path = 'diabetes.pkl'  # Adjust the file path as per your saved model

    # Load the saved model
    loaded_model = load(file_path)
    # Map smoking history to numerical value using a dictionary
    smoking_mapping = {'Never Smoked':0, 'No Info':1, 'Currently Smoke':2 ,'former':3, 'Ever Smoked':4, 'Not current':5}

    smoking_val = smoking_mapping.get(smoking_history)

    # Convert categorical variables to numerical values
    gender_val = 0 if gender == 'Female' else 1 if gender == 'Male' else 2
    hypertension_val = 1 if hypertension == 'Yes' else 0
    heart_disease_val = 1 if heart_disease == 'Yes' else 0

    # Make predictions
    y_pred = loaded_model.predict(np.array([[gender_val, age, hypertension_val, heart_disease_val, smoking_val,
                bmi, HBA1c_Level, blood_glucose_level]]))
    

    if y_pred == 1:
        st.markdown("<h2 style='color: red;'>Positive Results: You may have diabetes</h2>", unsafe_allow_html=True)
        st.write('Based on the information provided, it is possible that you have diabetes.') 
        st.write('Here are some suggestions to help manage your health:')
        st.write('1. Control your diet by limiting sugar and carbohydrates.')
        st.write('2. Exercise regularly to manage blood sugar levels.')
        st.write('3. Monitor blood sugar levels consistently and take prescribed medication as directed by your healthcare provider.')
    else:
        st.markdown("<h2 style='color: green;'>Negative Results: You likely do not have diabetes</h2>", unsafe_allow_html=True)
        st.write('Based on the information provided, it is unlikely that you have diabetes.')
        st.write('Keep up with your healthy lifestyle choices to maintain your well-being.')
