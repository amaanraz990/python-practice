# File Handling 
'''
f = open('amaan2.txt','a')


f.write("This is a file1\n")
f.write("This is a file2\n")
f.write("This is a file3\n")
f.write("This is a file4\n")
f.write("This is a file5\n")

f.close()
'''

#append mode
'''
f = open('amaan1.txt','a')

f.write("This is a file6\n")

f.close()

'''
'''
#Read file
f = open('amaan1.txt','r')
#print(f.read())
#it read character
#print(f.read(20))
#print(f.readline(4))

#line = f.readline()
#for l in line:
#    print(l)

f.close()
'''
#Deletation a file
import os 
os.remove("amaan2.txt")