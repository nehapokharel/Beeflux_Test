file1 = open("Bee.txt","w") 

l=["python test \n"]
file1.writelines(l) 
 
file1.close() 

file1 = open("Bee.txt","r+") 

print ("Message is:")
print (file1.read() )
print()
file1.close()
