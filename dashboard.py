#data visualization
import plotting as plt

#data retrieval
import Market_Data as md

#Create Dashboard
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from datetime import date
today = date.today().strftime("%Y-%m-%d")
import datetime
last_year = datetime.datetime.now().year - 1
this_month = datetime.datetime.now().month
this_day = datetime.datetime.now().day
today_last_year = datetime.datetime(last_year, this_month, this_day).strftime("%Y-%m-%d")

Dark_Mode = dbc.themes.CYBORG
Light_Mode = dbc.themes.LITERA

#Dashborad Layout
app = dash.Dash(external_stylesheets=[Dark_Mode], suppress_callback_exceptions=True)
app.title = "SIG Application"
app.layout = html.Div(
    
    [
        html.H1("SIG Application", style={'text-align': 'center'}),
        dbc.Row(
            [
                dbc.Col(
                    className="Input",
                    children=[
                        dbc.InputGroup([
                        dbc.Input(
                            id="asset_input", 
                            placeholder="name of asset here...",
                            value="avy"
                        ),
                        dbc.InputGroupAddon(
                            dbc.Button("Enter", 
                            id="asset_input_submit_btn"),
                            addon_type="append",
                            )
                        ]),
                    ],
                    width=10,
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
                                        start_date=today_last_year,
                                        end_date=today, 
                                        with_portal=True,
                                    )                                    
                                ),
                                id="date_range_collapse"
                            )
                    ],
                    width=2,
                )                
            ],
            justify="center",
            style={'padding': '25px'}
        ),
        html.Div(
            children = [
                dbc.Tabs(
                    id="tabs",
                    active_tab="candlesticks_plot",
                    children=[
                        dbc.Tab(label="Candlesticks Plot", tab_id="candlesticks_plot"),
                        dbc.Tab(label="Stats Plot", tab_id="stats_plot")
                    ]
                ),
                html.Div(id='tabs-content'), 
            ],
            style={'padding': '25px'}
        ),
        html.Div(id='volume_and_adj_close_section', style={'padding': '25px'}),
        html.Div(id='stats-table', style={'padding': '25px'}),
        html.Footer("Created By Tyler Adam Martinez and Svenn Mivedor", style={'text-align':'center'})
    ]
)


#This will change the asset, therefore, changing the data on the plot, and depending on which tab is selected it will show you a different type of graph 
@app.callback(
    [ 
        Output('tabs-content', 'children'), 
        Output('volume_and_adj_close_section', 'children'),
        Output('stats-table', 'children'),
    ], 
    [
        Input('asset_input_submit_btn', 'n_clicks'), 
        Input('asset_input', 'value'), 
        Input('date_range', 'start_date'),
        Input('date_range', 'end_date'),
        Input('tabs', 'active_tab')
    ]
)

def render_tabs_content(asset_input_submit_btn, asset_input, start_date, end_date, tab):
    #If stock will retrive data from the stock API, if crypto then retrive data from the crypto API
    asset_dataframe = md.get_stockData(asset_input, start_date, end_date)
    asset_financial_dataframe = md.get_stockFinancials(asset_input)

    if tab == 'candlesticks_plot':
        fig_candlestick = plt.candlesticks_plot(asset_dataframe, plottitle=f"Price of {asset_input} over time")

        volume_and_adj_close_section = [
            dbc.Row(
                [
                dbc.Col(
                   dcc.Graph(figure=plt.volume_plot(asset_dataframe, plottitle=f"Trading volume of {asset_input} over time")) 
                ),
                dbc.Col(
                    dcc.Graph(figure=plt.plot(asset_dataframe.index, asset_dataframe['Adj Close'], plottitle=f"Adjusted Close Price of {asset_input} over time"))
                )
                ]
            )
            
        ]

        stats_tables = [
            html.Div (
                children = [
                   dcc.Graph(figure=plt.stats_table(asset_dataframe, tabletitle=f"Stock stats table of {asset_input}"))
                ]
            ),
            html.Br(),
            html.Div (
                children = [
                   dcc.Graph(figure=plt.financials_table(asset_financial_dataframe, tabletitle=f"Financial stats table of {asset_input}")) 
                ]
            )
        ]
        

        return dcc.Graph(figure=fig_candlestick), volume_and_adj_close_section, stats_tables
    elif tab == 'stats_plot':
        fig_stock_plot = plt.stock_plot(asset_dataframe.index, asset_dataframe, plottitle=f"Price of {asset_input} over time")
        stats_plot_div = [
            html.Div(
                id="stats_plot_div",
                children=[
                    dcc.Graph(figure=fig_stock_plot),               
                ]
            )
        ]

        stats_tables = [
            html.Div (
                children = [
                   dcc.Graph(figure=plt.stats_table(asset_dataframe, tabletitle=f"Stats table of {asset_input}"))
                ]
            ),
            html.Br(),
            html.Div (
                children = [
                
                   dcc.Graph(figure=plt.financials_table(asset_financial_dataframe, tabletitle=f"Financial stats table of {asset_input}")) 
                   ]
                )
        ]

        return stats_plot_div, dcc.Graph(figure=plt.volume_plot(asset_dataframe, plottitle=f"Trading volume of {asset_input} over time")), stats_tables


#This will toggle the date picker from showing to hidden
@app.callback(
    Output('date_range_collapse', 'is_open'),
    Input('Choose_Dates_Collapse_Btn', 'n_clicks'),
    State('date_range_collapse', 'is_open'),
)

def toggle_date_picker(n, is_open):
    if n:
        return not is_open
    return is_open

