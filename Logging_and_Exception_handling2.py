import logging
logging.basicConfig(filename = "test4.log", level = logging.DEBUG, format= '%(levelname)s %(asctime)s %(name)s %(message)s')
try:
    logging.info("We are trying to read file")
    with open ("akriti.txt", 'r'):
        logging.info("Successfully read file")
except Exception as e:
    logging.critical("this is a critical situation")
    logging.error(e)