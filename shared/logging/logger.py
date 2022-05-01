"""Module for logging purposes
    """
import logging

# from shared.constant.config_keys import ConfigKey
from shared.logging.logging_properties import LoggingProperties
# from opencensus.ext.azure.log_exporter import AzureLogHandler, AzureEventHandler
from injector import singleton, inject

from shared.reader.config_reader import ConfigReader


@singleton
class Logger:
    """ Class for logging messages
    """

    @inject
    def __init__(self, log_instrumentation_key: str = None):
        # logging.basicConfig(format='%(asctime)s:level=%(levelname)s:%(message)s')
        logger = logging.getLogger(__name__)
        try:
            log_level = ConfigReader.read_config_parameter("log_level")
            if log_level.casefold() == "info":
                log_level = logging.INFO
            elif log_level.casefold() == "debug":
                log_level = logging.DEBUG
            elif log_level.casefold() == "error":
                log_level = logging.ERROR
            elif log_level.casefold() == "warning":
                log_level = logging.WARNING
        except KeyError:
            log_level = logging.ERROR
        logger.setLevel(level=log_level)
        self._logger = logger

    def info(self, message):
        """Method to log info message
        :param message: string
        :return: None
        """
        self._logger.info(message)

    def error(self, message):
        """Method to message as error

        :param message: string
        :return: None
        """
        self._logger.error(message, exc_info=True)

    def debug(self, message):
        """Method to debug message
        :param message: string
        :return: None
        """
        self._logger.debug(message, exc_info=True)


