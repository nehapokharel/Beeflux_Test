def aappend(item , lst):
	lst = []
	lst.append(item)
	return lst

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)


/* a =[1], b=[2], c=[3] are printed as output. As the items of the list are assigned 1,2 and 3 accordingly with the empty list each time. The list with the corresponding value is printed. */
