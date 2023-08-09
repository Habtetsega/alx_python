#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
_dig=num-(int(num/10)*10)
try:
    if num<5:
        print ("Last digit of {} is {} and is greater than 5".format(num,_dig))
    elif _dig == 0:
        print ("Last digit of {} is {} and is 0".format(num,_dig))
    else:
        print("Last digit of {} is {} and is less than 6 and not 0".format(num,_dig))
except:
    print("TypeError")

