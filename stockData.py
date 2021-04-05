import pandas as pd
import numpy as np
import yfinance as yfi
import datetime as dt
from pandas_datareader import data as pdr



import graphing 
import cryptoData as cD


def stockData():
    """Enter Stock Ticker, start date and end date returns Panda Datatable"""
    stock = input('Enter a Ticker Symbol: ')
    start = input('Start Date: ')
    end = input('End Date: ')
    data = pdr.get_data_yahoo(stock,start=start, end=end)
    close = np.array(data['Close'])
    print(close)
    print(np.size(close))

    dates = cD.createDates(start, end)[:-1]
    print(dates)
    print(np.size(dates))
    

    return data,dates 


stockdata, dates = stockData()

graphing.graph(dates, stockdata)


