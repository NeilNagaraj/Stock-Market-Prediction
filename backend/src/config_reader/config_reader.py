import configparser


class ConfigReader:
    def __init__(self):
        try:
            self._config = configparser.ConfigParser()
        except Exception as e:
            # TODO use logging
            print("Critical Error!!!Failed to Load the property:\t", e)

    def get(self):
        self._config.read(
            "../../settings/config.ini",
        )
        return self._config
