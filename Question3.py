def student(name, roll, age, address):
    print(name, roll, age, address)


student("pratima", name="pratima", 20, 20, 20)
	# It will show an error as the first argument pratima tries to set as the valueof name but the second argument already assigns value for the argument name as duplicate value for the same argument and the value and the parameter is assigned as name="pratima" and after that the value are only assigned for roll, age and address without defining them so it gives an error "positiobal argument follows keyword argument" 
student("pratima", 20, age=25, "kathmandu")
	# here the age is defined again and value is assigned but in case of address only the value is assigned hence it will also throw an error "positiobal argument follows keyword argument" 
student("pratima")
   # only the value for the name is assigned so it will give an error "student() missing 3 required positional arguments: 'roll', 'age', and 'address'"

