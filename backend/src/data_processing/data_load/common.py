import os
import pandas as pd

from backend.src.data_processing.cloud_bucket.constants import DEFAULT_TEMP_FILENAME
from backend.src.data_processing.cloud_bucket.firebase import FireBase
from backend.src.data_processing.data_load.data_load_exceptions import DataUploadException



def upload_df_as_csv(df, ticker_symbol, type="raw"):
    file = pd.DataFrame(df)
    file.to_csv(DEFAULT_TEMP_FILENAME.format(ticker_symbol))
    f = FireBase(ticker_symbol)

    upload = False
    if type == "raw":
        upload = f.upload_raw_csv()
    elif type == "extended":
        upload = f.upload_extended_feature_csv()

    if not upload:
        raise DataUploadException(ticker_symbol)
    try:
        if os.path.exists(DEFAULT_TEMP_FILENAME):
            os.remove(DEFAULT_TEMP_FILENAME)
    except Exception as e:
        # TODO change logging
        print(e)


