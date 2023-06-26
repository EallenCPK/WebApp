import requests
import pandas as pd
from datetime import datetime

class Kraken:

    def __init__(self):
        self.ohlc_df = None

    def get_ohlc(self, ticker, interval):
        resp = requests.get('https://api.kraken.com/0/public/OHLC?pair={}&interval={}'.format(ticker, interval))
        json = resp.json()

        df = pd.DataFrame(json['result'][ticker])
        df.columns = ['unixtimestap', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'count']
        df['close'] = pd.to_numeric(df['close'], downcast="float")

        # df["dt"]=pd.to_datetime(df['unixtimestap'])

        self.ohlc_df = df
        return df

    def getMovingAvg(self, ticker, interval, arrMA):
        df = self.ohlc_df
        df.columns = ['unixtimestap', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'count']
        df['close'] = pd.to_numeric(df['close'], downcast="float")

        moving_averages = {}
        for ma in arrMA:
            start_index = 720 - ma
            end_index = 720
            df_ma = df.iloc[start_index:end_index, :]
            moving_averages["ma{}".format(ma)] = df_ma["close"].mean()

        return moving_averages
    
    def getExponentialMovingAvg(self, ticker, interval, arrMA):
        df = self.ohlc_df
        df.columns = ['unixtimestap', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'count']
        df['close'] = pd.to_numeric(df['close'], downcast="float")

        resultDf = pd.DataFrame()

        moving_averages = {}
        for ma in arrMA:
            moving_averages["ema{}".format(ma)] = (df['close'].ewm(span=20, adjust=False).mean()).iat[-1]

        print(moving_averages)