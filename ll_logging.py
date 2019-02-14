#! /usr/bin/env python3

import logging

def usefulFunction():
    logging.warning("This is a warning message")
    return

datestr = "%m/%d/%Y %H:%M:%S %p"
fmtstr = "%(asctime)s %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
logging.basicConfig(level=logging.DEBUG, 
                    filename="output.log",
                    filemode="w",
                    format=fmtstr,
                    datefmt=datestr)

logging.debug("This is a debug message")

logging.info("This is a message with {} content.".format("variable"))

logging.info("This is an info message")

logging.warning("This is a warning message")

usefulFunction()

logging.error("This is an error message")

logging.critical("This is a critical message")