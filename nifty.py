import yfinance as yf
import pandas as pd
from datetime import date, timedelta

nifty_50_ticker = ["ADANIPORTS", "ASIANPAINT", "AXISBANK", "BAJAJ-AUTO"]

period = "5d"
interval = "15m"


nifty50_df = pd.DataFrame()
nifty50_df = {}

for i in nifty_50_ticker:
        item = i+".NS"
        nifty50_df[item] = yf.download(tickers=item, period=period, interval=interval)

print(nifty50_df['ADANIPORTS'+'.NS'].round(2))
print(nifty50_df['ADANIPORTS'+'.NS'].columns)

# start_time1 = "09:15:00"
# end_time1 = "09:30:00"

# start_time2 = "15:45:00"
# end_time2 = "16:00:00"

# nifty50_extracted_df = pd.DataFrame()


# nifty50 = yf.Ticker('TATASTEEL.NS')

# history = nifty50.history(start="2023-10-10", end="2023-10-17", interval='15m', actions=False)
# history_df = pd.DataFrame(history)
# print(history_df.columns)
# # history_df.to_excel('nifty.xlsx', index=False)
# data = yf.download("^NSEI ^NSEBANK", period="ytd",
#         group_by='ticker', actions=False)

# nifty=data["^NSEI"]
# print(nifty.head())
# nifty.to_csv('nifty.csv')

# # print(nifty50)

