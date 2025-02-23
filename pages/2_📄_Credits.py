import streamlit as st
import Nathan_info as M
import Phil_info as P

st.title("Credits")
st.header("Who worked on ***1 Fish, 2 Phish***?", divider=True)

st.subheader("Nathan Wilson")
st.image(M.profile_picture, width=200)
st.write(f"About Me: {M.about_me}\n")
st.write(f"My Contributions: {M.contributions.strip()}\n")
st.write(f"You can find my GitHub at [NathanNWCW]({M.my_github_url.strip()})!")
