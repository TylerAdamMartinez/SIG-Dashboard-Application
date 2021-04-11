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


#TESTING DATA
asset_dataframe = sd.stockData("googl", "2021-01-01", "2021-02-02")
fig_plot = plt.plot(asset_dataframe.index , asset_dataframe['Close'])
fig_candlestick = plt.candlesticks_plot(asset_dataframe)

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
                            id="asset_input"
                        ),
                        html.Button(
                            'Submit',
                            id="asset_input_submit_btn"
                        )                  
                    ]),
                html.Div(
                    className="DatePicker",
                    children = [
                            dcc.DatePickerRange(
                            id="date_range",
                            start_date_placeholder_text="Select a date",
                            end_date="2021-03-03"
                        )
                    ]
                )                
            ],
            style={
                'display':'grid',
                'grid-template-columns':'auto auto auto'
            }
        ),
        dcc.Tabs(
            id="tabs",
            value="candlestick",
            children=[
                dcc.Tab(label="Candlestick", value="candlestick"),
                dcc.Tab(label="Simple Plot", value="simple_plot")
            ]
        
        ),
        html.Div(id='tabs-content'),
        html.Footer("Created By Tyler Adam Martinez and Svenn Mivedor",style={'text-align': 'center'})
    ]
)

@app.callback(Output('tabs-content', 'children'), Input('tabs', 'value'))

def render_content(tab):
    if tab == 'candlestick':
        return dcc.Graph(figure=fig_candlestick)
    elif tab == 'simple_plot':
        simple_plot_div = [
            dcc.Checklist(
                options=[
                    {'label': 'Low', 'value': 'Low'},
                    {'label': 'High', 'value': 'High'},
                    {'label': 'Open', 'value': 'Open'},
                    {'label': 'Close', 'value': 'Close', 'disabled': True}
                ],
                value=['Close'],
                labelStyle={'display': 'inline-block'}
            ),
            dcc.Graph(figure=fig_plot)
        ]
        return simple_plot_div
app.run_server(debug=True)
