# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:52:03 2023

@author: navug
"""
import pickle 
import streamlit as st
import numpy as np
load_model=pickle.load(open(r"C:\Users\navug\Downloads\sleep_disorder.sav",'rb'))

def sleep_disorder_predict(input_data):
    input_data=np.asarray(input_data,dtype=float)
    input_data=input_data.reshape(1,-1)
    prediction=load_model.predict(input_data)
    
    if (prediction==0):
        return('The person doesnt have any sleep disorder')
    if (prediction==1):
        return('Sleep Apnea')
    else:
        return('Insomnia')
  
  
  
def change(Gender):
    if Gender=='male':
        return 0
    elif Gender=='female':
        return 1

def job(Occupation):
    
    if Occupation == 'Nurse':
        return 0
    elif Occupation == 'Doctor':
        return 1
    elif Occupation == 'Engineer':
        return 2
    elif Occupation == 'Lawyer':
        return 3
    elif Occupation == 'Teacher':
        return 4
    elif Occupation == 'Accountant':
        return 5
    elif Occupation == 'Salesperson':
        return 6
    elif Occupation == 'Software Engineer':
        return 7
    elif Occupation == 'Scientist':
        return 8
    elif Occupation == 'Sales Representative':
        return 9
    elif Occupation == 'Manager':
        return 10


def bmi(BMI_Category):
    
   if BMI_Category=='Normal':
       return 0
   elif BMI_Category=='Overweight':
       return 1
   elif BMI_Category=='Normal Weight':
       return 2
   elif BMI_Category=='Obese':
       return 3
      


def main():
    
    st.title('sleep disorder webpage')
    Gender = change(st.selectbox('Select the gender of the passenger', ['male','female']))
    
    Age=st.slider('select age of the patient')
    
    Occupation=job(st.selectbox('select Occupation of the patient', ['Nurse','Doctor','Engineer','Lawyer','Teacher','Accountant','Salesperson','Software Engineer','Scientist','Sales Representative','Manager']))
    Sleep_Duration=st.text_input(label='number of hours of sleep')
    Quality_of_Sleep=st.selectbox(label='Quality of Sleep', options=(0,1,2,3,4,5,6,7,8,9)) 
    Stress=st.text_input(label='stresslevel')
    BMI_Category=bmi(st.selectbox('BMI', ['Normal','Overweight','Normal Weight','Obese']))
    
    
    Result=''
    if st.button('Result'):
        Result=sleep_disorder_predict([Gender,Age,Occupation,Sleep_Duration,Quality_of_Sleep,Stress,BMI_Category])
    st.success(Result)
    
    
if__name__='__main__'
main()
        