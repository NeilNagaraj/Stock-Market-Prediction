def extract_sdmi_pos_n_neg(stock_data):
	stock_data["SDMI+"] = stock_data["SmoothDI+"]
	stock_data["SDMI-"] = stock_data["SmoothDI-"]
	stock_data.drop(["SmoothDI+", "SmoothDI-"], axis=1, inplace = True)
	return stock_data
