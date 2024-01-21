import os
from pathlib import Path

DEFAULT_FIREBASE_CONFIG = os.path.join(
    Path(__file__).parents[3], "config/firebase_config.json"
)
# Data File uploads
DEFAULT_TEMP_FILENAME = "temp_{}_{}.{}"
DEFAULT_BUCKET_NAME = "stocks-feature-info.appspot.com"
DEFAULT_RAW_DATA_BLOB = "raw-data/{}.csv"
DEFAULT_EXTENDED_FEATURE_BLOB = "extended-feature/{}.csv"

# Data File downloads
RAW_DATA_DOWNLOAD_URI = "gs://" + DEFAULT_BUCKET_NAME + "/" + DEFAULT_RAW_DATA_BLOB
EXTENDED_DATA_DOWNLOAD_URI = (
    "gs://" + DEFAULT_BUCKET_NAME + "/" + DEFAULT_EXTENDED_FEATURE_BLOB
)


# Model Uploads
DEFAULT_MODEL_DATA_BLOB = "models/{}/{}.h5"
DEFAULT_MODEL_DATA_URI = "gs://" + DEFAULT_BUCKET_NAME + "/" + DEFAULT_MODEL_DATA_BLOB
