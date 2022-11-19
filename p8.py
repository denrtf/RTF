import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="simslogs.log",
                    filemode="w",
                    format="We have next massage:%(asctime)s:%(levelname)s:%(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
