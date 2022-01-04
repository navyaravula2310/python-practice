# you have to check grade of student
marks>90--A
marks between 80 to 90--B
marks between 70 to 80--c
marks 70-60--D
else
fail

a=int(input("Enter marks:"))
if a>=90:
    print("grade is A")
elif a>=80 and a<90:
    print("grade id B")
elif(marks>70 and marks<80):
    print('grade is C')
elif(marks>60 and marks<70):
    print('grade is D')
else:
    print('fail')