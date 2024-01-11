from datetime import datetime

from backend.src.data_processing.cloud_bucket.firebase import FireBase
from backend.src.data_processing.feature_extraction.extract_all import ExtractFeatures
from backend.src.data_processing.feature_extraction.extract_averages import extract_ma, extract_ema
from backend.src.data_processing.data_load.stock_data import StockDataLoad

ex_feature = ExtractFeatures("BLK").extract_all_features()
print(ex_feature)
f = FireBase('BLK')
b = f._bucket.blob('extended-feature/BLK.csv')
b.download_to_filename('temp.csv')