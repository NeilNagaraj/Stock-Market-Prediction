def extract_sdmi_pos_n_neg(stock_data):
	stock_data["SDMI+"] = stock_data["SmoothDI+"]
	stock_data["SDMI-"] = stock_data["SmoothDI-"]
	stock_data.drop(["SmoothDI+", "SmoothDI-"], axis=1, inplace=True)
	return stock_data


def extract_ma7(stock_data, window=10):
	stock_data['MA7'.format(str(window))] = stock_data['Adj Close'].rolling(window).mean()
	return stock_data
