import logging
logging.basicConfig(filename = "test3.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s ,%(message)s')

def divide(a,b):
    logging.info("The number entered by user is %s and %s", a,b)
    try:
        logging.info("we are into the function")
        div = a/b
        logging.info("we have completed division")
        logging.info("result of the code is : %s", div)
        return div
    except Exception as ZeroDivisionError:
        logging.exception("User has entered denominator as Zero")
print(divide(3,0))
#DEBUG- 10
#INFO-20
#WARNING-30
#ERROR-40
#CRITICAL-50x


#ERROR-
