def extract_autoregression(stock_data):
	stock_data['AR_12'] = stock_data['Close'].shift(12)
	stock_data['AR_26'] = stock_data['Close'].shift(26)
	return stock_data


def extract_value_range(stock_data):
	stock_data['HL_Diff'] = stock_data['High'] - stock_data['Low']
	stock_data['HL_Ratio'] = stock_data['HL_Diff'] / stock_data['Low']
	stock_data['VR_12'] = stock_data['HL_Ratio'].rolling(window=12).mean()
	stock_data['VR_26'] = stock_data['HL_Ratio'].rolling(window=26).mean()
	stock_data.drop(['HL_Diff', 'HL_Ratio'], axis=1, inplace=True)
	return stock_data


def extract_buying_pressure(stock_data):
	stock_data['Range'] = stock_data['High'] - stock_data['Low']
	stock_data['Midpoint'] = (stock_data['High'] + stock_data['Low']) / 2
	stock_data['BR'] = ((stock_data['Close'] - stock_data['Low']) - (stock_data['High'] - stock_data['Close'])) / \
	                   stock_data['Range']

	stock_data['BR_12'] = stock_data['BR'].rolling(window=12).mean()
	stock_data['BR_26'] = stock_data['BR'].rolling(window=26).mean()
	stock_data.drop(['Range', 'Midpoint'], axis=1, inplace=True)
	return stock_data
