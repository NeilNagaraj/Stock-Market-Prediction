from datetime import datetime
from src.predict_data.predict import Predict
from src.data_training.train_model import TrainModel
from src.update_model.update_stock_data import UpdateStockData


#
# u = UpdateStockData(ticker_sym="BLK")
# u.update_data()
# #
# t = TrainModel("SBIN.NS")
# t.train_lstm()

#
column_names = [
    "Close",
    "Adj Close",
    "Volume",
    "MA30",
    "EMA100",
    "Upper_Band",
    "Lower_Band",
    "ATR",
    "ADX",
    "ROC",
    "Williams_%R",
    "%K",
    "%D",
    "CCI",
    "RSI",
    "MACD",
    "MACDS",
    "MACDH",
    "AR_12",
    "AR_26",
    "BR",
    "BR_12",
    "BR_26",
    "VR_12",
    "VR_26",
    "SDMI+",
    "SDMI-",
    "MA7",
]
p = Predict("BLK")
stock_data_list = p.get_data(period=7)
prediction_list = []
for stock_data in stock_data_list:
    prediction_dict = dict()
    stock_data_map_list = list(zip(column_names, stock_data[0]))
    # print(stock_data_map_list)
    # for stock_data_map in stock_data_map_list:
    #     print
    prediction_dict.update(stock_data_map_list)
    prediction_list.append(prediction_dict)


print(prediction_list)
