from keras.models import Sequential
from keras.layers import Dense, LSTM



def train_lstm(x_train, y_train,batch_size=32, epochs=25):
	# Build the LSTM model

	model = Sequential()
	model.add(LSTM(128, return_sequences=True, input_shape=(x_train.shape[1], 1)))
	model.add(LSTM(64, return_sequences=False))
	model.add(Dense(25))
	model.add(Dense(27))

	# Compile the model
	model.compile(optimizer='adam', loss='mean_squared_error')

	# Train the model
	model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)
	print(repr(model))
	return model



