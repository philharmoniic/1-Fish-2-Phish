import streamlit as st
import Nathan_info as M
import Phil_info as P

with st.sidebar:
  st.image("static/logo.png", width=None)
  
st.title("Credits")
st.header("Who worked on ***1 Fish, 2 Phish***?", divider=True)

st.subheader("Nathan Wilson")
st.image(M.profile_picture, width=200)
st.write(f"**About Me:** {M.about_me}\n")
st.write(f"**My Contributions:** {M.contributions.strip()}\n")
st.write(f"You can find my **GitHub** at [NathanNWCW]({M.my_github_url.strip()})!")

st.subheader("Phillip Abraham")
st.image(P.profile_picture, width=200)
st.write(f"**About Me:** {P.about_me}\n")
st.write(f"**My Contributions:** {P.contributions.strip()}\n")
st.write(f"You can find my **GitHub** at [philharmoniic]({P.my_github_url.strip()})!")

