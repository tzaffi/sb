import logging, time, random

logging.basicConfig(filename='logfile.txt', level=logging.DEBUG)

n = 1
while True:
    rc = random.choice(['hello', 'hola', 'hi', 'howdy'])
    logging.debug(rc)
    print(n, "rc: ", rc)
    n += 1
    time.sleep(1)

                  
