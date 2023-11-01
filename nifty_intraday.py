import yfinance as yf
import pandas as pd
import datetime

# tod = datetime.datetime.now()
# d = datetime.timedelta(days=5)
# start_date = tod-d
# end_date = tod

nifty50_tickers = ['^NSEI']

data = yf.download(tickers=nifty50_tickers, period="5d", interval="15m")

data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
data.index.name = 'timestamp'
# print(data.index)

filtered_data = data.loc[(data.index.time == pd.to_datetime('09:15:00').time()) | 

                           (data.index.time == pd.to_datetime('09:30:00').time()) | (data.index.time == pd.to_datetime('15:00:00').time()) | (data.index.time == pd.to_datetime('15:15:00').time())]

filtered_data = filtered_data[[ 'Open', 'Close']]
filtered_data.columns = ['Opening', 'Closing']

print(data.head)
print(filtered_data)


filtered_data.to_csv('nifty50_intraday_stock_data.csv')