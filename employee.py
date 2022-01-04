name=input("enter name=")
gender=input("gender[male/female]=")
experience=int(input("experience="))
education=input("education[pg/graduate]")
if gender=='female':
    if experience>5:
        print("eligible for job")
        if experience>=10 and education=='pg':
            print(name,"is eligible for the Job with a salary of Rs.60000")
        
        elif experience>5 and experience<10 and education=='pg':
            print(name,"is eligible for the Job with a salary of Rs.45000")
        
        elif experience>=10 and education=='graduate':
            print(name,"is eligible for the Job with a salary of Rs.30000")
        
        elif experience>5 and experience<10 and education=='graduate':
            print(name,"is eligible for the Job with a salary of Rs.20000")
if gender=='male':
    if experience>=5:
        print("eligible for job")
        if experience>=10 and education=='pg':
            print(name,"is eligible for the Job with a salary of Rs.75000")
        
        elif experience>5 and experience<10 and education=='pg':
            print(name,"is eligible for the Job with a salary of Rs.60000")
        
        elif experience>=10 and education=='graduate':
            print(name,"is eligible for the Job with a salary of Rs.50000")
        
        elif experience>5 and experience<10 and education=='graduate':
            print(name,"is eligible for the Job with a salary of Rs.35000")