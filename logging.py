import logging
logging.basicConfig(filename="test.log", level=logging.INFO)
logging.info("This is mt first logging code")
logging.warning("This will show a warning message")
logging.error("this is Error message for user")
l=[1,2,3,4,5,6]
for i in l:
    if i==2:
        logging.info(l)
        logging.warning("Warning that user have found 2 in list")
logging.shutdown()

