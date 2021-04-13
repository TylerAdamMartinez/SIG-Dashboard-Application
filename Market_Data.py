import pandas as pd
import numpy as np
import yfinance as yfi
import datetime as dt
from pandas_datareader import data as pdr

def inputStockDate():
    """Enter Stock Ticker, start date and end date returns Panda Datatable of the asset"""
    stock = input('Enter a Ticker Symbol: ')
    start = input('Start Date: ')
    end = input('End Date: ')
    stock_data = stockData(stock, start, end)
    return stock_data

def get_stockData(ticker_symbol , start_date, end_date):
    """Accepts stock ticker, start date, and end date in as string datetype. Then returns a Panda Datatable of the asset's info from the starting date to the ending date"""
    data = pdr.get_data_yahoo(ticker_symbol ,start=start_date, end=end_date)
    return data 

def get_stockFinancials(ticker_symbol):
    """Accepts stock ticker as string datetype. Then returns a Panda Datatable of the asset's financial info"""
    fin_data = yfi.Ticker(ticker_symbol).financials
    return fin_data

