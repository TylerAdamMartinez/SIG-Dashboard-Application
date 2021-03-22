import numpy as np
import cryptocompare as cc
from datetime import datetime as dt
import pandas as pd

def createDates(startDate , endDate):
    """Creates an array of datetime objects from the startDate (datetime obj) to the endDate (datetime obj)"""
    datelist = pd.date_range(start=startDate , end=endDate).to_pydatetime().tolist()
    datelist = np.array(datelist)
    return datelist

def getPricelist(name_of_asset, datelist, currency = 'USD'):
    """Creates an array of prices of the named asset for each date in the array of dates in the currency specified (by default USD)"""
    prices = []
    num_of_dates = len(datelist)
    
    #Let users know that the program is working.. just loading the data ..
    print("loading data for", name_of_asset, "from API... (This might take a moment)")

    for i in range(num_of_dates):
        price_obj = cc.get_historical_price(name_of_asset, currency , datelist[i], 'Kraken')
        price = price_obj.get(name_of_asset)[currency]
        prices.append(price)
    
    return prices

def getPricelists(name_of_assets, datelist, currency = 'USD'): 
    """Creates an 2D matrix of prices of the named assets for each date in the array of dates in the currency specified (by default USD)"""
    #creates the dates array from the datelist
    dates = []
    num_of_assets = len(name_of_assets)

    #creates the prices array base on the assets
    prices = []
    num_of_dates = len(datelist)
    for i in range(num_of_assets):
        price_of_asset = getPricelist(name_of_assets[i], datelist, currency)
        prices.append(price_of_asset)
        
    return prices
