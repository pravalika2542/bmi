import streamlit as st
st.set_page_config(page_title='BMI')
st.title("Welcome to BMI Calculator")

weight=st.number_input("Enter your weight(in kgs):")
height=st.radio("Select your height format:",('cms','meters','feet'))
