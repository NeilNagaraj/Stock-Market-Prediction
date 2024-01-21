import os
import pandas as pd

from src.data_processing.cloud_bucket.constants import DEFAULT_TEMP_FILENAME
from src.data_processing.cloud_bucket.firebase import FireBase
from src.data_processing.data_load.data_load_exceptions import DataUploadException


def upload_df_as_csv(df, ticker_symbol, type="raw"):
    file = pd.DataFrame(df)
    file.to_csv(DEFAULT_TEMP_FILENAME.format(ticker_symbol, "data", "csv"))
    f = FireBase(ticker_symbol)

    upload = False
    if type == "raw":
        upload = f.upload_raw_csv()
    elif type == "extended":
        upload = f.upload_extended_feature_csv()

    if not upload:
        raise DataUploadException(ticker_symbol)
