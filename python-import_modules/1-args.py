#!/usr/bin/python
if _name_ == "_main_" : 
    import sys
    c = len(sys.args)-1
    if c == 0:
        print("0 argument.")
    else :
        print("{} arguments.\n".format(c))
        for i in range(c):
            print("{}: {} \n".format(i+1,sys.args[i+1]))
