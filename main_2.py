import numpy as np
import pandas as pd
import datetime as dt
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

df = pd.read_csv('data/formattedData.csv')
df = df.drop(['Unnamed: 0'],axis=1)

df['date'] = pd.to_datetime(df['date']).astype('datetime64[ns]')
df.sort_values(by='date', inplace = True)
regions = np.append(df['region'].unique(), 'all')


app = Dash()

app.layout = html.Div([
    html.H1(children='Does sales change after January 15th',
            style = {
                'textAlign': 'center',
                'color' : '#8E67E0'
            }
            ),
    
    dcc.RadioItems(
        options = regions,
        value = regions[-1],
        id = 'radio',
        inline=True
    ),
    dcc.Graph(id='graph'),
    
    
])


@callback(
    Output('graph', 'figure'),
    Input('radio','value'))
def update_graph(radio):
    if radio == 'all':
        dff = df
    else:
        dff = df[df['region'] == radio]
        
    fig = px.line(dff, x = 'date', y = 'sales', hover_name='region')
    fig.update_traces(line=dict(color='#DE67E0'))
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    return fig

    
app.run(debug=True)