import streamlit as st
import pandas as pd
import numpy as np
import pickle  #to load a saved model
import base64  #to open .gif files in streamlit app

st.write("Hello,This is my work on usa_county_wise Covid_19 Dataset") 
st.title("PUD3106 ASSIGNMENT")
st.header("DATA VISUALISATION")
st.markdown("COUNTRY DATASET AVAILABLE ON KAGGLE")
st.code("2021/2022")

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value



st.title('Covid:')
st.image("COVID.png")
st.markdown('Dataset :')
data=pd.read_csv("day_wise.csv.xls")

dt1 = data.drop(["Date"], axis=1)
import sklearn
sc = preprocessing.StandardScaler()
sc.fit(dt1)
dtt = sc.transform(dt1)
dt1 = pd.DataFrame(dtt, columns=dt.columns)
d = pd.concat([data["Date"], dt1], axis=1)
st.write(data.head())
st.markdown("General Bar Chart for standardized data of various Attributes")
st.bar_chart(dt1)
import matplotlib.pyplot as plt

agree= st.button("click to see Histogram")
if agree:
    st.markdown("General Histogram for standardized data of various Attributes")
    fig, ax = plt.subplots()
    ax.hist(dt1, bins=15)
    st.pyplot(fig)

agree= st.button("click to see Area chart")
if agree:
    st.markdown("General Area Chart for standardized data of various Attributes")
    st.area_chart(dt1)

agree= st.button("click to see line chart")
if agree:
    st.markdown("General Line Chart for standardized data Chart of various Attributes")
    st.line_chart(dt1)
    


