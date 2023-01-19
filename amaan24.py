'''
* * *
*   *
* * *
*   *
* * *
'''
'''
h = 5
w = 3
center_pos = h//2 + 1
for i in range(1,h+1):
    if i == 1 or i == h or i == center_pos:
        print("* "*(w))
    else:
        print("*"+"   "+"*")    
'''
#      *
#     * *
#    *   *
#   * * * * 
#  *       *
# *         *
'''
h = 12
c = h*2+1
center_pos = int(h/2+1)
for i in range(1,h+1):
    if i == 1:
        print("*".center(c))
    elif i == center_pos:
        print(("* "*(center_pos+1)).center(c))
    else:
        print(("*"+" "*(i*2-1)+"*").center(c))        
'''

#* * * 
#*
#*
#*
#* * * 
'''
h = 5
for i in range(1,h+1):
    if i == 1 or i == h:
        print("* * *")
    else:
        print("*")    
'''
'''
* * * *
*     * 
*     *
*     *
* * * *
'''
'''
h = 7
w = 4
for i in range(1,h+1):
    if i == 1 or i == h:
        print("* "*(w))
    else:
        print("*"+" "*(w+1)+"*")    
'''
#* * * *
#* 
#* * * *
#*
#* * * *
'''
h = 5
center_pos = h//2 +1
for i in range(1,h+1):
    if i == 1 or i == center_pos or i == h:
        print("* "*4)
    else:
        print("*")    
'''
#* * * *
#* 
#* * * *
#*
#*
'''
h = 5
center_pos = h//2 + 1
for i in range(1,h+1):
    if i == 1 or i == center_pos:
        print("* "*4)
    else:
        print("*")     
  '''
  #* * * *
  #*
  #*   * *
  #*     * 
  #* * * * 
'''
h = 5
center_pos = h//2 + 1
for i in range(1,h+1):
    if i == 1 or i == h:
        print("* "*(h-1))
    elif i == center_pos:
        print("*"+" "*(h-2)+"* *") 
    elif i == 4:
        print("*"+" "*h+"*")       
    else:
        print("*")   
        '''  
#*     *
#*     *
#* * * *
#*     *
#*     *
'''
h = 5
cnt_p = h//2+1
for i in range(1,h+1):
    if i == cnt_p:
        print("* "*(h-1))
    else:
        print("*"+" "*(h)+"*") 
'''
#* * *
#  * 
#  *
#  *
#* * *          
h = 5
w = 3
for i in range(1, h+1):
    if i ==1 or i == h:
        print("* "*(w))
    else:
        print(" "*(w-1)+"*")    
       
