price = [
          [56,56,34,287,8],
          [6,76,56,344,788],
          [1,45,65,56,56,],
          [23,5,4,56,244,5],
          [3,54,65,46,46,6]    
]
#print(price)
#print(price[0:3])
#print(price[0][3])
#print(price[3][3])
#print(price[2][2:4])
"""
max = price[0][0] 
for x in price:
    for i in x:
        print(i)  
"""
"""
i = 1
for l in price:
    #print(p)
    sum = 0
    for p in l:
        sum = sum + p
    l.append(sum)
    i = i + 1    
print(price)
              """
"""
l = [12,45,34,23,67,58,67,54,]
evenl = []
for x in l:
    if x % 2 == 0:
        evenl.append(x)
print(evenl)                  

# extract odd list for a list
lst = [23,646,24,464,21,32,53,46,78]
oddlst = []
for x in lst:
    if x % 2 != 0:
        oddlst.append(x)
        
print(oddlst)        

"""
# how to print less one
"""
x = 34
y = 24

if (x < y): z = x
else:
    z = y
print(z)

# how to print greater one
x = 34
y = 24
if (x > y): z = x
else:
    z = y
print(z)

# short term
z = x if x < y else y
print(z)
"""
"""
lst = []
for x in "amaan":
    if x not in "aeiou":
     lst.append(x)
print(lst)

"""

lst = [ True for x in "amaan" if True]
print(lst)

lst = [32,54,61,31,541,24,657,89,51]
even = [ 'amaan' for x in lst if x % 2 == 0 ]
print(even)