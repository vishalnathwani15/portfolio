import streamlit as st

st.title("Contact me")

with st.form(key="my_forms"):
    user_email =st.text_input(" your email address:")
    message = st.text_area("Your message:")
    button = st.form_submit_button("submit")
    if button:
        print("submited")