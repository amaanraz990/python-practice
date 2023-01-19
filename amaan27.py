# list practise
'''
M = [23,34,55,66,43,34,]
print(M)
print(type(M))
'''
# if list contain a list it is called nested list
#c = [12,45,45,34,[424,45,45,53,],23,45,56,45,]
'''
print(c)
print(type(c))
print(len(c))
print(c[0])
print(c[2:5])
print(len(c[2:5]))

# another way to create a list

name = list(('amaan','irfan','shamile','sajid')) 
print(name)
print(len(name))
print(len(name[-4:3]))
print(len(name[-4:4]))
print("amaan" in name)
print("amaan" not in name)
print("saif" in name)
print("saif" not in name)
print("sajid" not in name)
print("sajid" in name)

# using for loop in list

for x in M:
    print(M)
'''
"""for x in c:
    print(c)
"""
# using while loop in list
''' = 0
while i < len(c):
    print(i)
    i = i + 1
print("exit")
i = 0
while i < len(c):
    print(c)
    i = i + 1
print("exit")
'''
"""marks = [87,97,67,57,56,43]
max = marks[0]
for x in marks:
    if x > max:
        max = x
print("max marks is ",max)        
# for minimum
marks = [87,97,67,57,56,43]
min = marks[0]
for x in marks:
    if x < min:
        min = x
print("minimum marks is",min)        """

rupees = [12,546,65,77,7,7,5,75533,]
max = rupees[0]
for x in rupees:
    if x > max:
        max = x
print("max rupees is",max)        
