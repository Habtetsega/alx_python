def is_prime(number):
	i=2
	count =0
	for i in range(-9,10):
		if i == 0:
			continue
		if number%i==0:
			count+=1
	i+=1
	if count > 2:
		return False
	else:
		return True
