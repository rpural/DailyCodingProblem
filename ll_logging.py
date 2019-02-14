#! /usr/bin/env python3

import logging

logging.basicConfig(level=logging.DEBUG, 
                    filename="output.log",
                    filemode="w")

logging.debug("This is a debug message")

logging.info("This is a message with {} content.".format("variable"))

logging.info("This is an info message")

logging.warning("This is a warning message")

logging.error("This is an error message")

logging.critical("This is a critical message")