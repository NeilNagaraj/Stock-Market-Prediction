import os
import firebase_admin
import pandas as pd
from firebase_admin import storage
from backend.src.data_processing.cloud_bucket.config import load_credentials
from backend.src.data_processing.cloud_bucket.constants import DEFAULT_BUCKET_NAME, DEFAULT_TEMP_FILENAME, \
	DEFAULT_RAW_DATA_BLOB, DEFAULT_EXTENDED_FEATURE_BLOB


class FireBase:
	def __init__(self, ticker_symbol):
		self._cred = load_credentials()
		if not firebase_admin._apps:
			self._app = firebase_admin.initialize_app(self._cred,
			                                          {'storageBucket': DEFAULT_BUCKET_NAME},
			                                          )
		self._ticker_symbol = ticker_symbol
		self._bucket = storage.bucket()

	def upload_file(self, blobname, filename=DEFAULT_TEMP_FILENAME):
		"""

		:param blobname: filepath in the firebase
		:param filename: temp CSV filepath in the project
		:return: bool file upload status
		"""
		try:
			blob = self._bucket.blob(blobname.format(self._ticker_symbol))
			blob.upload_from_filename(filename)
			# TODO change logging
			print("CSV file has been uploaded to firebase successfully")
			return True
		except Exception as e:
			# TODO change logging
			print(e)
			return False

	def get_data_from_csv(self, filepath):
		data = None
		try:
			blob = self._bucket.blob(filepath)
			blob.download_to_filename(DEFAULT_TEMP_FILENAME)
			data = pd.read_csv(DEFAULT_TEMP_FILENAME)

		except Exception as e:
			# TODO change logging
			print(e)
			return None

		finally:
			try:
				if os.path.exists(DEFAULT_TEMP_FILENAME):
					os.remove(DEFAULT_TEMP_FILENAME)
			except Exception as e:
				# TODO change logging
				print(e)
			return data

	def upload_raw_csv(self):
		return self.upload_file(DEFAULT_RAW_DATA_BLOB.format(self._ticker_symbol))

	def upload_extended_feature_csv(self):
		return self.upload_file(DEFAULT_EXTENDED_FEATURE_BLOB.format(self._ticker_symbol))

	def get_raw_data(self):

		return self.get_data_from_csv(DEFAULT_RAW_DATA_BLOB.format(self._ticker_symbol))

	def get_extended_feature_data(self):
		return self.get_data_from_csv(DEFAULT_EXTENDED_FEATURE_BLOB.format(self._ticker_symbol))
