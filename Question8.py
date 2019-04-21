def aappend(item , lst):
    lst.append(item)
    return lst

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)

/* a =[1], b=[1,2], c=[3] are printed as output. As the items of the list are assigned 1,2 and 3 accordingly along with the previous values. The list with the corresponding value is printed along with the value appended as case in b. */
