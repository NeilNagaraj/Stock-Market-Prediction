from backend.src.data_processing.cloud_bucket.firebase import FireBase
from backend.src.data_processing.data_load.common import upload_df_as_csv
from backend.src.data_processing.data_load.stock_data import StockDataLoad
from backend.src.data_processing.feature_extraction.function_list import extract_function_list


class ExtractFeatures:
	def __init__(self, ticker_symbol):
		self._ticker_symbol = ticker_symbol
		self._raw_data = FireBase(self._ticker_symbol).get_raw_data()
		print(self._raw_data)
		self._extended_feature = self._raw_data

	def extract_all_features(self):
		# load extract feature columns to new csv file
		for extract_feature in extract_function_list:
			self._extended_feature = extract_feature(self._extended_feature)
		upload_df_as_csv(self._extended_feature, self._ticker_symbol, type="extended")
		return self._extended_feature
	


