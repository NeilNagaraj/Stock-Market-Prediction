from backend.src.data_processing.data_load.load_stock_data import get_stock_data
from backend.src.data_training.extract_training_set import extract_training_test_data
from backend.src.data_training.train_lstm import train_lstm
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics


def test_lstm(ticker_symbol):
	x_train, y_train, x_test, y_test, scaler = extract_training_test_data(ticker_symbol)
	model = train_lstm(x_train, y_train)

	predictions = model.predict(x_test)
	predictions = scaler.inverse_transform(predictions)

	stock_data = get_stock_data(ticker_symbol)
	stock_data = stock_data.dropna()

	training_data_len = int(np.ceil(len(stock_data) * .95))
	train = stock_data[:training_data_len]
	valid = stock_data[training_data_len:]

	pred_close = []
	for pred in predictions:
		pred_close.append(pred[0])
	#
	pred_close = np.array(pred_close)
	# valid["p_trend"] = pred_close
	# valid["trend"] = valid["SDMI+"] > valid["SDMI-"]
	valid["Predictions"] = pred_close
	print(valid)
	valid["trend"] = valid["Close"] > valid["Close"].shift(1)
	valid["p_trend"] = valid["Predictions"] > valid["Predictions"].shift(1)
	plt.figure(figsize=(16, 6))
	plt.title('Model')
	plt.xlabel('Date', fontsize=18)
	plt.ylabel('Close Price USD ($)', fontsize=18)
	plt.plot(train['Close'])
	plt.plot(valid[['Close', 'Predictions']])
	plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
	plt.show()

	accuracy = metrics.accuracy_score(y_true=valid["trend"], y_pred=valid["p_trend"])
	# rmse = np.sqrt(np.mean(((valid["p_trend"] - valid["trend"]) ** 2)))
	# return rmse

	return accuracy


#
print(test_lstm('BLK'))
# # print(rmse)
