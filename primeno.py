def prime_number(n):
    i = 2
    Flag = True
    while i < n:
         if n % i == 0:
            
            Flag = False
            break
         i = i + 1
    if Flag == True:
     print(n,"is prime")
    else:
     print(n,"is not prime")    
  

