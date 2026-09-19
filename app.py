import streamlit as st 

st.title("App")
a = st.number_input("Enter a number: ")
b = st.number_input("Enter another number: ")

sum = int(a) + int(b)
st.write("The sum of", a, "and", b, "is:", sum)