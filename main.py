#data visualization
import graphing as grph
import plotting as plt

#data retrieval 
import cryptoData as cd
import stockData as sd

#Used for Test Driven Development
import Unit_Testing as ut

"""
TODO:
This code below will be in it's own file once finnished
"""
#Create Dashboard
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from datetime import date
today = date.today()
import datetime
last_year = datetime.datetime.now().year - 1
this_month = datetime.datetime.now().month
this_day = datetime.datetime.now().day
today_last_year = datetime.datetime(last_year, this_month, this_day).strftime("%B %d, %Y")


#TESTING DATA
asset_dataframe = sd.stockData("googl", "2020-04-10", "2021-04-10")
fig_price_plot = plt.plot(asset_dataframe.index, asset_dataframe['Close'])
fig_stock_plot = plt.stock_plot(asset_dataframe.index, asset_dataframe)
fig_candlestick = plt.candlesticks_plot(asset_dataframe, "Candlesticks Plot of Google")

#Dashborad Layout
app = dash.Dash()
app.layout = html.Div(
    
    [
        html.H1("SIG Application", style={'text-align': 'center'}),
        html.Div(
            children = [
                html.Div(
                    className="Asset_type",
                    children = [
                        dcc.Dropdown(
                            id="asset_type", 
                            options=[
                            {'label': 'stocks', 'value':'stock' },
                            {'label': 'cryptocurrenices', 'value':'crypto'}],
                            placeholder="Select an asset type",
                            value='stock'
                        ) 
                    ]),
                html.Div(
                    className="Input",
                    children=[
                        dcc.Input(
                            id="asset_input", 
                            style={'width': '80%', 'height': '30px', 'padding': '0px', 'margin': '0px'}
                        ),
                        html.Button(
                            'Submit',
                            id="asset_input_submit_btn",
                            style={'width': '19%', 'height': '35px'}
                        )                  
                    ]),
                html.Div(
                    className="DatePicker",
                    children = [
                            dcc.DatePickerRange(
                            id="date_range",
                            is_RTL=True,
                            display_format="MMMM DD, YYYY",
                            start_date=today,
                            end_date_placeholder_text=today_last_year, 
                            style={'width': '100%', 'height': '30px'} 
                        )
                    ]
                )                
            ],
            style={
                'display':'grid',
                'grid-template-columns':'1fr 1fr 1fr'
            }
        ),
        html.Br(),
        dcc.Tabs(
            id="tabs",
            value="candlestick",
            children=[
                dcc.Tab(label="Candlestick", value="candlestick"),
                dcc.Tab(label="Price Plot", value="price_plot"),
                dcc.Tab(label="Stock Plot", value="stock_plot")
            ]
        
        ),
        html.Div(id='tabs-content'),
        html.Footer("Created By Tyler Adam Martinez and Svenn Mivedor",
            style={
                'text-align': 'center',
                'bottom': '10px'
            })
    ]
)

@app.callback(
    Output('tabs-content', 'children'),
    Input('tabs', 'value'), 
)

def render_content(tab):
    if tab == 'candlestick':
        return dcc.Graph(figure=fig_candlestick)
    elif tab == 'price_plot':
        return dcc.Graph(figure=fig_price_plot)
    elif tab == 'stock_plot':
        stock_plot_div = [
            html.Div(
                id="stock_plot_div",
                children=[
                    dcc.Graph(figure=fig_stock_plot),
                    dcc.Checklist(
                        id="stock_plot_lines",
                        options=[
                            {'label': 'Low', 'value': 'Low'},
                            {'label': 'High', 'value': 'High'},
                            {'label': 'Open', 'value': 'Open'},
                            {'label': 'Close', 'value': 'Close'}
                        ],
                        value=['Low', 'High', 'Open', 'Close'],
                        labelStyle={'display': 'inline-block'}
                    )                   
                ]
            )
        ]
        return stock_plot_div
app.run_server(debug=True)
