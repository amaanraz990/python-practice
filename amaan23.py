# for loop
"""
name = "amaan"
for x in name:
    print(x)
"""
"""
str = "python programming"
for x in str:
    if x not in "aeiou":
        print(x)     
"""
"""
for i in range(1,11):
    print(i)


for i in range(0, 50, 5):
    print(i)    
"""
"""
sum = 0
for x in range(1,11):
    print(x ,end = "+")
    sum = sum + x
print("=",sum)    
"""
"""
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j,end = ' ')
        j = j + 1
    i = i + 1 
    print()   
"""
"""
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end = ' ')
    print()
    """
"""
      *
     * *
    *   *
   * * * *
  *       *
 *         *
"""
"""
for i in range(1,7):
    if i == 1:
        print("*".center(12))
    elif i == 2:
        print("* *".center(12))
    elif i == 3:
        print("*   *".center(12))
    elif i == 4:
        print("* * * *".center(12))
    elif i == 5:
        print("*       *".center(12))
    elif i == 6:
        print("*         *".center(12))
print()
"""
""" 
*           * 
* *       * *
*   *   *   * 
*     *     *
*           *
*           *

"""
'''

for i in range(1,7):
    if i == 1:
     print("*           *".center(13))
    elif i == 2:
        print("* *       * *".center(13)) 
    
    elif i == 3:
        print("*   *   *   *".center(13)) 
    
    elif i == 4:
        print("*     *     *".center(13)) 
    
    elif i == 5:
        print("*           *".center(13)) 
    elif i == 6:
        print("*           *".center(13)) 
print()
for i in range(1,7):
    if i == 1:
        print("*".center(12))
    elif i == 2:
        print("* *".center(12))
    elif i == 3:
        print("*   *".center(12))
    elif i == 4:
        print("* * * *".center(12))
    elif i == 5:
        print("*       *".center(12))
    elif i == 6:
        print("*         *".center(12))
print()
for i in range(1,7):
    if i == 1:
        print("*".center(12))
    elif i == 2:
        print("* *".center(12))
    elif i == 3:
        print("*   *".center(12))
    elif i == 4:
        print("* * * *".center(12))
    elif i == 5:
        print("*       *".center(12))
    elif i == 6:
        print("*         *".center(12))
print()
'''
# *        *
# * *      *
# *  *     *
# *    *   *
# *      * *
# *        *
'''
for i in range(1,7):
    if i == 1:
        print("*        *".center(13))
    elif i == 2 :
        print("* *      *".center(13))
    elif i ==3:
        print(" *  *     *".center(13))        
    elif i ==4:
        print("*    *   *".center(13))        
    elif i ==5:
        print("*      * *".center(13))        
    elif i ==6:
        print("*        *".center(13))        
'''
#   * *
# *     *
# *     *
# *     *
#   * * 
'''
h = 5
space = 5
for i in range(1,h+1):
    if i == 1 or i == h:
        print(" "*(h-3)+"* *")
    else:
        print("*"+" "*(h)+"*")
        '''
#* * *
#*   * 
#* * * 
#* 
#*  
'''       
h = 5
cnt_pos = h//2 + 1 
for i in range(1,h+1):
    if i == 1 or i == cnt_pos:
        print("* "*(h-2))
    elif i == 2:
        print("*   *")
    else:
        print("*")    
'''
#* * * *
#*     *
#*     *
#*   * *  
#* * * *
#        *




























