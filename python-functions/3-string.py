def reverse_string(string):
     rev=""
     for i in range (len(string)-1,-1,-1):
	     rev += string[i]
     return rev
