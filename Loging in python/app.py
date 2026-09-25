import logging

## Basic Logging settings

logging.basicConfig(
  level = logging.DEBUG,
  format='%(asctime)s-%(name)s-%(levelname)s- %(message)s',
  datefmt= '%y-%m-%d %H:%M:%S',
  handlers=[
    logging.FileHandler("app.log"),
    logging.StreamHandler()
  ]
)

logger = logging.getLogger('AirthematicApp')

def add(a,b):
  result = a+b
  logger.debug(f'Adding : {a} + {b} = {result}')
  return result

def multi(a,b):
  result = a*b
  logger.debug(f'multiplying : {a} * {b} = {result}')
  return result

def sub(a,b):
  result = a-b
  logger.debug(f'subtracting : {a} - {b} = {result}')
  return result

def divide(a,b):
  try:
    result = a/b
    logger.debug(f'deviding : {a} / {b} = {result}')
    return result
  except ZeroDivisionError as ex:
    logger.error(ex)
    return None

add(4,6)
multi(8,7)
divide(9,3)
divide(33,0)
sub(19,5)

