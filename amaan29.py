value = ["amaan",90,"shavan",89,"kashif",98,"false",True,[12,45,67,],"saif",87]
#print(value)
#print(len(value))
#print(value[-8:6])
#print(len(value[-10:9]))#
# we can also change the value of any item of a list like that
#value[3] = "husain"
#value[2] = "rehman"
#print(value)
# append function is used to insert a new item in a list at last
#value.append("raza")
#print(value)
# remove is used to remove a object in a list
#value.remove("shavan")
#print(value)

# insert is used to insert any object by indexing(that place you want to insert)
#value.insert(3, "78")
#print(value)
#value.insert(6#,"husain")
#print(value)

#pop is used to 
#value.pop(2)
#print(value)

# reverse is used to reverse the list
#value.reverse()
#print(value)
 
# copy is used to copy list
x = value.copy()
x = value
print(x)

print(value is x)
#count is for counting the quantity of abject
print(value.count("amaan"))
print(value.count("kashif"))
# extend is used to extend the object we give
value.extend("[amaan]")
print(value)