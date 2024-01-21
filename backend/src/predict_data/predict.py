import numpy as np
from src.data_processing.data_normalization.normalize_input import Normalize
from src.data_processing.cloud_bucket.firebase import FireBase
from src.config_reader.config_reader import ConfigReader


class Predict:
    def __init__(self, ticker, period=1):
        self._ticker = ticker
        self._firebase = FireBase(self._ticker)
        self._period = period

    def _get_data(self):
        n = Normalize(self._ticker)
        dataset, scaler = n.min_max_normalize(get_recent=True)
        sequence_len = 14
        print(len(dataset))
        y_predict_list = []
        x_test = []
        for j in range(self._period):
            dataset_readable = n.stock_data
            x_test.append(dataset[-sequence_len:, 0])
            x_test = np.array(x_test)
            print(x_test.shape)
            model = self._firebase.get_trained_model()
            y_predict = model.predict(x_test)
            y_predict_readable = scaler.inverse_transform(y_predict)
            y_predict_list.append(y_predict_readable)
            dataset_readable = np.append(
                dataset_readable, y_predict_readable.reshape(1, -1), axis=0
            )

            n = Normalize(self._ticker, stock_data=dataset_readable)
            dataset, scaler = n.min_max_normalize(get_recent=True)
            x_test = []

        return y_predict_list

    def get_predicted_data(self):
        column_names = (
            ConfigReader().get().get("features", "columns", raw=True).split(",")
        )

        stock_data_list = self._get_data()
        prediction_list = []
        for stock_data in stock_data_list:
            prediction_dict = dict()
            stock_data_map_list = list(zip(column_names, stock_data[0]))
            prediction_dict.update(stock_data_map_list)
            prediction_list.append(prediction_dict)
        return prediction_list
