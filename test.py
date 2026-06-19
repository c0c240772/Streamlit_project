import streamlit as st

st.title("Hello, Streamlit!")

age = st.sidebar.slider("年齢",0,100,25)

st.write(f"{age}")