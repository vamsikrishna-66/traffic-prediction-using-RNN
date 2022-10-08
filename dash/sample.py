from ctypes import alignment
from multiprocessing.sharedctypes import Value
from click import style
import plotly.express as px
import pandas as pd
import ipywidgets as widgets
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import dash
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler as scaler
import plotly.express as px
from skimage import io
import base64


app = Dash(__name__)

df = pd.read_csv("day1.csv")
# model = keras.models.load_model("trafficpredictor")

# def load_data_scaler():
#     data = pd.read_csv("allphases.csv",index_col="Time")
#     data1 = data[data.columns[[5,11,17]]]
#     scaler.fit_transform(data1)

# load_data_scaler()
image_filename = "C:/Users/Vamsi/Desktop/Geospatial-and-Transportation-Engineering/dashboard/assets/my-image.png"
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')

# test_png = 'download.png'
# test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')


app.layout=html.Div([
    html.Div(
    id="one",
    children="DASHBOARD for VALECHERRY",
    style={
        'textAlign' : 'center',
        'font-size' : '40px',
        'color' : '#ffffff',
        'background' : '#000000',
        'margin-bottom' : '10px'
        
    }
    ),
    html.Div([
    
    
    html.Div(
    dcc.Dropdown(
        id="ticker",
        options=[{"label": x, "value": x} 
                 for x in df.columns[1:]],
        value=df.columns[1],
        clearable=False,
    ),
    

    style = {
        'color' : '#0000ff',
        'background' : '#fff000',
        'padding': '10px',
        'width' : '20%',
        'margin-top' : '0px',
        'margin-left' : '40px',
        'margin-right' : '10px',

    }
),


html.Div(
     dcc.Dropdown(['MON', 'TUE', 'WED' , 'THU', 'FRI','SAT'],'MON', id='demo-dropdown',multi=True),
     style = {
        'color' : '#0000ff',
        'background' : '#fff000',
        'padding': '10px',
        'width' : '20%',
        'margin-top' : '40px',
        'margin-left' : '40px',
        'margin-right' : '10px',
     }
    
),


# html.Div(
# dbc.DropdownMenu(
# label="Menu",
# children=[
#     dbc.DropdownMenu(
#     children=[
#         dbc.DropdownMenuItem("Item 1"),
#         dbc.DropdownMenuItem("Item 2"),
#     ],
#     ),
#     dbc.DropdownMenuItem("Item 2"),
#     dbc.DropdownMenuItem("Item 3"),
# ],
# )),
html.Div(
    dcc.Graph(id="time-series-chart"),

    style={
        'width' : '32%',
        'flex' : '1' ,
          }

),




html.Div(
    dcc.Graph(id="gra"),

    style={
        'width' : '50%',
        'margin-top' : '-50%',
        'margin-left' : '54%',
        'position' : 'absolute'
          }

)

],
    style={
        'dispaly' : 'flex',
        'flex-direction' : 'row',
        
        
    })
])


@app.callback(
    Output('gra','figure'),
    [Input('demo-dropdown','value')]
)

def update_output(value):

    day = pd.read_csv(r"velacheryday.csv",skiprows={0}, usecols= [value])
    print(value)
    # dm = pd.DataFrame(mon)
    fig = px.line(day[value])
    # fig = px.line(day["TUE"])
    fig.update_layout(
        xaxis=dict(tickmode="linear",
        tick0=0,
        dtick=1)
    )
    #fig = mpl_to_plotly(fig)
    return fig


@app.callback(
    Output('time-series-chart', 'figure'),
    
    [Input('ticker', 'value')]
)

def update_output(value):
    
        
        fig = px.scatter(df, x=value, y="Time", size=value, hover_data=['Total'])
        return fig

app.run_server(debug=True)