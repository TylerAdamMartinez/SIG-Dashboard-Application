import plotly.graph_objects as go
import numpy as np
import pandas as pd
from rich.table import Table
from rich import print

"""""""""  Single Asset Plotting """""""""""

def plot(time_array, price_array, plottitle = "Price of asset over time",  yaxistitle = 'Price (USD)', xaxistitle = 'Time (Months)'):
	""" First parameter is for the price array and the second is for the time array"""
	
	#Creates the figure
	fig = go.Figure(
		data = [
			go.Scatter(
				x = time_array,
				y = price_array,
			)
		]
	)
	fig.update_layout(
		title = plottitle,
		yaxis_title = yaxistitle,
		xaxis_title = xaxistitle, 
		template="plotly_dark"
	)
	print("[bold purple][Displaying\t][/bold purple] plot")
	print(f"[bold yellow][Title:\t\t][/bold yellow] {plottitle}")
	return fig
	print("[bold red][Exiting\t][/bold red] plot\n")

def stock_plot(time_array, stock_dataTable, plottitle = "Price of asset over time",  yaxistitle = 'Price (USD)', xaxistitle = 'Time (Months)'):
	""" First parameter is for the price array and the second is for the time array"""
	
	#Creates the figure
	fig = go.Figure(
		data = [
			go.Scatter(
				x = time_array,
				y = stock_dataTable['Low'],
				name="Low"
			)
		]
	)
	fig.add_scatter(
		x = time_array, 
		y = stock_dataTable['High'],
		name="High"
	)
	fig.add_scatter(
		x = time_array, 
		y = stock_dataTable['Close'],
		name="Close"
	)
	fig.add_scatter(
		x = time_array, 
		y = stock_dataTable['Open'],
		name="Open"
	)
	fig.add_scatter(
		x = time_array, 
		y = stock_dataTable['Adj Close'],
		name="Adjusted Close"
	)
	fig.update_layout(
		title = plottitle,
		yaxis_title = yaxistitle,
		xaxis_title = xaxistitle, 
		template="plotly_dark"
	)
	print("[bold purple][Displaying\t][/bold purple] plot")
	print(f"[bold yellow][Title:\t\t][/bold yellow] {plottitle}")
	return fig
	print("[bold red][Exiting\t][/bold red] plot\n")

def candlesticks_plot(asset_dataframe, plottitle = "Price of asset over time",  yaxistitle = 'Price (USD)', xaxistitle = 'Time (Months)'):
	""" First parameter is for the asset date in pandas Datatable where the dates are the indexes """
	
	#Creates the figure
	fig = go.Figure(
		data = [
			go.Candlestick(
				x = asset_dataframe.index,
				low = asset_dataframe['Low'], 
				high = asset_dataframe['High'],
				close = asset_dataframe['Close'],
				open = asset_dataframe['Open'],
				
				#makes the highs green and the lows red
				increasing_line_color = 'green',
				decreasing_line_color = 'red'
			)
		]
	)
	fig.update_layout(
		xaxis_rangeslider_visible=False,
		title = plottitle,
		yaxis_title = yaxistitle,
		xaxis_title = xaxistitle,
		template="plotly_dark"
	)

	#sets up the graph and displays it to the screen in the figure
	print("[bold purple][Displaying\t][/bold purple] candlestick plot")
	print(f"[bold yellow][Title:\t\t][/bold yellow] {plottitle}")
	return fig
	print("[bold red][Exiting\t][/bold red] plot\n")

	
def volume_plot(asset_dataframe, plottitle = "Trading Volume of asset over time",  yaxistitle = 'Number of Trades', xaxistitle = 'Time (Months)'):
	""" First parameter is for the asset date in pandas Datatable where the dates are the indexes """
	
	#Creates the figure
	fig = go.Figure(
		data = [
			go.Bar(
				x = asset_dataframe.index,
				y = asset_dataframe['Volume'],
				name="Volume",
			)
		]
	)
	fig.update_layout(
		title = plottitle,
		yaxis_title = yaxistitle,
		xaxis_title = xaxistitle,
		template="plotly_dark"
	)

	#sets up the graph and displays it to the screen in the figure
	print("[bold purple][Displaying\t][/bold purple] volume plot")
	print(f"[bold yellow][Title:\t\t][/bold yellow] {plottitle}")
	return fig
	print("[bold red][Exiting\t][/bold red] plot\n")

def stats_table(asset_dataframe, tabletitle = "Stats of asset in a table format"):
	""" First parameter is for the asset date in pandas Datatable where the dates are the indexes """

	#Creates the figure
	fig = go.Figure(
		data = [
			go.Table(
				header=dict(values=list(["Dates", "Low", "High", "Close", "Open", "Volume", "Adj Close"]),
							align='center'),
				cells=dict(values=[
								asset_dataframe.index, 
								asset_dataframe['Low'], 
								asset_dataframe['High'],
								asset_dataframe['Close'],
								asset_dataframe['Open'],
								asset_dataframe['Volume'],
								asset_dataframe['Adj Close'],
							],
						align='center',
						)
			)
		]
	)
	fig.update_layout(
		title = tabletitle,
		template="plotly_dark"
	)

	#sets up the graph and displays it to the screen in the figure
	print("[bold purple][Displaying\t][/bold purple] stats table")
	print(f"[bold yellow][Title:\t\t][/bold yellow] {tabletitle}")
	return fig
	print("[bold red][Exiting\t][/bold red] table\n")


def financials_table(asset_financial_dataframe, tabletitle = "Stats of asset in a table format"):
	""" First parameter is for the asset date in pandas Datatable where the dates are the indexes """
	rowEvenColor = 'grey'
	rowOddColor = 'darkgrey'

	#Creates the figure
	asset_financial_dataframe.insert(0, 'Financials Categories', asset_financial_dataframe.index)
	list_of_columns = list( asset_financial_dataframe.columns)
	list_of_cells = list([])
	for col in range(asset_financial_dataframe.shape[1]):
		list_of_cells.append(asset_financial_dataframe.iloc[:,col])

	fig = go.Figure(
		data = [
			go.Table(
				header=dict(values=list_of_columns),
				cells=dict(values=list_of_cells)
                                                                ),
                                
			
		]
	)
	fig.update_layout(
		title = tabletitle,
		template="plotly_dark"
	)

	#sets up the graph and displays it to the screen in the figure
	print("[bold purple][Displaying\t][/bold purple] stats table")
	print(f"[bold yellow][Title:\t\t][/bold yellow] {tabletitle}")
	return fig
	print("[bold red][Exiting\t][/bold red] table\n")
