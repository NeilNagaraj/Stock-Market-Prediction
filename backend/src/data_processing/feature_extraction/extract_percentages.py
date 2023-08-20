def extract_roc(stock_data, window=25):
	stock_data['ROC'] = (stock_data['Close'] - stock_data['Close'].shift(window)) / stock_data['Close'].shift(
		window) * 100
	return stock_data


def extract_williams_percentage(stock_data, window=14):
	# Calculate the Highest High and Lowest Low over the specified period
	stock_data['HH'] = stock_data['High'].rolling(window=window).max()
	stock_data['LL'] = stock_data['Low'].rolling(window=window).min()

	# Calculate Williams %R
	stock_data['Williams_%R'] = (stock_data['HH'] - stock_data['Close']) / (stock_data['HH'] - stock_data['LL']) * -100

	# Drop intermediate columns
	stock_data.drop(['HH', 'LL'], axis=1, inplace=True)
	return stock_data


def extract_stochastic_percentage(stock_data, window=14, smoothing_period=3):
	# Calculate the Lowest Low and Highest High over the specified period
	stock_data['LL'] = stock_data['Low'].rolling(window=window).min()
	stock_data['HH'] = stock_data['High'].rolling(window=window).max()

	# Calculate the Stochastic Oscillator
	stock_data['%K'] = ((stock_data['Close'] - stock_data['LL']) / (stock_data['HH'] - stock_data['LL'])) * 100

	# Calculate the %D, which is a smoothed version of %K (often a moving average of %K)

	stock_data['%D'] = stock_data['%K'].rolling(window=smoothing_period).mean()

	# Drop intermediate columns
	stock_data.drop(['LL', 'HH'], axis=1, inplace=True)
	return stock_data
