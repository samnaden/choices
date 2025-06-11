import logging
import os
import time

fmt = "%(asctime)s %(levelname)-8.8s %(thread)d %(module)-25.25s:%(lineno)-5.5s %(message)s"
formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S.%fZ")
formatter.converter = time.gmtime

logger = logging.getLogger()
logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
