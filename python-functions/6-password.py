def validate_password(password):
	small=0
	big=0
	num=0
	space=0
	for j in range(97,123):
		i=chr(j)
		if i in password:
			small+=1
	for j in range(65,91):
		i=chr(j)
		if i in password:
			big+=1
	for j in range(1,10):
		i=str(j)
		if i in password:
			num+=1
	for i in password:
		if i==" ":
			space+=1
	if small !=0 and big !=0 and num!=0 and space==0:
		return True
	else:
		return False
