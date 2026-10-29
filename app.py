import streamlit as st
import joblib
import numpy as np
import pandas as pd

try:
    scaler = joblib.load("scaler.pkl")
    model = joblib.load("model.pkl")
except:
    import pickle
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)


st.title("Churn Prediction App")
st.divider()
st.write("Please enter the values and hit the predict button for getting a prediction.")

st.divider()


credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
age = st.number_input("Enter Age", min_value=18, max_value=100, value=35)
tenure = st.number_input("Enter Tenure", min_value=0, max_value=10, value=3)
balance = st.number_input("Balance", min_value=0.0, value=75000.0)
products_number = st.selectbox("Product Number", [1,2,3,4])
credit_card = st.selectbox("Has Credit Card?", [0,1], format_func=lambda x: "Yes" if x==1 else "No")
active_member = st.selectbox("Is Active Member?", [0,1], format_func=lambda x: "Yes" if x==1 else "No")
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=100000.0)
country = st.selectbox("Country", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Female", "Male"])

# Feature order
feature_order = ['credit_score', 'age', 'tenure', 'balance', 'products_number',
                 'credit_card', 'active_member', 'estimated_salary', 'country_France',
                 'country_Germany', 'country_Spain', 'gender_Female', 'gender_Male']

if st.button("Predict"):
    input_data = {
        'credit_score': credit_score,
        'age': age,                   
        'tenure': tenure,               
        'balance': balance,             
        'products_number': products_number,      
        'credit_card':  credit_card,          
        'active_member': active_member,         
        'estimated_salary': estimated_salary,               
        'country_France': 1 if country == "France" else 0,       
        'country_Germany': 1 if country == "Germany" else 0,      
        'country_Spain': 1 if country == "Spain" else 0,        
        'gender_Female': 1 if gender == "Female" else 0,        
        'gender_Male': 1 if gender == "Male" else 0
    }

    data = pd.DataFrame([input_data])
    data = data[feature_order]

    # Scale and predit
    scaled = scaler.transform(data)
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1]

    st.divider()
    st.metric("Churn Probability", f"{prob*100:.2f}%")

    if pred == 1:
        st.error(f"Customer will CHURN - {prob*100:.1f}% risk")
    else:
        st.success(f"Customer will NOT churn - {prob*100:.1f}% risk")
