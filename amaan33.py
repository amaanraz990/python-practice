#sets{}
#x = {'amaan',23,'laptop',60000,'copy','delhi'}
#print(type(x))
#print(x)
#y = list(x)
#y[0]= 'raza'
#x = set(y)
#print(x)

#for i in x:
#    print(i)
#print('amaan' in x)
#print('laptop' not in x)
"""
roll_no = set((1,2,3,4,5,6,7,8,9))
print(roll_no)
print(type(roll_no)) 
y = list(roll_no)
print(type(y))
y.append(10)
print(y)
y = set(roll_no)
print(type(roll_no))
"""

adhar_no = set(())
while True:
    a = input("please input aadhar no. or 0 to exit:")
    if a == "0":
        break
    adhar_no.add(a)

for x in adhar_no:
    print("10k transfer to",x)  
print(adhar_no)



