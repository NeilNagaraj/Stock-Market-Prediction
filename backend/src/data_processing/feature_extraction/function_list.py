from src.data_processing.feature_extraction.extract_averages import *
from src.data_processing.feature_extraction.extract_percentages import *
from src.data_processing.feature_extraction.extract_momentum import *
from src.data_processing.feature_extraction.extract_regressive import *
from src.data_processing.feature_extraction.extract_trend import *

extract_function_list = [
	extract_ma,
	extract_ema,
	extract_bollinger_band,
	extract_atr,
	extract_adx,
	extract_roc,
	extract_williams_percentage,
	extract_stochastic_percentage,
	extract_commodity_channel_index,
	relative_strength_index,
	extract_mad,
	extract_autoregression,
	extract_buying_pressure,
	extract_value_range,
	extract_sdmi_pos_n_neg,
	extract_ma7
]
