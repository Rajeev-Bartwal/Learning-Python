from logger import logging

def add(a,b):
  logging.debug("THE ADDTION FUNCTION")
  return a+b

logging.debug("the addition function is called")
print(add(4,6))

