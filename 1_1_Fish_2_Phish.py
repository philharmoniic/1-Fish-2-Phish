import streamlit as st
import pandas as pd
import numpy as np
import random
import requests as req
import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = st.secrets['key']
client = genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini

# logo on sidebar

with st.sidebar:
  st.image("static/logo.png", width=None)

st.title("1 Fish, 2 Phish 🎣 \n A Game About Fishy Emails")
# st.text(response.text)

def disable():
    st.session_state['disabled'] = True

if ('rand_int' not in st.session_state):
    st.session_state['rand_int'] = random.randint(0,1)

if ('score' not in st.session_state):
    st.session_state['score'] = 0

if ('hi_score' not in st.session_state):
    st.session_state['hi_score'] = st.session_state['score'] 

st.write(f"**High Score:** {st.session_state['hi_score']}")
st.write(f"**Correct Answer Streak:** {st.session_state['score']}")

try:
    with st.container():
        # data reading
        data = ""
        if (st.session_state['rand_int'] == 1):
            data = pd.read_csv("data/messages.csv")
        else:
            data = pd.read_csv("data/non-phishing.csv")
        random_row = data.sample(n=1).iloc[0]
        
        if ('disabled' not in st.session_state):
            st.session_state['disabled'] = False
        
        if ('row' not in st.session_state):
            st.session_state['row'] = random_row


        random_email = st.session_state['row']['body'].replace('`','*')
        random_subject = st.session_state['row']['subject']
        # random_sender = st.session_state['row']['sender']
        random_phish = st.session_state['row']['label']

        reformat_prompt = f'''
        Your job is to reformat the following email, "{random_email}".
        When reformatting, fix any grammar mistakes, paragraph formatting, and errors without deviating
        too much from the structure of the original email. Do nothing other than reformat the email.

        Change the dates to be after 2020. Replace any instance of Enron with a different company name
        [like Google, Amazon, Microsoft, Sony, Georgia Power, etc.]. Replace any and all links to outside
        sources with [https://1fish-2phish.streamlit.app] so that, in case someone clicks it, it links them
        back to our site.
        '''
        if ('body' not in st.session_state or st.session_state['body'] == st.session_state['row']['body']):
            reformatted_email = model.generate_content(reformat_prompt)
            st.session_state['body'] = reformatted_email.text

        # display text
        st.header(f"**{random_subject}**", divider=True) # subject line
        # st.caption(f"From: {random_sender}") # sender
        st.write(st.session_state['body']) # body of email

        # buttons
        phish = st.button(label="Phish!", icon="🐟", on_click=disable, disabled=st.session_state['disabled'])
        not_phish = st.button(label="Not Phish!", icon="🐈", on_click=disable, disabled=st.session_state['disabled'])

    prompt = f'''
    You are an AI model being used in a phishing detection web-game. Please explain why the following 
    set of data is phishing (if it has a label of 1) or not phishing (if it has a label 0): Subject: {st.session_state['row']['subject']}, Body: {st.session_state['body']}.

    The phishing/not phishing value is: {random_phish}
    
    Try to write it like a normal person explaining what about it indicates that it is or is not phishing.
    Also, don't include the label, as users cannot see that. Don't indicate that this is using a dataset. Don't include
    the provided URL counter; only count them yourself if you want to point out the number of URLs.
    Try to sound as natural as possible. Please start sentences with something other than "okay." Try to be kind
    and caring to users, explaining it in a way that anyone could understand.
    If the email is not a phishing email, don't talk about it being suspicious, focus more on what makes it obviously not
    a phishing scam.
    '''

    response = model.generate_content(prompt)


    if (phish):
        if (random_phish == 1):
            st.subheader("Correct! You caught the phish!")
            st.session_state['score'] += 1
        else:
            st.subheader("Incorrect! That was not a phish.")
            st.session_state['score'] = 0
        st.write(response.text.replace('`', '*'))
    elif (not_phish): 
        if (random_phish == 0):
            st.subheader("Correct! That was not a phish.")
            st.session_state['score'] += 1
        else:
            st.subheader("Incorrect! You let the phish swim by.")
            st.session_state['score'] = 0
        st.write(response.text.replace('`', '*'))

    print(response.text)

    # Refresh button logic

except:
    st.subheader('''
    Too many requests! The lake's gone dry!
    Please wait ~1 minute before trying again!
    ''')

def refresh():
    st.session_state['row'] = data.sample(n=1).iloc[0]
    st.session_state['body'] = st.session_state['row']['body']
    st.session_state['disabled'] = False
    st.session_state['rand_int'] = random.randint(0,2)
    if (st.session_state['score'] > st.session_state['hi_score']):
        st.session_state['hi_score'] = st.session_state['score']
refresh_button = st.button(icon="🔄", label="Re-Phish", on_click=refresh)
