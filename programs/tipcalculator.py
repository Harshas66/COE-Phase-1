import streamlit as st

st.title("Tip Calculator")

bill = st.number_input("Enter your Bill Amount", min_value=0)


if bill < 1000:
    tip_percentage = 2
elif 1000 <= bill <= 5000:
    tip_percentage = 5
else:
    tip_percentage = 7

tip_amount = (tip_percentage / 100) * bill


st.write("Bill Amount: ", bill)
st.write("Tip percentage: ", tip_percentage)
st.write("Tip Amount: ", tip_amount)


if st.button("Add"):
    total_amount = bill + tip_amount
    st.write("Total Amount: ", total_amount)
