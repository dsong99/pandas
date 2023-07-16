import os, sys
import pandas as pd
import datetime
import yfinance as yf
dataDf = yf.download (tickers = "DX-Y.NYB", start = "1954-07-01", interval = "1d")

dataDf.to_csv(os.path.join(os.getcwd(),'stocks','data', 'usd_index_history.csv'))
dataDf = dataDf[['Close']]
dataDf.rename(columns={'Close':'Prices'}, inplace=True)

dataDf['YearMonth'] = dataDf.index
dataDf['YearMonth'] = dataDf['YearMonth'].dt.strftime('%Y%m');
monthData=dataDf.groupby('YearMonth').agg({'Prices':'max'})
monthData.to_csv(os.path.join(os.getcwd(),'stocks','data', 'usd_index_history_month.csv'))


plt=monthData.plot(figsize=(20, 10))
plt.axhline(monthData['Prices'].mean(), color= 'green', linewidth=1)
plt.legend(['USD', 'Mean'])
plt.set_ylabel('USD Index')
plt.set_xlabel('Time Line')
fig=plt.get_figure()
fig.savefig(os.path.join(os.getcwd(),'stocks','data', 'USD-Index-History-{}-{}.png'.format('195407', '202307')))


plt.close()
