import numpy as np

from src.config_reader.config_reader import ConfigReader
from src.data_processing.data_normalization.normalize_input import Normalize


def extract_training_test_data(ticker_symbol):
	config = ConfigReader().get()
	train_set_ratio = float(config["train_model"]["train_set_ratio"])
	sequence_len = int(config["train_model"]["sequence_len"])

	data_set, scaler = Normalize(ticker_symbol).min_max_normalize()
	training_data_len = int(np.ceil(len(data_set) * train_set_ratio))
	train_data = data_set[0:int(training_data_len), :]
	# Split the data into x_train and y_train data sets
	x_train = []
	y_train = []

	for i in range(sequence_len, len(train_data)):
		x_train.append(train_data[i - sequence_len:i, 0])
		y_train.append(train_data[i, 0])
		if i <= sequence_len + 1:
			print(x_train)
			print(y_train)
			print()

	# Convert the x_train and y_train to numpy arrays
	x_train, y_train = np.array(x_train), np.array(y_train)

	# Reshape the data
	x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

	test_data = data_set[training_data_len - sequence_len:, :]
	x_test = []
	y_test = data_set[training_data_len:, :]
	for i in range(sequence_len, len(test_data)):
		x_test.append(test_data[i - sequence_len:i, 0])

	# Convert the data to a numpy array
	x_test = np.array(x_test)

	# Reshape the data
	x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
	return x_train, y_train, x_test, y_test, scaler
