import streamlit as st

st.title("Welcome to BMI Calculator")

weight=st.number_input("Enter your weight(in kgs):")
height=st.radio("Select your height format:",('cms','meters','feet'))
