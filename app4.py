# -*- coding: utf-8 -*-
"""
Created on Thu May 11 09:02:52 2023

@author: debna
"""

import streamlit as st
import numpy as np
import pickle
from pickle import load
from sklearn.linear_model import LogisticRegression

lr = load(open('E:/LiveProject/Job Placement/job_placement_lr.pickle', 'rb'))

st.title("Job Placement Predictors")

gender = st.radio("Select Your Gender", ["M", "F"])
if gender == "Male":
    gender = 1
else:
    gender = 0

ssc_percentage = st.number_input('ssc_percentage', value=0.0)

ssc_board = st.radio("Select Your ssc_board", ["Central", "Others"])
if ssc_board == "Central":
    ssc_board = 1
else:
    ssc_board = 2

hsc_percentage = st.number_input('hsc_percentage', value=0.0)

hsc_board = st.radio("Select Your hsc_board", ["Central", "Others"])
if hsc_board == "Central":
    hsc_board = 1
else:
    hsc_board = 2

hsc_subject = st.radio("Select Your hsc_subject", ["Commerce", "Science", "Arts"])
if hsc_subject == "Commerce":
    hsc_subject = 1
elif hsc_subject == "Science":
    hsc_subject = 2
elif hsc_subject == "Arts":
    hsc_subject = 3
    
degree_percentage = st.number_input('degree_percentage', value=0.0)

undergrad_degree = st.radio("Select Your undergrad_degree", ["Comm&Mgmt", "Sci&Tech", "Others"])
if undergrad_degree == "Comm&Mgmt":
    undergrad_degree = 1
elif undergrad_degree == "Sci&Tech":
    undergrad_degree = 2
elif undergrad_degree == "Others":
    undergrad_degree = 3

work_experience = st.radio("Select Your work_experience", ["No", "Yes"])
if work_experience == "No":
    work_experience = 1
else:
    work_experience = 2

emp_test_percentage = st.number_input('emp_test_percentage', value=0.0)

specialisation = st.radio("Select Your specialisation", ["Mkt&Fin", "Mkt&HR"])
if specialisation == "Mkt&Fin":
    specialisation = 1
else:
    specialisation = 2

mba_percent = st.number_input('mba_percent', value=0.0)


if st. button("Predict"):
    query_point = np. array([gender,ssc_percentage,ssc_board,hsc_percentage,hsc_board,hsc_subject,degree_percentage,undergrad_degree,work_experience,emp_test_percentage,specialisation,mba_percent])
    query_point = query_point. reshape(1, -1)
    prediction = lr.predict(query_point)
    if prediction == 1:
        st.success("The person will placed 😊!")
    else:
        st.error("The person will not placed 😥!")



#!streamlit run app.py & npx localtunnel --port 8501  



















































