def factor(n):
	for i in range(1,n+1):
		if(n % i == 0):
			print("the factor of "+ str(n) + " are:" + " " + str(i))
n = int(input("Enter a number: "))

factor(n)

