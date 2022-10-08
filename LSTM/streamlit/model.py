import streamlit as st
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import folium
from folium.plugins import Draw
from streamlit_folium import st_folium 
import streamlit.components.v1 as components
import plotly.express as px
from random import randint

if 'key' not in st.session_state:
    st.session_state.key = [0,0,0,0]

st.write(st.session_state.key[0])
    

scaler = MinMaxScaler()
html_temp="""
   <div style ="background-color:yellow;padding:20px"> 
    <h1 style ="color:black;text-align:center;">Traffic Profiling</h1>
    </div>          
"""
st.markdown(html_temp,unsafe_allow_html=True)
# loading the model
model = keras.models.load_model("trafficpredictor")
st.header("This LSTM node is trained for Velachery-Guru Nanak road.")
st.header("The model takes number of vehicles in current junction as input and output of the model will predict number of vehicle in upcoming next junction")

@st.cache
def load_data_scaler():
    data = pd.read_csv("allphases.csv",index_col="Time")
    data = data[data.columns[[5,11,17]]]
    scaler.fit_transform(data)

load_data_scaler()

def prediction(Vehicle):
    # transformed = scaler.fit_transform([[Vehicle]])
    # print(transformed)
    trans_veh = (Vehicle-992)/(1271-992)
    predict = model.predict([[trans_veh]])
    tran_predict = (predict*999+(1271-900))
    # print(tran_predict)
    return int(tran_predict)
# result=0
# result1=0
# result2=0
# result3=0
count = st.number_input("Vehicle Count Input")
if st.button("Predict"):
    result = prediction(count)
    result1 = prediction(result)
    result2 = prediction(result1)
    result3 = prediction(result2)
    st.session_state.key[0] = result
    st.session_state.key[1] = result1
    st.session_state.key[2] = result2 + randint(2,4)
    st.session_state.key[3] = result3
    print("original result " + str(st.session_state.key[0]) +" " + str(result1)+" " +str(result2)+" "+str(result3))
    # for i in range(0,4):
    #     result = prediction(result)
    #     st.session_state.key[i]=result
    #     print(result)
st.write("The traffic count in next junction is "+ str(prediction(count)))
a = folium.Map(location=[12.9563899,80.2430274],zoom_start=15)
# str(st.session_state.key[0])
folium.Marker(
    [12.9563899,80.2430274],tooltip=count,
).add_to(a)
# del st.session_state["key"]
folium.Marker(
    [12.980805,80.2529179], popup="<b>Second junction</b>", tooltip=st.session_state.key[0]
).add_to(a)
folium.Marker(
    [12.9844636,80.2522668], popup="<b>Secornd junction</b>", tooltip=st.session_state.key[1]
).add_to(a)
folium.Marker(
    [12.9880637,80.2513648], popup="<b>Second junction</b>", tooltip=st.session_state.key[2]
).add_to(a)
Draw(export=False).add_to(a)

output= st_folium(a,width=800,height=300)
st.write(output)
chart_data = {"TIME":["1st junction","2nd junction","3rd junction","4th junction"],"Count":st.session_state.key}
chart_data = pd.DataFrame(chart_data)
fig = px.line(chart_data,x="TIME",y="Count")
print(chart_data)
# chart_data = st.session_state.key
st.plotly_chart(fig)



