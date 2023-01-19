"""
def sum(a,b,c):
    z = a + b + c
    print(z)
sum(10,29,76)
sum(1012,267,7878)
sum(1012,267,0)

def odd_even(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

odd_even(34)
odd_even(398)
odd_even(391)

def sum(a,b,c):
    z = a + b + c
    return z

s = sum(56, 45, 12) 
print(s)   
s1 = sum(534, 24, 42) 
print(s1)   

def odd_even( n ):
    if n%2 == 0 :
        return True
    else:
 
         return False
print(odd_even(4))         
print(odd_even(45))         


def odd_even( n ):
    if n%2 == 0 :
        return True
 
    return False
print(odd_even(987))         
print(odd_even(498))  

def is_prime(n):
    i = 2
    flag = True
    while i < n:
      if  n % i == 0:
        flag = False
        break
    i = i + 1
    return flag
print(is_prime(31))    
"""
"""

def display_list( l ):
    for x in l:
        print(x)
        
display_list([10, 20, 30, 40])


def chai_lao( x = 1 ):
    print(f"{x} Chai are here")

chai_lao(2)

def display( x , y , z =300 ):
    print(f"x={x}")
    print(f"y={y}")
    print(f"z={z}")
    
display( 10, 20)

def display( x = 1000 , y= 200 , z = 100 ):
    print(f"x={x}")
    print(f"y={y}")
    print(f"z={z}")
    
display(  y = 2, x = 100, z = 200 )

"""
#Keyword Arguments

#def print_no(a,b,c):
#    print(a)
#    print(b)
#    print(c)
#
#print_no(4,67,89)
#print_no(c=4,a=67,b=89)

#Arbitrary Arguments, *args
#the function will receive a tuple of arguments and can access accordingly.
#def test(*no):
#    print(no)
#test(3,4,6)    

#Arbitrary Keyword Arguments, **kwargs
# it gives the dictionary data
#def fun(**no):
#    print(no)
#fun(a=3,b=5,d=9,z=1,)    
#fun(a=5,b=5,d=9,z=1,)    

#Function Recursion

#def print_rec(i):
#    if i <= 5:
#        print(i)
#        print_rec(i+1)
#        return
#    else:
#     return
#print_rec(1)
#print_rec(3)





































