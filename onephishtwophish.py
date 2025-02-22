import streamlit as st
import pandas as pd
import numpy as np
import random
import requests as req
import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = st.secrets["key"]
client = genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini
response = model.generate_content('''You are a phishing scam email generator. Return an example phishing email from the Georgia Institute of Technology. 
Don't make it obviously a phishing email, and don't put a 'note: this is a fake phishing email' at the end. 
This is part of a website about differentiating phishing from non-phishing.''') #enter your prompt here!
print(response.text) #dont forget to print your response!

st.title("One Phish Two Phish")
st.text(response.text)
