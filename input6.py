p = float(input("please enter p: "))
b = float(input("please enter b: "))
h = p + b
print("h=",type(h))
print("p =",type(p))
print("b =", type(b))
t = int(input("please enter the time "))
s = int(input("please enter the speed "))
d = s*t
print("d=",d)
a = float(input("please enter a "))
b = float(input("please enter b "))
hcf = float(input("please enter hcf "))
lcm = a*b / hcf*a + hcf*b
print("lcm=",lcm)
k = int(input("please enter the value of k "))
x = int(input("please enter the value of x "))
a = int(input("please enter the value of a "))
b = int(input("please enter the value of b "))
quadratic = k*(x-(a+b)*x + a*b)
print("quadratic= ", quadratic)
#  cuboid
h = float(input("please enter height "))
l = float(input("please enter length "))
b = float(input("please enter breadth "))
total_surface_area  = 2*(l*b + b*h + h*l)
curved_surface_area = 2*h*(l+b)
volume = l*b*h
print("total surface area =",total_surface_area )
print("curved surface area =",curved_surface_area)
print("volume =",volume)
# hollow cylinder
r = float(input("please enter internal radii "))
R = float(input("please enter external radii "))
h = float(input("please enter height "))
volume = 3.14*(R*R - r*r)*h
area = 2*3.14*(R+r)*(h + R - r)
print("volume =  " , volume)
print("area = " , area)