import streamlit as st
import pandas as pd
import plotly.express as px


st.title("DATA VISUALISATION ASSIGNMENT")
st.header("Coronavirus disease (COVID-19) APP")
st.subheader("DAY WISE DATASET AVAILABLE ON KAGGLE")
st.write("Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus. Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment. However, some will become seriously ill and require medical attention.") 
st.write("The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe. These particles range from larger respiratory droplets to smaller aerosols. You can be infected by breathing in the virus if you are near someone who has COVID-19, or by touching a contaminated surface and then your eyes, nose or mouth. The virus spreads more easily indoors and in crowded settings.")


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



st.image("COVID.png")
st.markdown('Dataset :')
data=pd.read_csv("day_wise.csv.xls")
numeric_columns = list(data.select_dtypes(['float', 'int']).columns)
non_numeric_columns = list(data.select_dtypes(['object']).columns)
non_numeric_columns.append(None)
print(non_numeric_columns)

dt = data.drop(["Date"], axis=1)
st.write(data.head())


Chart_Taype=st.selectbox('Choose the Chart Type',('line chart','Boxplot','Histogram','Bar Chart'))

if Chart_Taype=='line chart':
    st.markdown(" Line Chart for  data Chart of various Attributes")
    st.line_chart(dt)
    

elif Chart_Taype=='Area Chart':
    st.markdown(" Bar Chart for data of various Attributes")
    st.bar_chart(dt)
    
elif Chart_Taype=='Bar Chart':
    st.markdown("Bar Chart for data of various Attributes")
    st.bar_chart(dt)
    
elif Chart_Taype=='Boxplot':
    plot = px.box(data_frame=dt)
    st.plotly_chart(plot)
    
elif Chart_Taype=='Histogram':
    st.sidebar.subheader("Histogram Settings")
    st.markdown('Histogram')
    x = st.sidebar.selectbox('Feature', options=numeric_columns)
    bin_size = st.sidebar.slider("Number of Bins", min_value=10, max_value=100, value=40)
    color_value = st.sidebar.selectbox("Colored", options=non_numeric_columns)
    plot = px.histogram(x=x, data_frame=data, color=color_value)
    st.plotly_chart(plot)

st.header("Thank You For Visiting")
st.write("Duha Bakhit")

         
         
