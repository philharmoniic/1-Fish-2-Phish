import streamlit as st
import pandas as pd
import numpy as np
import random
import requests as req
import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyC4xfkOAnvagK_2j4L6YVZDJPouGS8JXlI"
client = genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini

st.markdown(
    """
    <link rel="stylesheet" type="text/css" href="style.css">
    """,
    unsafe_allow_html=True
)

st.title("One Fish, Two Phish: The Game About Fishy Emails")
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
    random_sender = st.session_state['row']['sender']
    random_phish = st.session_state['row']['label']

    # display text
    st.header(f"**{random_subject}**", divider=True) # subject line
    st.caption(f"From: {random_sender}") # sender
    st.write(random_email) # body of email

    # buttons
    phish = st.button(label="Phish!", icon="🐟", on_click=disable, disabled=st.session_state['disabled'])
    not_phish = st.button(label="Not Phish!", icon="🐈", on_click=disable, disabled=st.session_state['disabled'])

prompt = f'''
You are an AI model being used in a phishing detection web-game. Please explain why the following 
set of data is phishing (if it has a label of 1) or not phishing (if it has a label 0): {st.session_state['row']}.
Try to write it like a normal person explaining what about it indicates that it is or is not phishing.
Also, don't include the label, as users cannot see that. Don't indicate that this is using a dataset. Don't include
the provided URL counter; only count them yourself if you want to point out the number of URLs.
Try to sound as natural as possible. Please start sentences with something other than "okay." Try to be kind
and caring to users, explaining it in a way that anyone could understand.
'''

response = model.generate_content(prompt)

if (phish):
    if (random_phish == 1):
        st.subheader("Correct! You caught the phish!")
    else:
        st.subheader("Incorrect! That was not a phish.")
    st.write(response.text.replace('`', ''))
elif (not_phish): 
    if (random_phish == 0):
        st.subheader("Correct! That was not a phish.")
    else:
        st.subheader("Incorrect! You let the phish swim by.")
    st.write(response.text.replace('`', ''))

print(response.text)

# Refresh button logic
def refresh():
    st.session_state['row'] = data.sample(n=1).iloc[0]
    st.session_state['disabled'] = False

refresh_button = st.button(label="Re-Phish", on_click=refresh)
