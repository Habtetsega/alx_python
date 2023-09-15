#!/usr/bin/python
if _name_=="_main":
    import sys
    c = len(sys.args)-1
    if c==0:
        print("0 argument.")
    else :
        print("{} arguments.\n".format(c))
        for i in range(1:c+1):
            print("{}: {} \n".format(i,sys.args[i]))
