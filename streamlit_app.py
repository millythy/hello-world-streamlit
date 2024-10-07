import streamlit as st

st.title("hello world streamlit")
name = st.text_input("masukkan nama")
if (name):
    st.write("hello, nama saya : ", name)
else:
    st.write("hello, nama saya: ", name)