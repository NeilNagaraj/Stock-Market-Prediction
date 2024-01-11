import os
from datetime import datetime
import logging
import pandas as pd
import yfinance as yf
from backend.src.data_processing.cloud_bucket.firebase import FireBase
from backend.src.data_processing.data_load.common import upload_df_as_csv
from backend.src.data_processing.data_load.data_load_exceptions import DataDownloadException, DataUploadException


class StockDataLoad:
	def __init__(self, ticker_symbol: str, start_date: datetime, end_date: datetime):
		self._ticker_symbol = ticker_symbol
		self._start_date = start_date
		self._end_date = end_date
		self._data = self.load()

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, data):
		self._data = data

	def load(self):

		logging.info(
			"Dowloading stock data for {} from {} to {}".format(self._ticker_symbol, self._start_date, self._end_date))
		try:
			data = yf.download(self._ticker_symbol, self._start_date, self._end_date)
			return data
		except Exception as e:
			logging.error("Error downloading stock data:\n{}".format(e))
			return None

	def upload_raw_data(self):
		# function to load stocks df to csv

		df = self.data
		if df is None:
			raise DataDownloadException(self._ticker_symbol)
		upload_df_as_csv(df, self._ticker_symbol)




