import streamlit as st
import pickle
import spacy
import numpy as np
import string  # Import the string module
import pandas as pd


st.set_page_config(layout="wide")
col1,col2 = st.columns([0.55,0.45])
with col2:
    st.markdown(f""" <style>.stApp {{
                        background: url('https://cdn.create.vista.com/api/media/medium/466293910/stock-photo-businessman-hand-holding-mail-icon-contact-newsletter-email-protect-your?token=');   
                        background-size: cover}}
                    </style> """,unsafe_allow_html=True)
# Load the SVM model
with open('rf_model1.pkl', 'rb') as file:
    svc_model = pickle.load(file)

# Load the Spacy NLP model
nlp = spacy.load('spacy_model')

# Function to vectorize the input message
def vectorize_message(message):
    doc = nlp(message)
    return doc.vector

with col1:
    # Streamlit app
    st.title(" :blue[SPAM DETECTION APPLICATION]")
    st.write(" :green[Enter a message to check if it is spam or ham:]")

    input_message = st.text_area("Enter your Message")

    if st.button("Predict"):
        if input_message:
            vectorized_message = vectorize_message(input_message).reshape(1, -1)
            length = len(input_message)
            punct = sum([1 for char in input_message if char in string.punctuation])
            input_features = np.hstack([vectorized_message, [[length, punct]]])
            prediction = svc_model.predict(input_features)
            result = "Ham" if prediction[0] == "ham" else "Ham"
            st.write(f"The message is: **{result}**")
        else:
            st.write("Please enter a message.")
