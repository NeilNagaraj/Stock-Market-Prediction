from src.data_processing.data_load.stock_info import STOCK_INFO


class DataDownloadException(Exception):
    def __init__(self, ticket_symbol):
        self._ticker_symbol = ticket_symbol

    def __str__(self):
        return "Failed to Download data for {}".format(STOCK_INFO[self._ticker_symbol])


class DataUploadException(Exception):
    def __init__(self, ticket_symbol):
        self._ticker_symbol = ticket_symbol

    def __str__(self):
        return "Failed to Upload CSV file to firebase for {}".format(
            STOCK_INFO[self._ticker_symbol]
        )
