import plotly.graph_objects as go
import numpy as np
import pandas as pd
from rich.table import Table
from rich import print

"""""""""  Single Asset Plotting """""""""""

def plot(time_array, price_array, plottitle = "Price of asset over time",  yaxistitle = 'Price (USD)', xaxistitle = 'Time (months)'):
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

def stock_plot(time_array, stock_dataTable, plottitle = "Price of asset over time",  yaxistitle = 'Price (USD)', xaxistitle = 'Time (months)'):
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

def candlesticks_plot(asset_dataframe, plottitle = "Price of asset over time",  yaxistitle = 'Price (USD)', xaxistitle = 'Time (months)'):
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

	