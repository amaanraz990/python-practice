#tuple ,truple is immutable(not changable)
#x = (1,23,3,34,2,3,5)
#print(type(x))
#print(x[1:-1])
#print(len(x))

#months = ('jan','fab','mar','apr','may','jun','july','aug','sep','oct','nov','dec')

#print(type(months))
#print(months)
#print(months[5:11])
#it will not work bec tuple is not mutable
#months[0]= "dec"

#another way to create tuple

##days = tuple(('mon','tue','wed','thr','fri','sat')) 
##print(days)
##print(type(days))
##print(days[2:4])
# we can change any object in tuple to assign a tuple to list and then asign 
# list to tuple 
#days_list = list(days)
#print(days_list)
#print(type(days_list))
#days_list[2] = 'wed1'
#print(days_list)
#days = tuple(days_list)
#print(days)
#print(type(days))
"""
# use for loop in tuple 
for d in days:
    #print(d[0:2])
    #print(d)
    for m in d:
        if m not in 'aeiou':
            print(m) 
            """

week_days = ( 'Mon', 'Tue', 'Wed', 'Thur', 'Fri','sat','sun' )
#(a,b,c,d,e,d,e,) = week_days
#c = 'wed1'
#print(week_days)
#print(c)
day1 = week_days[0] 
day2 = week_days[1] 
day3 = week_days[2] 
day4 = week_days[3] 
day5 = week_days[4] 
day6 = week_days[5] 
day7 = week_days[6] 
print(day1)
print(day2)
print(day3)
print(day4)
print(day5)
print(day6)
print(day7)

