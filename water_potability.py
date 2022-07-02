# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:49:48 2022

@author: ACER
"""
from pickle import dump
import pickle
import pandas as pd
import streamlit as st
from lightgbm import LGBMClassifier
import matplotlib.image as mp


st.title('**WATER POTABILITY**')

image = mp.imread("water.jpg")
st.image(image)
st.write("""
         water is drinkable or not detecting using mechinelearning
         In this implimentation various **mechine learning** algorithms for building a **classification model** to **
         """
         )

st.sidebar.header('Enter input')

def user_input_features():
    ph_value=st.sidebar.number_input('ph',0,14)
    hardness=st.sidebar.number_input('hardness',0,500)
    solids=st.sidebar.number_input('solids',0,50000)
    chloramines=st.sidebar.number_input('chloramines',0,20)
    sulfate=st.sidebar.number_input('sulfate',0,500)
    conductivity=st.sidebar.number_input('conductivity',0,1000)
    organic_carbo=st.sidebar.number_input('organic_carbo',0,30)
    trihalomethane=st.sidebar.number_input('trihalomethane',0,200)
    turbidity=st.sidebar.number_input('turbidity',0,10)
    data={'ph_value':ph_value,
          'hardness':hardness,
          'solids':solids,
          'chloramines':chloramines,
          'sulfate':sulfate,
          'conductivity':conductivity,
          'organic_carbo':organic_carbo,
          'trihalomethane':trihalomethane,
          'turbidity':turbidity}
    features = pd.DataFrame(data,index = [0])
    return features
df=user_input_features()
st.subheader('user input value')
st.write(df)


model = pickle.load(open('water_potability_pickle.pickle','rb'))
prediction=model.predict(df)



st.subheader("Result=")
#output=pd.DataFrame({'Result':prediction})
st.write("yes" if prediction == 1 else "no")


    