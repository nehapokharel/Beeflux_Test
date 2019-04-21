class Dog:

    kind = 'canine'         

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')


print(d.kind)
	#output = canine

print(d.type)
	#'Dog' object has no attribute 'type' so it will give an error

print(e.kind)
	#canine

print(e.type)
	#'Dog' object has no attribute 'type' so it will give an error
