"""i = 0
while i < 10:
    print(i)
    i = i + 1
else:
    print("false")    """

"""
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j,end = ' ')
        j = j + 1
    i = i + 1
    print()         
    
"""i = 0
while i <= 10:
    j = 0
    while j <= i:
        print(j,end =' ')
        j = j+1
    i = i + 1
    print()    
"""
#i = 1
"""while i <= 10:
    j = 1
    while j <= i:
        print("*",end =' ')
        j = j+1
    i = i + 1
    print()
"""

"""i = 1
while i <= 5 :
   print('*'*i, end = ' ')    
   i = i + 1
   print()
"""

"""i = 1
while i <= 20:
    print("#"' '*i, end =' ')
    i = i + 1
    print()
"""
# 1 to 100 sum

"""i = 1
sum = 0
while i <= 100:
    print(i,end =" + ")
    sum = sum + i
    i = i + 1
print(" =",sum)    
"""
"""
# 1 to 100 even no sum
i = 2
sum =  0
while i % 2 ==0:
    j = 1
    while j <= 100:
        print(j)
        sum = sum + j
        j = j + 1
    i = i + 1    
print(sum)
"""