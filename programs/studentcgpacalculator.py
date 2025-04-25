import streamlit as st

st.title(" Student CGPA Calculator")
st.header(" Student Login")

student_name = st.text_input("Enter your Name:")
student_rollnumber = st.text_input("Enter your Roll Number:")
branch = st.selectbox("Select your Branch", ["CSE", "AIML", "IT"])

 
if branch == "CSE":
    subjects = ["DAA", "BEFA", "DBMS", "DM"]
elif branch == "AIML":
    subjects = ["DA", "IRS", "KRR", "NLP"]
elif branch == "IT":
    subjects = ["IAI", "OS", "AECL", "PYTHON"]


if student_name and student_rollnumber:
    st.success(f"Welcome {student_name} from {branch} branch (Roll No: {student_rollnumber})")

    st.subheader(" Enter Your Marks")

    total_points = 0
    total_subjects = 0

    for subject in subjects:
        marks = st.number_input(f"Enter marks for {subject} (out of 100):", min_value=0, max_value=100, step=1, key=subject)

        
        if marks >= 90:
            grade_point = 10
        elif marks >= 80:
            grade_point = 9
        elif marks >= 70:
            grade_point = 8
        elif marks >= 60:
            grade_point = 7
        elif marks >= 50:
            grade_point = 6
        elif marks >= 40:
            grade_point = 5
        else:
            grade_point = 0

        total_points += grade_point
        total_subjects += 1

    if total_subjects > 0:
        cgpa = total_points / total_subjects
        st.success(f" Your CGPA is: *{cgpa:.2f}*")
