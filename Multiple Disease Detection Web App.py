# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 08:09:22 2023

@author: Windows 10 Pro
"""
import numpy as np
import pickle
import streamlit as st 
from streamlit_option_menu import option_menu

Diabetes_prediction = pickle.load(open('C:/Users\Windows 10 Pro/Desktop/python class/personal projects/trained_model.sav','rb'))
heart_prediction = pickle.load(open('C:/Users\Windows 10 Pro/Desktop/python class/personal projects/trained_heart_disease_model.sav','rb'))
parkinsons_prediction = pickle.load(open('C:/Users\Windows 10 Pro/Desktop/python class/personal projects/trained_parkinsons_disease_model.sav','rb'))

                                    
## Creating the side bar navigation 

with st.sidebar:
    selected = option_menu('Yara Jazairi Disease Detection Web App',
                           ['Diabetes detection',
                            'Heart disease detection',
                            'Parkinsons Disease detection'], icons=['activity','heart','person'],
                           default_index = 0)
    
# Building the diabetes interface 
if (selected=='Diabetes detection'):
    
    # page title
    st.title('Diabetes detection system')
    
    # get input from the user 
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    Pregnancies = st.text_input('No of pregnancies') 
    Glucose = st.text_input('Glucose level') 
    BloodPressure = st.text_input('Blood Pressure') 
    SkinThickness = st.text_input('Skin Thickness') 
    Insulin = st.text_input('Insulin level') 
    BMI = st.text_input('BMI level') 
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedegree level') 
    Age = st.text_input('Age') 
    
    # code for prediction 
    
    diagnosis = ' '
    
    # creating a prediction button 
    
    if st.button('Diabetes test result'):
        
        prediction_result = Diabetes_prediction.predict([[Pregnancies,Glucose,BloodPressure,
                                                      SkinThickness,Insulin,BMI,
                                                      DiabetesPedigreeFunction,Age]])
        if (prediction_result[0] == 1):
            diagnosis = 'The patient is Diabetic'
            
        else :
            diagnosis = 'The patient is not diabetic'
            
    st.success(diagnosis)


# Building the heart disease  interface 

if (selected == 'Heart disease detection'):
    
    # page title 
    st.title('Heart disease detection system')
    
    # Code for prediction 
    
    # taking input from the user 
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    Age = st.text_input(int('Enter Age'))
    sex = st.text_input(int('Enter Sex'))
    cp = st.text_input(int('Cp level'))
    trestbps = st.text_input(int('Enter Trestbps'))
    chol = st.text_input(int('Enetr Chol'))
    fbs = st.text_input(int('Enter Fbs'))
    restecg = st.text_input(int('Enter Restecg'))
    thalach = st.text_input(int('Enter Thalach'))
    exang = st.text_input(int('Enter Exang'))
    oldpeak = st.text_input(int('Enter oldpeak'))
    slope = st.text_input(int('Enter Slope'))
    ca = st.text_input(int('Enter ca'))
    thal = st.text_input(int('Enter Thal'))
    
    
    # CReating an empty sring to save the result 
    
    Diagnosis = ' '
    
    # Creating a prediction button 
    
    if st.button('Heart disease detection'):
        Result = heart_prediction.predict([[Age,sex,cp,trestbps,chol,
                                            fbs,restecg,thalach,exang,
                                            oldpeak,slope,ca,thal]])
        if (Result[0]==1):
            Diagnosis = 'The patient has heart disease'
        else:
            Diagnosis = 'The patient has no heart disease'
            
    st.success (Diagnosis)



# Building the parkoinsons disease interface 

if (selected == 'Parkinsons Disease detection'):
    
    # page title 
    st.title('Parkinsons Disease Detection')
    
    # Creating columns for the input 
    
    col1, col2, col3, col4 = st.columns(4)
    
    # Taking input from the user 
    with col1:
        MDVP_Fo = st.text_input('MDVP')
    with col2:
        MDVP_Fhi = st.text_input('MDVP-Fhi')
    with col3:
        MDVP_Flo = st.text_input('MDVP-Flo')
    with col4:
        MDVP_Jitter = st.text_input('MDVP-jitter')
    with col1:
        MDVP_Jitter = st.text_input('MDVP-jitt')
    with col2:
        MDVP_RAP = st.text_input('MDVP-RAP')
    with col3:
        MDVP_PPQ = st.text_input('MDVP-PPQ')
    with col4:
        Jitter_DDP = st.text_input('Jitter-DDP')
    with col1:
        MDVP_Shimmer = st.text_input('MDVP-Shimmer')
    with col2:
        MDVP_Shimmer = st.text_input('MDVP-shimm')
    with col3:
        Shimmer_APQ3 = st.text_input('Shimmer-APQ3')
    with col4:
        Shimmer_APQ5 = st.text_input('Shimmer-APQ5')
    with col1:
        MDVP_APQ = st.text_input('MDVP-APQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer-DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col4:
        HNR = st.text_input('HNR')
    with col1:
        RPDE = st.text_input('RPDE')
    with col2:
        DFA = st.text_input('DFA')
    with col3:
        spread1 = st.text_input('Spread-1')
    with col4:
        spread2 = st.text_input('Spread-2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
    
    # code for prediction 
    
    diagnosis = ' '
    
    # Prediction 
    
    if st.button('Parkinsons test result'):
    
        result = parkinsons_prediction.predict([[MDVP_Fo,MDVP_Fhi,MDVP_Flo,
                                                MDVP_Jitter,MDVP_Jitter,MDVP_RAP,
                                                MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,
                                                MDVP_Shimmer,Shimmer_APQ3,
                                                Shimmer_APQ5,
                                                MDVP_APQ,Shimmer_DDA,NHR,
                                                HNR,RPDE,DFA,spread1,
                                                spread2,D2,PPE]])
        if (result[0] == 1):
            diagnosis = 'The person has a parkinsons Disease'
        else:
            diagnosis = 'The person is healthy'
        
    st.success(diagnosis)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     

                                    

                                    
    