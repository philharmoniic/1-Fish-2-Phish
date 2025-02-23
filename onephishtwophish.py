import streamlit as st
import pandas as pd
import numpy as np
import random
import requests as req
import google.generativeai as genai
import os

# os.environ["GOOGLE_API_KEY"] = st.secrets["key"]
# client = genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini
# response = model.generate_content('''You are a phishing scam email generator. Return an example phishing email from the Georgia Institute of Technology. 
# Don't make it obviously a phishing email, and don't put a 'note: this is a fake phishing email' at the end. 
# This is part of a website about differentiating phishing from non-phishing.''') #enter your prompt here!
# print(response.text) #dont forget to print your response!

st.title("One Phish, Two Phish")
# st.text(response.text)


def disable():
    st.session_state['disabled'] = True

with st.container():
    # data reading
    data = pd.read_csv("data/messages.csv")
    random_row = data.sample(n=1).iloc[0]
    
    if ('disabled' not in st.session_state):
        st.session_state['disabled'] = False
    
    if ('row' not in st.session_state):
        st.session_state['row'] = random_row

    random_email = st.session_state['row']['body']
    random_subject = st.session_state['row']['subject']
    random_phish = st.session_state['row']['label']

    # display text
    st.header(f"**{random_subject}**") # subject line
    st.write(random_email) # body of email

    # buttons
    phish = st.button(label="Phish!", icon="🐟", on_click=disable, disabled=st.session_state['disabled'])
    not_phish = st.button(label="Not Phish!", icon="🐈", on_click=disable, disabled=st.session_state['disabled'])


if (phish):
    if (random_phish == 1):
        st.write("Correct! You caught the phish!")
    else:
        st.write("Incorrect! That was not a phish.")

elif (not_phish): 
    if (random_phish == 0):
        st.write("Correct! That was not a phish.")
    else:
        st.write("Incorrect! You let the phish swim by.")

# Refresh button logic
def refresh():
    st.session_state['row'] = data.sample(n=1).iloc[0]
    st.session_state['disabled'] = False

refresh_button = st.button(label="Re-Phish", on_click=refresh)
