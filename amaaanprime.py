n = int(input("please enter any no: "))

i = 2

flag = True

while i < n:
    
    if n % i == 0:
        flag = False
        break
    i = i + 1
if flag == True:
    print("no. is prime")   
else:
    print("no is not prime")