def aappend(item , lst):
	return lst.append(item)

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)


/* a and c will print the value None is the return value of the function aapend as it will return nothing the None is printed. b will given an error as the value of a is nothing it will give a NoneType  error as the value of a is assigned to b and will print none. */


