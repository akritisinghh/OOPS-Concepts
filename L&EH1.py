import logging
logging.basicConfig(filename="test1.log", level=logging.DEBUG, format="%(levelname)s %(asctime)s %(name)s %(message)s")

logging.info("We are writing a program to draw a pattern through for loop")
try:
    def pattern(n):
        logging.info("We are drawing a pattern for %s lines",n)
        for i in range(n):
            print((chr(65+i)+" ")*(n-i))
        logging.info("we will draw alphabetical patterns")
    print(pattern(7))
except Exception as e:
    print(e)
    logging.error("user has entered string")
    logging.exception(e)