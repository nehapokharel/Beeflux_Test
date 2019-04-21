class Dog:

    kind = 'canine'         

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

d.kind="white"
d.name="john"
e.name="jonny" 

print(d.kind)
	#white
print(e.kind)
	#canine
print(d.type)
	#'Dog' object has no attribute 'type'
print(e.type)
	#'Dog' object has no attribute 'type'
