from datetime import datetime
import pandas as pd
import os
from src.data_processing.cloud_bucket.firebase import FireBase
from src.data_processing.feature_extraction.extract_all import ExtractFeatures
from src.data_processing.data_load.stock_data import StockDataLoad
from src.data_processing.data_load.common import DEFAULT_TEMP_FILENAME


def get_stock_data(ticker_symbol, raw=False, keep=False):
	stock_data = None
	try:
		f = FireBase(ticker_symbol)
		if not raw:
			b = f._bucket.blob('extended-feature/{}.csv'.format(ticker_symbol))
		else:
			b = f._bucket.blob('raw-data/{}.csv'.format(ticker_symbol))
		b.download_to_filename(DEFAULT_TEMP_FILENAME)
		stock_data = pd.read_csv(DEFAULT_TEMP_FILENAME)
	except Exception as e:
		# TODO implement logging
		print(e)
	finally:
		if not keep:
			try:
				if os.path.exists(DEFAULT_TEMP_FILENAME):
					os.remove(DEFAULT_TEMP_FILENAME)

			except Exception as e:
				pass
		return stock_data
