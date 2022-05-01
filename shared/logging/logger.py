"""Module for logging purposes
    """
import logging

from injector import singleton, inject

from shared.reader.config_reader import ConfigReader


@singleton
class Logger:
    """ Class for logging messages
    """

    @inject
    def __init__(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.INFO)
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


