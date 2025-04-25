import streamlit as st
num1 = st.number_input("Enter num1 value",min_value=0,step=1)
num2 = st.number_input("Enter num2 value",min_value=0,step=1)
if st.button("Add"):
    if num1 and num2 >0:
        st.write('Total : ',num1+num2)
        st.success("Successfully calculated")
    else:
        st.error("Invalid")
