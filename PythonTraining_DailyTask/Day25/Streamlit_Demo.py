import streamlit as st

username = st.text_input("Username")
st.write("The current username is", username)

password = st.text_input("Password", type="password")

st.button("Login", type="primary")
#st.write("Login successful",)