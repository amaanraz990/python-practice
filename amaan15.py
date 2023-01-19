x = float(input("please enter any no x:"))
y = float(input("please enter any no y:"))
o = (input("please enter operation /,*,+,-: "))
if o == "/":
    print(f"you enter x = {x}")
    print(f"you enter y = {y}")
    print(f"divisoin of x and y =",x/y)
elif o == "*":
    print(f"you enter x = {x}")
    print(f"you enter y = {y}")
    print(f"Multiplication of x and y =",x*y)   

elif o == "+":
    print(f"you enter x = {x}")
    print(f"you enter y = {y}")
    print(f"addition of x and y =",x+y)       

elif o == "-":
    print(f"you enter x = {x}")
    print(f"you enter y = {y}")
    print(f"subtraction of x and y =",x-y)
else:
    print("you entered wrong operations")  
print("thankyou")
print("exit")             