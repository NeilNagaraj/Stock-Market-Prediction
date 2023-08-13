from datetime import datetime
import numpy as np
import pandas as pd
import yfinance as yf
import logging

class LoadData:
    def __init__(self, ticker_symbol : str, start_date, end_date):
        self._ticker_symbol = ticker_symbol
        self._start_date = start_date
        self._end_date = end_date
    
    def load(self):

        logging.info("Dowloading stock data for {} from {} to {}".format(self._ticker_symbol, self._start_date, self._end_date))
        data = yf.download(self._ticker_symbol, self._start_date,self._end_date)
        return data
    def load_as_csv(self):
        df = self.load()
        file = pd.DataFrame(df)
        file.to_csv("backend/src/data_processing/data_load/data/AAPL.csv")



end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)
LoadData("AAPL", start, end).load_as_csv()

# print(type(l))