a = 200
b = 45
if b > a:
    print("b is greater than a")
else:
    print("b is less than a")

a = 75
b = 464
c = 765
if c>b and b>c:
    print("print if condition are true")
else:
    print("else condition is true")


x = int(input("please input any no less than 10:"))
if x % 2 == 0:
    print("you entered even no")
    print(f"you entered{x}")
else:
    print("you entered a odd no")
    print(f"you entered:+" "+{x}")

x = int(input("please input any no less than 500:"))
if x % 2 == 1:
    print("you entered an odd number")
    print(f"you entered:{x} ")
else:
     print("you entered an even number")
     print(f"you entered:{x} ")

a = float(input("please input the length of the area in sm:"))     
b = float(input("please input the width of the area in sm:")) 
area = a*b
if a == b:
    print("it is a square") 
    print(f"area of a square:",area,"sm")
else:
    print("it is a rectangle") 
    print(f"area of a rectangle :",area,"sm")

vowel = input("please enter any alphabet:")  
if vowel in ("a","e","i","o","u","A","E","I","O","U"):
    print(vowel,"is a vowel")
       
else:
    print(" it is a consonents")

x = int(input("Enter your age: "))
if x >= 18:
    print(f"your age is {x} you are eligable for polling ")
else:
    print(f"your age is {x} you are not eligable for polling ") 


total_marks = float(input("Enter your total marks out of 500: "))
x = total_marks/5
if total_marks >= 165:
    print("you are passed")
    print(f"you got {x} %")
else:
    print("you are failed")
    print(f"you got {x} %")    
   

     