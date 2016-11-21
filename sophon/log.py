# encoding: utf-8

import logging


class ConsoleLogger(object):
    def __init__(self):
        formatter = logging.Formatter("[%(asctime)s][%(levelname)s]: %(message)s")

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        self.logger = logging.getLogger("sophon")
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(ch)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
