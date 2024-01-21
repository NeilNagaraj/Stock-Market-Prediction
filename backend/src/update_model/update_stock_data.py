from src.data_processing.data_load.stock_data import StockDataLoad
from src.data_processing.data_load.stock_info import STOCK_INFO
from src.data_processing.feature_extraction.extract_all import ExtractFeatures
from datetime import datetime
import logging


class UpdateStockDataException(Exception):
    pass


class UpdateStockData:
    def __init__(self, ticker_sym="all"):
        self._stock_tickers = STOCK_INFO
        if ticker_sym == "all":
            self._ticker = None
        else:
            self._ticker = ticker_sym

    def update_data(self, ticker_sym=None):
        if ticker_sym == "all":
            for ticker in self._stock_tickers:
                try:
                    StockDataLoad(
                        ticker, start_date="2012-01-01", end_date=datetime.now()
                    ).upload_raw_data()
                    e = ExtractFeatures(ticker)
                    e.extract_all_features()

                except Exception as e:
                    raise UpdateStockDataException(
                        "Failed to update stock data for {}: {}".format(
                            self._stock_tickers[ticker]["name"], e
                        )
                    )
        else:
            try:
                StockDataLoad(
                    self._ticker, start_date="2012-01-01", end_date=datetime.now()
                ).upload_raw_data()
                e = ExtractFeatures(self._ticker)
                e.extract_all_features()
            except Exception as e:
                raise UpdateStockDataException(
                    "Failed to update stock data for {}: {}".format(
                        self._stock_tickers[self._ticker]["name"], e
                    )
                )
