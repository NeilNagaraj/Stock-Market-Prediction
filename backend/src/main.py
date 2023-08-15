from datetime import datetime

from backend.src.data_processing.feature_extraction.extract_all import ExtractFeatures
from backend.src.data_processing.feature_extraction.extract_averages import extract_ma, extract_ema
from backend.src.data_processing.data_load.stock_data import StockDataLoad




# end = datetime.now()
# start = datetime(end.year - 1, end.month, end.day)
#
# l = LoadData(ticker_symbol="BLK", start_date=start, end_date=end)
# l.load_as_csv
ex_feature = ExtractFeatures("BLK").extract_all_features()
print(ex_feature)