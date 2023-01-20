# ops (object oriented programming)
#class amaan:
#    age = 18
#   weight = 65
#   sname = "raza"

#    def displayname():
#        print("hello name")

#amaan.displayname()
'''
class amaan:
    def displayname(self,x):
        print("hello",self.name)
        print("x=", x)

        
    def displayAge( self ):
         print("You age  ", self.age)

p1 = amaan()
p1.name = "raza"
print(p1.name)

p2 = amaan()
p2.name = "mujahid"
p2.age = "25"
print(p2.name)
print(p2.age)
'''
'''
class male:


     def __init__( self , name, age ):
        self.name = name
        self.age = age

     def displayName( self , x ):
        print("Hello ", self.name)
        print("x=", x)

     def displayAge( self ):
        print("You age  ", self.age)


p1 = male("amaan", 18)
print(p1.name)
print(p1.age)

p2 = male("mujahid", 24)
print(p2.name)
print(p2.age)
'''
'''
class cars:
   color = "black"
   engin = "lxi"  
   name = "hector"    

   def displayName():
      print("hello")

cars.displayName()'''
'''
class cars:
   def displayName(self , x):      
     print("name:",self.name)
     print("seat:" , x)
   def displayColor(self):
      print("color:",self.color)
   def displayPrice(self):
      print("price:", self.price)
   

p1 = cars()
p1.name = "bmw"
p1.color = 'black'
p1.price = 10000000
print(p1.name)
print(p1.color)

p2 = cars()
p2.name = "porsch"
p2.color = "blue"
p2.price = 2000000000
print(p2.name)
print(p2.color)

p1.displayName()
p2.displayName()
p2.displayColor()
p1.displayColor()
p1.displayPrice()
p2.displayPrice()


p1.displayName(5)'''
# __init__ is a constructor it call when we create a object
"""
class cars:
   def __init__(self, name , color):
      self.name = name
      self.color = color
       
   def displayName(self , x):      
     print("name:",self.name)
     print("seat:" , x)
   def displayColor(self):
      print("color:",self.color)
   def displayPrice(self):
      print("price:", self.price)
   
p1 =  cars("mercidies","red")
p1.displayColor()
p2 = cars("bmw","white")
p2.displayName(5)
print(p2.color)
"""
class country :
   def __init__(self,country,capital,area,pm,states,union_ter):
      self.country = country
      self.capital = capital
      self.area = area
      self.pm = pm
      self.states = states
      self.union_ter = union_ter

   def displayCountry(self):
      print("name:",self.country)    
   def displayCapital(self):
      print("Capital:", self.capital)  
   def displayArea(self):
      print("Area:", self.area)  
   def displayPm(self):
      print("PM:", self.pm)  
   def displayStates(self):
      print("states:", self.states)  
   def displayunion_ter(self):
      print("states:", self.union_ter)  

c1 = country("india","new delhi",2500,"modi",28,8)   
c2 = country("pakistan","islamabad",1000,"shehwaz shareef",4,1)
#c1.displayName()   
#c1.displayPm()
#c1.displayArea()
#c#2.displayArea()
c2.displayCountry()
c2.displayArea()
c2.displayPm()