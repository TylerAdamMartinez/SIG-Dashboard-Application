import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def graph(price_array, time_array, graphtitle = "Price of asset over time",  yaxistitle = 'Price (USD)', xaxistitle = 'Time (months)'):
	""" First parameter is for the price array and the second is for the time array"""
	fig = plt.figure(graphtitle)
	#sets the background of the plot to trasparent
	fig.patch.set_alpha(0.0)
	ax = plt.axes()
	ax.patch.set_alpha(0.0)
	plt.title(graphtitle)
	plt.plot(price_array, time_array)
	plt.ylabel(yaxistitle)
	plt.xlabel(xaxistitle)
	print("Displaying graph")
	plt.show()
	print("Exit graph")

def subcompare(assets_array, subplot_title = "The prices over time:", yaxistitle = 'Price (USD)', xaxistitle = 'Time (months)'):
	"""Compares multiple assets in one price over time graph. (Parameter: Expects a Matrix)"""
	number_of_assets = len(assets_array[0])

	#Dynamically creates the title and adds in all the assets to it
	title_array = [subplot_title]
	for assets_name in assets_array[0]:
		title_array.append(assets_name)
	title = pd.Series(title_array)
	title = title.str.cat(sep=" ")
	
	#creates new transparent figure and inputs the title
	fig = plt.figure(title)
	fig.patch.set_alpha(0.0)
	plt.title(title)

	#dynamically determine which subplot figuration is best based on the number of assets 
	if(number_of_assets % 2 == 0 and number_of_assets >= 4):
		#dynamically subplots the data xs then ys in a nested for loop
		num_of_rows = int(number_of_assets / 2)
		num_of_cols = int(number_of_assets / 2)
		for i in range(number_of_assets):
			ax = plt.subplot(num_of_rows, num_of_cols, i + 1)
			#sets the background of the plot to trasparent
			ax.patch.set_alpha(0.0)
			plt.title(assets_array[0][i])
			plt.ylabel(yaxistitle)
			plt.xlabel(xaxistitle)
			plt.plot(assets_array[1][i], assets_array[2][i])
	else:
		#dynamically subplots the data xs then ys in a nested for loop
		num_of_rows = number_of_assets
		for i in range(number_of_assets):
			ax = plt.subplot(num_of_rows, 1, i + 1)
			#sets the background of the plot to trasparent
			ax.patch.set_alpha(0.0)
			plt.title(assets_array[0][i])
			plt.ylabel(yaxistitle)
			plt.xlabel(xaxistitle)
			plt.plot(assets_array[1][i], assets_array[2][i])

	#displays the plot
	print("Displaying subcompare graph")
	plt.show()
	print("Exit subcompare graph")

def figcompare(assets_array, figure_title =  "The prices over time:\n", yaxistitle = 'Price (USD)', xaxistitle = 'Time (months)'):
	"""Compares multiple assets in multiple price over time graph. (Parameter: Expects a Matrix)"""
	number_of_assets = len(assets_array[0])

	#Dynamically creates the title and adds in all the assets to it
	title_array = [figure_title]
	count = 0
	for assets_name in assets_array[0]:
		title = figure_title + " " + assets_name
	
		#creates new transparent figure and inputs the title
		fig = plt.figure(title)
		fig.patch.set_alpha(0.0)
		ax = plt.axes()
		ax.patch.set_alpha(0.0)
		
		plt.title(title)
		plt.ylabel(yaxistitle)
		plt.xlabel(xaxistitle)
		plt.plot(assets_array[1][count], assets_array[2][count])
		count = count + 1

	#displays the plot
	print("Displaying figcompare graph")
	plt.show()
	print("Exit figcompare graph")

def graphcompare(assets_array, figure_title =  "The prices over time:\n", yaxistitle = 'Price (USD)', xaxistitle = 'Time (months)'):
	"""Compares multiple assets in one price over time graph. (Parameter: Expects a Matrix)"""
	number_of_assets = len(assets_array[0])

	#Dynamically creates the title and adds in all the assets to it
	title_array = [figure_title]
	for assets_name in assets_array[0]:
		title_array.append(assets_name)
	title = pd.Series(title_array)
	title = title.str.cat(sep=" ")

	#creates new transparent figure and inputs the title
	fig = plt.figure(title)
	fig.patch.set_alpha(0.0)
	ax = plt.axes()
	ax.patch.set_alpha(0.0)
	
	plt.title(title)
	plt.ylabel(yaxistitle)
	plt.xlabel(xaxistitle)
	
	for i in range(number_of_assets):
		asset_name = assets_array[0][i]
		plt.plot(assets_array[1][i], assets_array[2][i], label = asset_name)

	#displays the plot
	plt.legend(loc=2)
	print("Displaying graphcompare graph")
	plt.show()
	print("Exit graphcompare graph")
