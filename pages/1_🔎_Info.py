import streamlit as st
import pandas as pd

with st.sidebar:
  st.image("static/logo.png", width=None)

st.title("Info")

st.header("About the Project", divider=True)

st.subheader("Description")
st.write('''
        ***1 Fish, 2 Phish*** is a web-game similar to games like [The Higher Lower Game](https://www.higherlowergame.com),
         but for Phishing emails!

        You are given a sample email, sampled from [this dataset](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset/data?select=SpamAssasin.csv),
        and users are tasked with determining whether or not the message is a real email or a phishing scam.

        After guessing, Google Gemini creates a response either explaining why it is phishing and what to 
        look out for, or what signifies that the email is a real, legitemate email.
        
        **Note:** Every email is processed through Google Gemini and re-formatted to be more realistic. 
        ''')

st.subheader("Inspiration")
st.write('''
        As college students, we get a shockingly high amount of phishing emails.
         
        Usually, the signs are easy to spot - Misspelled headings, unknown senders, terrible grammar, etc.
        But with the recent growth of large language models (LLMs), it's easier than ever before to be fooled by a 
        phishing email. 
         
        Gone are the days of phishing emails exclusively fooling your grandparents - ***1 Fish, 2 Phish*** 
        both exemplifies how realistic phishing emails can be in the modern day, 
        and provides AI-powered explanations of how to spot difficult phishing emails from afar.
        ''')

st.subheader("Citations")

st.write('''
        __Dataset__:
         
        Naser Abdullah Alam. (2024). Phishing Email Dataset [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DS/5074342
        ''')
