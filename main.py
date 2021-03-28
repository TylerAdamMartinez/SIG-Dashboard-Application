import graphing as grph
import cryptoData as cd
import numpy as np
import SIGApp as ui

def Basic_Test():
    print("Starting Test")

    #Testing data
    startingDate = "2021-02-19"
    endingDate = "2021-03-21"
    datelist = cd.createDates(startingDate, endingDate)

    #single asset test
    prices_of_ETH = cd.getPricelist('ETH', datelist)
    asset_array = ['ETH', datelist, prices_of_ETH]

    #multi-assets test
    crypto_arr = np.array(['LINK','ETH','XRP','ADA', 'DOGE'])
    prices_of_assets = cd.getPricelists(crypto_arr, datelist)
    dates = []
    for i in range(len(crypto_arr)):
        dates.append(datelist)
    assets_array = [crypto_arr, dates, prices_of_assets]

    #demostrates the graph
    grph.graph(asset_array[1], asset_array[2], "Price of ETH over time")

    #demostrates the graphing compare functions
    grph.figcompare(assets_array)
    grph.graphcompare(assets_array)
    grph.subcompare(assets_array)

    print("Test Finnished")

if __name__ == '__main__':
    ui.SIGApp().run()