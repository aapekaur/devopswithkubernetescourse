import datetime
import random
import string
import time

length = 64
random_string = "".join(random.choices(string.ascii_letters + string.digits, k=length))

while True:
    print(datetime.datetime.now(), random_string)
    time.sleep(5)
