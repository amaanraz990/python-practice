#compile type error
#run time error

 # Exception Handeling
"""
import logging

try:
       
    x = int(input("enter no. :"))
    y = int(input("enter another no. :"))
    z = x/y
    print(z) # run time error (division by 0)

except Exception as e:

    print("Error:", e)    

    logging.basicConfig(filename
                      ='error.log', encoding='utf-8', level=logging.DEBUG)
    logging.exception(e)

"""
# different errors from different blogs 

'''
print("start")
try:
       
    x = int(input("enter no. :"))
    y = int(input("enter another no. :"))
    print("start2")
    z = x/y
    print(z) # run time error (division by 0)
    print(g)
    print("start2") 
except NameError as e :
    print("NameError",e)
  

except ZeroDivisionError as e:
    print("ZeroDivisionError",e)

except Exception as e:
    print("Error",e)


print("end")    '''
'''
import logging

print("start")
try:
       
    x = int(input("enter no. :"))
    y = int(input("enter another no. :"))
    print("start2")
    z = x/y
    print(z) # run time error (division by 0)
  
    print("start2") 
except NameError as e :
    print("NameError",e)
    logging.basicConfig(filename
                      ='NameEroor.log', encoding='utf-8', level=logging.DEBUG)
    logging.exception(e)

  

except ZeroDivisionError as e:
    print("ZeroDivisionError",e)
    logging.basicConfig(filename
                      ='Divission by zero eroor.log', encoding='utf-8', level=logging.DEBUG)
    logging.exception(e)

except IndentationError as e:
    print("IndentationError",e)

    logging.basicConfig(filename
                      ='IndentationError.log', encoding='utf-8', level=logging.DEBUG)
    logging.exception(e)

except Exception as e:

    print("Error",e)
    logging.basicConfig(filename
                      ='other error.log', encoding='utf-8', level=logging.DEBUG)
    logging.exception(e)

else:
                      #if there is no error in code the else body exicuted
    print("else  blog")

finally:

    print("finally will exicuted any how")

'''

print("start")
try:
       
    x = int(input("enter no. :"))
    y = int(input("enter another no. :"))
    if x == y:
        raise Exception("y is equal to x")
    print("start2")
    z = x/y
    print(z) # run time error (division by 0)
    print(g)
    print("start2") 
except NameError as e :
    print("NameError",e)
  

except ZeroDivisionError as e:
    print("ZeroDivisionError",e)

except Exception as e:
    print("Error",e)