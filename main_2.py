import numpy as np
import pandas as pd
import datetime as dt
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv('data/formattedData.csv')
df = df.drop(['Unnamed: 0'],axis=1)

df['date'] = pd.to_datetime(df['date']).astype('datetime64[ns]')
df.sort_values(by='date', inplace = True)


app = Dash()
fig = px.line(df, x = 'date', y = 'sales')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales'),

    html.Div(children='''
        Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?
    '''),

    dcc.Graph(
        id='Pink Morsel Sales',
        figure=fig
    )
])
if __name__ == '__main__':
    app.run(debug=True)