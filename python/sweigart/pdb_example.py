import logging
logging.basicConfig(level=logging.DEBUG)

print('Enter the first number:')
first = input()

import pdb; pdb.set_trace()

print('Enter the second number:')
logging.debug(type(first))
second = input()
logging.debug(type(second))
print('the sum of ', first, ' and', second,
      ' is ', (first+second))
