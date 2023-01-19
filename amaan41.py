# start with __ is private member ex(__salary)
# we can call private member within the class only not out side the class
'''
class Person :

    def __init__(self,name,age,s):
        self.name = name
        self.age = age
        self.__salary = s

    def displayName( self):
         print("Hello ", self.name)
         print("Salary ", self.__salary)
         self.__displayAge()
         
# it starts __ it is private function it call in another function
# it access only with in the class
    def __displayAge( self ):
        print("You age  ", self.age)

    def __str__(self):
        return self.name
    
p1 = Person("Amaan", 21, 100000)
#p2 = Person("saim",21,4357)
#p1.displayName()
#p2.displayName()

print(p1) # it call __str__ function automatically

class Person :

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
       
    def displayfname( self):
         print( self.fname)

    def displaylname(self):
        print(self.lname)    


    def __add__(self):
        z = self.fname + " " + self.lname
        print (z)

p1 = Person("amaan","raza")   
p1.__add__()'''
'''
# Python inheritance (child class contains the propery of parent class )
class Desktop :

    def __init__(self,s,r,k,d):
        self.screen = s
        self.rom = r
        self.keyboard = k
        self.disk = d

    def displayScreen(self):
        print("screen:",self.screen)    
    def displayRam(self):
        print("rom:",self.rom)    
    def displayKeyboard(self):
        print("keyboard:",self.keyboard)    
    def displayDisk(self):
        print("disk:",self.disk)    

#d1 = Desktop(15,512,"backlight","hdd")  
#d1.displayScreen()
#d1.displayRam()

#class Laptop (Desktop):
#    pass
#l1 = Laptop(16,1080,"backlight","ssd")

#l1.displayRam()
#l1.displayDisk()
#l1.displayKeyboard()

class Laptop (Desktop):

    def __init__(self,s,r,k,d,t,p,w):
        super().__init__(s,r,k,d,)
        self.touch = t
        self.power = p
        self.wifi = w

    def displayTouch(self):
        print("laptop is: ",self.touch)    

    def displayPower(self):
        print("power consumption: ",self.power)    

    def displayWifi(self):
        print("wifi support: ",self.wifi)    

    def webcam(self):
        print("webcam is on")
            
# over writting a function from parent class  

    def displayDisk(self):
        print("this is laptop disk")
        print("disk:",self.disk)    
   



#l1 = Laptop(15,256,"normal","hdd","yes","low","5g")       
#l1.displayScreen()
#l1.webcam()
#l1.displayDisk()

'''
"""
# multilevel inheritance
class India :
    
    def __init__(self,p,t):
        self.prime_minister = p
        self.Country_Capital = t

    def PrimeMinister (self):
        print("pm: ",self.prime_minister)

    def CountryCapital(self):
        print("capital: ",self.Country_Capital)      


class States(India):

    def __init__(self,p,t,c,m):  
        super().__init__(p,t)
        self.statescapital = c
        self.cm = m    

    
    def StatesCapital (self):
        print("StatesCapital: ",self.statescapital)

    def CheifMinister(self):
        print("CM: ",self.cm)      
    
#s1 = States ("modi","new delhi","lucknow","yogi")    

#s1.CheifMinister()
#s1.PrimeMinister()
#s1.CheifMinister()
#s1.StatesCapital()
#s1.CountryCapital()
#s1.CountryCapital()

class Distric(States):

    def __init__(self,p,t,c,m,v,w):
         super().__init__(p,t,c,m)
         self.villages = v
         self.town = w

    def Villages(self):
        print("No. villages: ",self.villages)

    def Town(self):
        print("No. of towns: ",self.town)


d1 = Distric("Modi","New Delhi","Lucknow","Yogi",80, 6)        

d1.CheifMinister()
d1.PrimeMinister()
d1.CountryCapital()
d1.Villages()
d1.Town()
d1.StatesCapital()
"""
# Hierarchical Inheritance
'''
class Student:

    def __init__(self,n,c):
        self.students = n
        self.ClassTeacher = c
    
    def No_of_students(self):
        print("No of students in class: ",self.students)

    def Class_Teacher(self):
        print("Class Teacher:",self.ClassTeacher)    
 

class Biology (Student):

    def __init__(self,n,c,s,b):
        super().__init__(n,c)
        self.Biot = s
        self.Bios = b

    def Bio_Teacher(self):
        print("Bio teacher is ", self.Biot)

    def Bio_Sudents(self):
        print("No of students in Bio",self.Bios)



#b1 = Biology(54,"amaan","ariz", 24)
#b1.No_of_students()
#b1.Class_Teacher()
#b1.Bio_Sudents()
#b1.Bio_Teacher()


class Maths (Student):

    def __init__(self,n,c,mt,ms):
        super().__init__(n,c,)
        self.mt = mt
        self.ms = ms

    def Maths_Teacher(self):
        print("Maths teacher is ", self.mt)

    def Maths_Sudents(self):
        print("No of students in maths",self.ms)

m1 = Maths(54,"amaan","kaif",30)

m1.Maths_Sudents()
m1.Maths_Teacher()
m1.Class_Teacher()
m1.No_of_students()
'''
# multiple Inheritance
'''
class Tuv:
    
    def __init__(self,s,g):
        self.slow = s
        self.goodspace = g

    def Lowspeed (self):
        print("speed is :",self.slow)

    def Goodspace (self):
        print("space:",self.goodspace)
  
#c1 = Tuv(120,"good")
#c1.Goodspace()
#c1.Lowspeed()


class Porsche:

    def __init__(self,f,b):
        self.fast = f
        self.badspace = b

    def Fastspeed(self):
        print("speed: ",self.fast)

    def Badspace(self):
        print("space:",self.badspace)

#s1 = Porsche("300","bad")
#s1.Badspace()
#s1.Fastspeed()

class RangeRover(Tuv,Porsche):
   
    def __init__(self):
'''

class Frontant:

    def __init__(self,ui,ux):

        self.ui = ui
        self.ux = ux

    def displayUI(self):
         print(self.ui)

    def displayUX(self):
        print(self.ux)     


#f1 = Frontant("UI design","UX design")
#f1.displayUX()
#f1.displayUI()
       
class Backend:

    def __init__(self,g,d):

        self.game = g
        self.database = d

    def displayGame(self):

        print(self.game)    

    def displayDatabase(self):

        print(self.database)    
      
#b1 = Backend("game design","database management") 
#b1.displayDatabase()
#b1.displayGame()
  
class Language (Frontant , Backend):

    def __init__(self,ui,ux,g,d,p,h):
        super().__init__(ui,ux,g,d)          
        self.py = p
        self.html = h
        
    def BackendLan(self):

        print(self.py,"is backend language")       

    def FrontantLan(self):

        print(self.html,"is frontant language")
l1 = Language("navbar","grafix design" ,"game", "dbms management","python", "html")

l1.BackendLan()















































































