import yfinance as yf
import pandas as pd

start_date = '2023-10-16'
end_date = '2023-10-20'

nifty50_tickers = ['ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS']

data = yf.download(nifty50_tickers, start=start_date, end=end_date, interval='15m')

data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
data.index.name = 'timestamp'

filtered_data = data.loc[(data.index.time == pd.to_datetime('09:15:00').time()) | 

                           (data.index.time == pd.to_datetime('09:30:00').time()) | (data.index.time == pd.to_datetime('15:00:00').time()) | (data.index.time == pd.to_datetime('15:15:00').time())]

print(data.head)
print(filtered_data)


filtered_data.to_csv('nifty50_intraday_stock_data.csv')