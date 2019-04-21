def sqt(x):
	try:
		x = x**(.5)
	except ValueError:
		x ="The entered value must be either int or float"
		return x

print(sqt(25))  	
