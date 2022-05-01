"""
It is used to read the config from environment
"""

import os


class ConfigReader:

    @staticmethod
    def read_config_parameter(key):
        return os.environ[key]
