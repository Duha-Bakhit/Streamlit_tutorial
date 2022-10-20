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
st.image("https://www.google.com/search?q=covid19&rlz=1C1GCEA_enKE1027KE1028&sxsrf=ALiCzsYUEqV-6vJf0Q4rFmKpD7HGYUw-Gg:1666264164367&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi5rfnc1e76AhUHgv0HHa-ZDnsQ_AUoAnoECAEQBA&biw=1280&bih=601&dpr=1.5#imgrc=btJiBBcxjOuWDM")
st.markdown('Dataset :')
data=pd.read_csv("day_wise.csv.xls")


dt = data.drop(["Date"], axis=1)
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(dt)
dtt = sc.transform(dt)
dt = pd.DataFrame(dtt, columns=dt.columns)
d = pd.concat([data["Date"], dt], axis=1)
st.write(data.head())
st.markdown("General Bar Chart for standardized data of various Attributes")
st.bar_chart(dt)
import matplotlib.pyplot as plt

agree= st.button("click to see Histogram")
if agree:
    st.markdown("General Histogram for standardized data of various Attributes")
    fig, ax = plt.subplots()
    ax.hist(dt, bins=15)
    st.pyplot(fig)

agree= st.button("click to see Area chart")
if agree:
    st.markdown("General Area Chart for standardized data of various Attributes")
    st.area_chart(dt)

agree= st.button("click to see line chart")
if agree:
    st.markdown("General Line Chart for standardized data Chart of various Attributes")
    st.line_chart(dt)
    
agree= st.button("click to see maps chart")
if agree:
    st.markdown("General maps Chart for standardized data Chart of various Attributes")
    st.map(dt)


