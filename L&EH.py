import logging

logging.basicConfig(filename= 'L&EH.log', level= logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

try:
    n = int(input("Enter any number: "))
    logging.info("Number entered by user is %S ", n)
    logging.info("We will enter into for loop now")
    for i in range(1,11):
        product = n*i
        print(n,"X", i,"=",product)
    logging.info("we are multiplying user input = %s with each number in range of 1 to 10", n)
except Exception as e:
    print(e)