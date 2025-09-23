from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import os

def make_dataframe(directory):
    files = os.listdir(directory)
    frames = []
    for file in files:
        frames.append(pd.read_csv("data/" + file))
    df = pd.concat(frames, axis=0, ignore_index=True)
    
    #select pink morsel
    #df = df[df["product"] == "pink morsel"]

    #create sales column
    df["price"] = df["price"].str.replace("$", "").astype(float)
    df['sales'] = df.price * df.quantity
    
    
    #create final df
    df = df[["date", "sales", "region", 'product']]
    
    # sorting by date
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    return df


def dash_app(df):
    # Run this app with `python app.py` and
    # visit http://127.0.0.1:8050/ in your web browser.


    colors = {
    'line': "#6F00FF",
    'text': "#3B0270",
    "background": "#FFF1F1"
    
    }

    app = Dash()
    app.layout = html.Div([
            html.Div([
                html.Div(children='Sales Revenue Against Time', style={
                'textAlign': 'center',
                'color': colors['text']}), 

            html.Div([
                dcc.RadioItems(
                    df.region.unique(),
                    'north',
                    id='region-name',
                    inline=True
                )
            ], style={'width': '48%', 'display': 'inline-block'}),

        ]),

               dcc.Graph(id='sales-graph')
    ])
    
    @callback(
        Output("sales-graph", "figure"), 
        Input("region-name", "value")
    )
    def update_graph(region):
        df_region = df[df["region"] == region]
        
        fig = px.scatter(df, x = 'date', y = 'sales', color = 'product')
        
        fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
        )
        
        fig.update_yaxes(title = "Sales in the " + region)
        fig.update_xaxes(title = "Date")
        
        return fig
    return app

if __name__ == '__main__':
    df = make_dataframe("data/")
    app = dash_app(df)
    app.run(debug=True)



    
    
    
    
