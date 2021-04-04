import pandas as pd
import numpy as np
import yfinance as yfi
import datetime as dt
from pandas_datareader import data as pdr



import graphing 



def stockData():
    """Enter Stock Ticker, start date and end date returns Panda Datatable"""
    stock = input('Enter a Ticker Symbol: ')
    start = input('Start Date: ')
    end = input('End Date: ')
    data = pdr.get_data_yahoo(stock,start=start, end=end)
    adj_close = data['Adj Close']
    print(adj_close)
    print(data)

    return data


stockdata = stockData()

graphing.graph(stockdata)


