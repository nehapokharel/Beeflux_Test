def aappend(item,lst=[]):
	lst = []
	return lst.append(item)

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)


/* a, b and c will print the value None is the return value of the function aapend as it will return nothing the None is printed. */
