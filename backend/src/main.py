from datetime import datetime

from backend.src.data_processing.feature_extraction.extract_all import ExtractFeatures
from backend.src.data_processing.feature_extraction.extract_averages import extract_ma, extract_ema
from backend.src.data_processing.data_load.stock_data import StockDataLoad

ex_feature = ExtractFeatures("BLK").extract_all_features()
print(ex_feature)