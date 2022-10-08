from multiprocessing.sharedctypes import Value
from stringprep import map_table_b2
import matplotlib as mpl
from matplotlib.pyplot import figure
import plotly.express as px
import pandas as pd
import ipywidgets as widgets
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import dash
from plotly.tools import mpl_to_plotly

dat = pd.read_excel("C:/Users/Vamsi/Desktop/Review/dash/tt.xlsx",index_col=[0],skiprows={0})
    # dm = pd.DataFrame(mon)
fig = px.scatter(dat)
    #fig = mpl_to_plotly(fig)

mot = pd.read_excel("C:/Users/Vamsi/Desktop/Review/dash/pp.xlsx",index_col=[0])
photo = px.bar(mot)


pot =  pd.read_excel("C:/Users/Vamsi/Desktop/Review/dash/ttp.xlsx",index_col=[0])
palasa = px.bar(pot)

app = Dash(__name__)
app.layout=html.Div([
    html.Div(
    id="one",
    children="DASHBOARD for PERUNGUDI",
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
    
     dcc.Dropdown(['JAN','FEB','MARCH','APRIL','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'],['JAN','FEB'], id='demo-dropdown',multi=True),
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


html.Div(
    dcc.Graph(id="gra"),

    style={
        'width' : '100%',
        'flex' : '1' ,
          }

),

html.Div(
     dcc.Dropdown(['MON','TUE','WED','THU','FRI','SAT'],['MON','TUE'], id='drpdown',multi=True),
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

html.Div(
   
    dcc.Graph(id="coke"),
    
    style={
        'width' : '100%',
        'margin-top' : '20px',
      
          }

),


html.Div(
    dcc.Graph(figure=fig),

    

),


html.Div(
    children = "patterns generated for prefix-span",
    style={
        'font-size' : '20px',
        'font-weight' : 'bold',
        'margin-left' : '90px',
        'color' : 'purple'

      
    }
),

html.Div(

    dcc.Graph(figure = photo),
    style = {
        'width' : '45%'
    }
),

html.Div(
    children = "patterns generated for TT prefix-span",
    style={
        'font-size' : '20px',
        'font-weight' : 'bold',
        'margin-left' : '55%',
        'position' : 'absolute',
        'margin-top' : '-38%',
        'color' : 'purple'
    }
),
html.Div(

    dcc.Graph(figure = palasa),
    style = {
        'width' : '45%',
        'margin-left' : '50%',
        'position' : 'absolute',
        'margin-top' : '-36%'
    }
),

],
    style={
        'dispaly' : 'flex',
        'flex-direction' : 'row',
        
        
    })
])

@app.callback(
    Output('gra', 'figure'),
    Input('demo-dropdown', 'value')
)
def update_output(value):

    mon = pd.read_excel("C:/Users/Vamsi/Desktop/Review/dash/DAYWISEPERUNGUDI.xlsx",skiprows={0}, usecols= value,sheet_name="DAY1")
    fig = px.line(mon[value])
    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Vehicle Count",
        xaxis=dict(tickmode="linear",
        tick0=0,
        dtick=1)
    )

    return fig

@app.callback(
    Output('coke','figure'),
    Input('drpdown','value')
)

def update_output(value):
    
    day = pd.read_csv("C:/Users/Vamsi/Desktop/Review/dash/velacheryday.csv",skiprows={0}, usecols=value)                                 
    # dm = pd.DataFrame(mon)
    fig = px.line(day)
    # fig = px.line(day["TUE"])
    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Vehicle Count",
        xaxis=dict(tickmode="linear",
        tick0=0,
        dtick=1)
    )
    #fig = mpl_to_plotly(fig)
    return fig






   

if __name__ == '__main__':
    app.run_server(debug=True)