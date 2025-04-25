import streamlit as st
st.title("Thi is sample Program")
num1=st.number_input("Enter num1",min_value=1,step=1)
num2=st.number_input("Enter num2",min_value=1,step=2)
st.write("Total: ",num1*num2)
