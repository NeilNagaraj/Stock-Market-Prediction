from src.data_processing.data_load.load_stock_data import get_stock_data
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


class NormalizeLoadDataException(Exception):
    def __init__(self):
        pass


class Normalize:
    def __init__(self, ticker_symbol, recent=14, stock_data=None):
        self._ticker_symbol = ticker_symbol
        self._recent = recent

        if stock_data is None:
            try:
                self._stock_data = get_stock_data(self._ticker_symbol, keep=False)

                self._stock_data_columns = self._stock_data.columns
                self._stock_data = self._stock_data.dropna().filter(
                    self._stock_data_columns[5:]
                )

            except Exception as e:
                raise NormalizeLoadDataException(
                    "Error while getting stock data:\t" + e
                )
        else:
            self._stock_data = stock_data

    @property
    def stock_data(self):
        return self._stock_data

    def min_max_normalize(self, get_recent=False):
        if get_recent:
            self._stock_data = self._stock_data[-self._recent :]
        scaler = MinMaxScaler(feature_range=(0, 1))

        stock_data_normalized = scaler.fit_transform(self._stock_data)
        return stock_data_normalized, scaler
