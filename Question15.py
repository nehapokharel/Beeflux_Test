def norm(v1,p,v):
	n =int(input("enter the value of n: "))
	p==2
	for i in range(0,n):
		v += v*((p)**n) 
	print("The value of v in norm form is: " + str(v))
	e = (v1**2 + p**2)**(.5)
	print("the Euclidean norm is: "+ str(e))

v1 = int(input("Enter a value for v1: "))
p = int(input("Enter a value for p: "))
v = int(input("Enter a value for v: "))
norm(v1,p,v)

