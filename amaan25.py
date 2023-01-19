# prime no
n = int(input("please enter any no"))

i = 2

flag = True

while i < n:

    if n % i == 0:
        flag = False
        break
    i = i + 1

if flag == True:
    print("the no. is prime")
else:
    print("the no is not prime")    