for i in range(0,10):
            for j in range(0,10):
                    if i==8 and j==9:   
                        print("{}{} ".format(i,j),end="")
                    elif i<j :
                            print("{}{}, ".format(i,j),end="")
