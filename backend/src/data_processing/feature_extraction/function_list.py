from backend.src.data_processing.feature_extraction.extract_averages import *
from backend.src.data_processing.feature_extraction.extract_percentages import *

extract_function_list = [
	extract_ma,
	extract_ema,
	extract_bollinger_band,
	extract_atr,
	extract_adx,
	extract_roc,
	extract_williams_percentage,
	extract_stochastic_percentage
]
