import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger('myapp')
        self.hdlr = logging.FileHandler('./tests.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.hdlr.setFormatter(formatter)
        self.logger.addHandler(self.hdlr)
        self.logger.setLevel(logging.WARNING)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
