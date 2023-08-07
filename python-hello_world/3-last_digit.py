#!/usr/bin/python3
num=int(input())
_dig=num-(int(num/10)*10)
try:
    if _dig >5:
        print ("Last digit of ",num," is ",_dig," and is greater than 5")
    elif _dig == 0:
        print ("Last digit of ",num," is ",_dig," and is 0")
    else:
        print("Last digit of ",num," is ",_dig," and is less than 6 and not 0")
except:
    print("TypeError")

