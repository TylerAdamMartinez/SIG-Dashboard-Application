#data visualization
import graphing as grph
import plotting as plt

#data retrieval 
import Market_Data as md

#libaraies for Testing
import numpy as np
from rich.console import Console


""" THIS WILL NEED TO BE COMPLETELY REDONE TO USE Market_Data 
def Basic_Graphing_Test():
    "" Will systemically create data and graph the data on each one of the graphing functions "
    console = Console()
    print("\n")
    console.print("Basic Graphing Test", style="bold white on blue", justify="center")
    console.print("Starting Test", style="bold white on blue", justify="center")

    #Testing data
    startingDate = "2021-02-19"
    endingDate = "2021-03-21"
    datelist = cd.createDates(startingDate, endingDate)

    #single asset test
    prices_of_ETH = cd.getPricelist('ETH', datelist)
    asset_array = ['ETH', datelist, prices_of_ETH]

    #demostrates the graph
    grph.graph(asset_array[1], asset_array[2], "Price of ETH over time")

    #multi-assets test
    crypto_arr = np.array(['LINK','ETH','XRP','ADA', 'DOGE'])
    prices_of_assets = cd.getPricelists(crypto_arr, datelist)
    dates = []
    for i in range(len(crypto_arr)):
        dates.append(datelist)
    assets_array = [crypto_arr, dates, prices_of_assets]

    #demostrates the graphing compare functions
    grph.figcompare(assets_array)
    grph.graphcompare(assets_array)
    grph.subcompare(assets_array)

    console.print("Test Finnished", style="bold white on blue", justify="center")
"""

def Basic_Ploting_Test():
    """ Will systemically create data and plot the data on each one of the plotting functions """
    console = Console()
    print("\n")
    console.print("Basic Plotting Test", style="bold white on blue", justify="center")
    console.print("Starting Test", style="bold white on blue", justify="center")

    #Testing data
    startingDate = "2021-02-19"
    endingDate = "2021-03-21"
    asset = "avy"
   
    #single asset test
    avy_stock_data = md.stockData(asset, startingDate, endingDate)

    #demostrates the graph
    plt.candlesticks_plot(avy_stock_data)
    plt.plot(avy_stock_data.index , avy_stock_data['Close'])

    console.print("Test Finnished", style="bold white on blue", justify="center")
