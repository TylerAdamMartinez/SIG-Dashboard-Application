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
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

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


Dark_Mode = dbc.themes.DARKLY
Light_Mode = dbc.themes.LITERA

#Dashborad Layout
app = dash.Dash(external_stylesheets=[Dark_Mode])
app.title = "SIG Application"
app.layout = html.Div(
    
    [
        html.H1("SIG Application", style={'text-align': 'center'}),
        html.Br(),
        dbc.Row(
            children = [
                dbc.Col(
                    className="Asset_type",
                    children = [
                        dbc.InputGroup([ 
                        dbc.Select(
                            id="asset_type", 
                            options=[
                            {'label': 'stocks', 'value':'stock' },
                            {'label': 'cryptocurrenices', 'value':'crypto'}],
                            placeholder="Select an asset type",
                            value='stock'
                        ),
                        dbc.InputGroupAddon("Asset Type", addon_type="append"),
                        ]),
                    ],
                    width=2,
                    ),
                dbc.Col(
                    className="Input",
                    children=[
                        dbc.InputGroup([
                        dbc.Input(
                            id="asset_input", 
                            placeholder="name of asset here..."
                        ),
                        dbc.InputGroupAddon(
                            dbc.Button("Enter", 
                            id="asset_input_submit_btn"),
                            addon_type="append",
                            )
                        ]),
                    ],
                    width=8,
                    ),
                dbc.Col(
                    className="DatePicker",
                    children = [
                            dbc.Button(
                                "Dates",
                                id="Choose_Dates_Collapse_Btn",
                                block=True
                            ),
                            dbc.Collapse(
                                dbc.Card(
                                    dcc.DatePickerRange(
                                        id="date_range",
                                        is_RTL=True,
                                        display_format="MMMM DD, YYYY",
                                        start_date=today,
                                        end_date_placeholder_text=today_last_year, 
                                        with_portal=True
                                    )                                    
                                ),
                                id="date_range_collapse"
                            )
                    ],
                    width=2,
                )                
            ],
            justify="center",
            no_gutters=True,
        ),
        html.Br(),
        dbc.Tabs(
            id="tabs",
            active_tab="candlestick",
            children=[
                dbc.Tab(label="Candlestick", tab_id="candlestick"),
                dbc.Tab(label="Price Plot", tab_id="price_plot"),
                dbc.Tab(label="Stock Plot", tab_id="stock_plot")
            ]
        
        ),
        html.Div(id='tabs-content'),
        html.Br(),
        html.Footer("Created By Tyler Adam Martinez and Svenn Mivedor",
            style={
                'text-align': 'center',
                'bottom': '10px'
            })
    ]
)

@app.callback(
    Output('tabs-content', 'children'), 
    Input('tabs', 'active_tab'), 
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
                    dbc.Label("Toggle Lines"),
                    dbc.Checklist(
                        id="stock_plot_lines",
                        options=[
                            {'label': 'Low', 'value': 'Low'},
                            {'label': 'High', 'value': 'High'},
                            {'label': 'Open', 'value': 'Open'},
                            {'label': 'Close', 'value': 'Close'}
                        ],
                        value=['Low', 'High', 'Open', 'Close'],
                        inline=True,
                        switch=True,
                    )                   
                ]
            )
        ]
        return stock_plot_div

@app.callback(
    Output('date_range_collapse', 'is_open'),
    Input('Choose_Dates_Collapse_Btn', 'n_clicks'),
    State('date_range_collapse', 'is_open'),
)

def toggle_date_picker(n, is_open):
    if n:
        return not is_open
    return is_open

app.run_server(debug=True)
