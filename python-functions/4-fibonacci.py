def fibonacci_sequence(n):
	fibo=[]
	sum=0
	for i in range(0,n):
		if i<2 :
			fibo.append(i)
		else:
			sum=fibo[i-2]+fibo[i-1]
			fibo.append(sum)
	return fibo
