'''
S&P 500 Index source: yahool finance tickers = "^GSPC"
Fed rates data source: https://fred.stlouisfed.org/series/FEDFUNDS

'''

import os, sys
import pandas as pd
import datetime

import yfinance as yf
spxData = yf.download (tickers = "^GSPC", start = "1990-01-01", interval = "1d")

spxData = spxData[['Close']]
spxData.rename(columns={'Close':'Prices'}, inplace=True)
spxData['YearMonth'] = spxData.index
spxData['YearMonth'] = spxData['YearMonth'].dt.strftime('%Y%m');

monthData=spxData.groupby('YearMonth').agg({'Prices':'max'})
del spxData

ratesData = pd.read_csv('fed-funds-rate-historical-chart.csv')
ratesData['YearMonth']=pd.to_datetime(ratesData['DATE'])
ratesData = ratesData.rename(columns={'FEDFUNDS':'Rates'})
ratesData = ratesData[['YearMonth','Rates']]
ratesData = ratesData[ratesData.YearMonth>=datetime.datetime.strptime('19900101', '%Y%m%d')]
ratesData['YearMonth'] = ratesData['YearMonth'].dt.strftime('%Y%m')
ratesData.set_index('YearMonth', inplace=True)

mergedPd = ratesData.merge(monthData, left_index=True, right_index=True, how='outer')
mergedPd.iloc[-1, 0]=mergedPd.iloc[-2]['Rates']
mergedPd.rename(columns={'Prices':'S&P 500 Index'}, inplace=True)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,5))
mergedPd.plot(y='S&P 500 Index', ax=ax)
mergedPd.plot(y='Rates', ax=ax, secondary_y=True)

plt.close()