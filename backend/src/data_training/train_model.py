from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import tensorflow as tf
import pickle
from src.config_reader.config_reader import ConfigReader
from src.data_processing.cloud_bucket.constants import DEFAULT_TEMP_FILENAME
from src.data_processing.cloud_bucket.firebase import FireBase
from src.data_training.extract_training_set import extract_training_test_data


class TrainModel:
    def __init__(self, ticker_symbol):
        self._ticker_symbol = ticker_symbol
        (
            self.x_train,
            self.y_train,
            self.x_test,
            self.y_test,
            self.scaler,
        ) = extract_training_test_data(self._ticker_symbol)

    def train_lstm(self):
        # Build the LSTM model

        batch_size = int(ConfigReader().get()["train_model"]["batch_size_lstm"])
        epochs = int(ConfigReader().get()["train_model"]["epochs_lstm"])
        model = None
        try:
            model = Sequential()
            model.add(
                LSTM(128, return_sequences=True, input_shape=(self.x_train.shape[1], 1))
            )
            model.add(LSTM(64, return_sequences=False))
            model.add(Dense(25))
            model.add(Dense(28))
            optimizer = tf.keras.optimizers.Adam()
            # Compile the model
            model.compile(optimizer=optimizer, loss="mean_squared_error")

            # Train the model

            model.fit(self.x_train, self.y_train, batch_size=batch_size, epochs=epochs)
        except Exception as e:
            # TODO implement logging
            print("Failed to ")

        # Upload model to cloud
        try:
            filename = DEFAULT_TEMP_FILENAME.format(self._ticker_symbol, "model", "h5")
            # with open(filename, "wb") as model_file:
            #     pickle.dump(model, model_file, protocol=3)
            model.save(filename)
            f = FireBase(self._ticker_symbol)
            f.upload_trained_model("lstm")

        except Exception as e:
            # TODO logging
            print("Couldn't upload model to cloud:\t", e)
        return model
