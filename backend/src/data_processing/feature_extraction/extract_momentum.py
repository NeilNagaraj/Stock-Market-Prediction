def extract_mad(stock_data):
	df = stock_data
	# Calculate 12-period EMA and 26-period EMA
	df['EMA12'] = df['Close'].ewm(span=12, adjust=False).mean()
	df['EMA26'] = df['Close'].ewm(span=26, adjust=False).mean()

	# Calculate MACD line
	df['MACD'] = df['EMA12'] - df['EMA26']
	df.drop(['EMA12', 'EMA26'], axis=1, inplace=True)
	# Calculate 9-period EMA of MACD to get the signal line
	df['MACDS'] = df['MACD'].ewm(span=9, adjust=False).mean()

	# Calculate MACD histogram
	df['MACDH'] = df['MACD'] - df['MACDS']

	return df


def extract_mtm(stock_data):
	for period in [5, 10, 15]:
		stock_data["MTM_{}".format(str(period))] = stock_data['Close'].diff(period)
	return stock_data
