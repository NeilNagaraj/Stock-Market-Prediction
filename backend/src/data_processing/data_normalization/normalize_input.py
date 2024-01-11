from backend.src.data_processing.data_load.load_stock_data import get_stock_data
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


class Normalize:
	def __init__(self, ticker_symbol):
		self._ticker_symbol = ticker_symbol

	def min_max_normalize(self):
		stock_data = get_stock_data(self._ticker_symbol)
		stock_data_columns = stock_data.columns
		stock_data_cleaned = stock_data.dropna().filter(stock_data_columns[5:])
		scaler = MinMaxScaler(feature_range=(0, 1))

		stock_data_normalized = scaler.fit_transform(stock_data_cleaned)
		return stock_data_normalized, scaler


