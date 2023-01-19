student = {}
n = int(input("enter the no. of student"))
for i in range(n):
    name = input("please enter your name: ")
    marks=[]
    n1 = int(input("enter the no. of subjects:"))
    for i in range(n1):
        m = int(input("enter the marks:"))
        marks.append(m)
    student[name] = marks
print(student)        

for i in student:
    print("student name:",i,)
    total_marks = sum(student[i])
    percentage = total_marks/n1
    print("total marks out of 500",total_marks)
    print("percentage",percentage)
    div = ''
    if percentage >= 60:
        print("congratulation pass with first position")
    elif percentage >= 50:
        print("congratulationpass with secont position") 
    elif percentage >= 40:
        print("congratulationpass with second position") 
    elif percentage >= 33:
        print("congratulation pass")
    else:
        print("fail")
        print("work hard")    



