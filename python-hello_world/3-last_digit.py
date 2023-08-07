#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
last_dig=num%10
if last_dig >5:
    print ("Last digit of ",num," is ",last_dig," and is greater than 5")
elif last_dig == 0:
    print ("Last digit of ",num," is ",last_dig," and is 0")
else:
    print("Last digit of ",num," is ",last_dig," and is less than 6 and not 0")

