import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL) # added this later to disable except for critical

print('Enter the first number:')
first = input()
print('Enter the second number:')
logging.debug(type(first))
second = input()
logging.debug(type(second))
print('the sum of ', first, ' and', second,
      ' is ', (first+second))
