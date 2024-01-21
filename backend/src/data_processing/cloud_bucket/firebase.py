import os
import firebase_admin
import pandas as pd
import tensorflow as tf
import pickle
from firebase_admin import storage
from src.data_processing.cloud_bucket.config import load_credentials
from src.data_processing.cloud_bucket.constants import (
    DEFAULT_BUCKET_NAME,
    DEFAULT_TEMP_FILENAME,
    DEFAULT_RAW_DATA_BLOB,
    DEFAULT_EXTENDED_FEATURE_BLOB,
    DEFAULT_MODEL_DATA_URI,
    DEFAULT_MODEL_DATA_BLOB,
)


class FireBase:
    def __init__(self, ticker_symbol):
        self._cred = load_credentials()
        if not firebase_admin._apps:
            self._app = firebase_admin.initialize_app(
                self._cred,
                {"storageBucket": DEFAULT_BUCKET_NAME},
            )
        self._ticker_symbol = ticker_symbol
        self._bucket = storage.bucket()

    def _upload_file(
        self, blobname, filename=DEFAULT_TEMP_FILENAME, extension="csv", type="data"
    ):
        """

        :param blobname: filepath in the firebase
        :param filename: temp filepath in the project
        :param extension: temp file extension
        :param type: type of the data stored in the temop file. Example data, model etc.
        :return: bool file upload status
        """
        filename = filename.format(self._ticker_symbol, type, extension)
        uploaded = False
        try:
            blob = self._bucket.blob(blobname.format(self._ticker_symbol))
            blob.upload_from_filename(filename)
            # TODO change logging
            print(
                "{} file has been uploaded to firebase successfully".format(
                    extension.upper()
                )
            )
            uploaded = True
        except Exception as e:
            # TODO change logging
            print(e)
        finally:
            try:
                if os.path.exists(filename):
                    os.remove(filename)
            except Exception as e:
                # TODO change logging
                print(e)

        return uploaded

    def _get_data_from_cloud(self, filepath, extension="csv", type="data"):
        data = None
        local_filepath = DEFAULT_TEMP_FILENAME.format(
            self._ticker_symbol, type, extension
        )
        try:
            print(filepath)
            blob = self._bucket.blob(filepath)
            print(blob)

            blob.download_to_filename(local_filepath)
            if extension == "csv":
                data = pd.read_csv(local_filepath)
                print("Inside the wrong one")
            elif extension == "h5":
                print("Inside the right one")
                # with open(local_filepath, "rb") as model_file:
                #     data = pickle.load(model_file)
                data = tf.keras.models.load_model(
                    local_filepath, custom_objects={"Adam": tf.keras.optimizers.Adam}
                )
                print(data)

        except Exception as e:
            # TODO change logging
            print(e)
            return None

        finally:
            try:
                if os.path.exists(local_filepath):
                    os.remove(local_filepath)
            except Exception as e:
                # TODO change logging
                print(e)
            return data

    def upload_raw_csv(self):
        return self._upload_file(DEFAULT_RAW_DATA_BLOB.format(self._ticker_symbol))

    def upload_extended_feature_csv(self):
        return self._upload_file(
            DEFAULT_EXTENDED_FEATURE_BLOB.format(self._ticker_symbol)
        )

    def upload_trained_model(self, model_name="lstm"):
        return self._upload_file(
            DEFAULT_MODEL_DATA_BLOB.format(model_name, self._ticker_symbol),
            extension="h5",
            type="model",
        )

    def get_raw_data(self):
        return self._get_data_from_cloud(
            DEFAULT_RAW_DATA_BLOB.format(self._ticker_symbol)
        )

    def get_extended_feature_data(self):
        return self._get_data_from_cloud(
            DEFAULT_EXTENDED_FEATURE_BLOB.format(self._ticker_symbol)
        )

    def get_trained_model(self, model_name="lstm"):
        return self._get_data_from_cloud(
            DEFAULT_MODEL_DATA_BLOB.format(model_name, self._ticker_symbol),
            extension="h5",
        )
