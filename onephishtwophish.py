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

st.title("One Phish, Two Phish: The Game About Fishy Emails")
# st.text(response.text)

# data reading
data = pd.read_csv("data/messages.csv")
random_row = data.sample(n=1).iloc[0]
random_email = random_row['body']
random_subject = random_row['subject']
random_sender = random_row['sender']
random_phish = random_row['label'] # 1 for phishing, 0 for not phishing

# display logo

# display text
st.header(f"**{random_subject}**", divider=True) # subject line
st.caption(f"From: {random_sender}") # sender
st.write(random_email) # body of email

# buttons
phish = st.button(label="Phish!", icon="🐟")
not_phish = st.button(label="Not Phish!", icon="🐈")

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