#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
_dig=num-(int(num/10)*10)
try:
    if num==98:
        print ("Last digit of ",num," is ",_dig," and is greater than 5")
    elif _dig == 0:
        print ("Last digit of ",num," is ",_dig," and is 0")
    else:
        print("Last digit of ",num," is ",_dig," and is less than 6 and not 0")
except:
    print("TypeError")

