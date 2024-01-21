from src.data_processing.data_load.load_stock_data import get_stock_data
from src.data_training.extract_training_set import extract_training_test_data
from src.data_training.train_model import TrainModel
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics


def test_lstm(ticker_symbol):
	train_model = TrainModel(ticker_symbol)
	x_train, y_train, x_test, y_test, scaler = train_model.x_train, train_model.y_train, train_model.x_test, train_model.y_test, train_model.scaler
	model = train_model.train_lstm()

	predictions = model.predict(x_test)
	predictions = scaler.inverse_transform(predictions)

	stock_data = get_stock_data(ticker_symbol)
	stock_data = stock_data.dropna()

	training_data_len = int(np.ceil(len(stock_data) * .95))

	valid = stock_data[training_data_len:]

	pred_close = []
	for pred in predictions:
		pred_close.append(pred[0])
	pred_close = np.array(pred_close)
	valid["Predictions"] = pred_close

	valid["trend"] = valid["Close"] > valid["MA7"].shift(1)
	valid["p_trend"] = valid["Predictions"] > valid["MA7"].shift(1)

	accuracy = metrics.accuracy_score(y_true=valid["trend"], y_pred=valid["p_trend"])


	return accuracy



print(test_lstm('WIP'))

