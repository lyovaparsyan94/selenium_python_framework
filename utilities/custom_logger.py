import inspect
import logging


def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler(filename='automation.log', mode='w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                                      datefmt="%m/%d/%Y %I:%M:%S %p")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
