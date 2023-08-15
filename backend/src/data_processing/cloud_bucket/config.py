from firebase_admin import credentials
from backend.src.data_processing.cloud_bucket.constants import DEFAULT_FIREBASE_CONFIG


def load_credentials(filename=DEFAULT_FIREBASE_CONFIG):
	# load firebase credentials
	try:
		cred = credentials.Certificate(filename)
		return cred
	except Exception as e:
		# TODO change logging
		print(e)
