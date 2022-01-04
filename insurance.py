name=input("enter name=")
gender=input("gender[male/female]=")
married=input("married[yes/no]=")
age=int(input("enter the age="))
if gender=='female':
    if married=='yes':
        if age>25:
            print(name,"  is eligible for insurance")
        else:
            print(name, " age is less than 25 not eligible for insurance")
    else:
        print(name,"is unmarried")
        
if gender=='male':
    if married=='yes':
        if age>30:
            print(name," is eligible for insurance")
        else:
            print(name,"age is less than 30 not eligible for insurance")
    else:
        print(name," is unmarried")