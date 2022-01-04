
 
 
num=int(input("enter number"))
for i in range(1,11):
    print(num,"*",i,"=",(num*i)) 
    
    n=1
i=1
while(n==1):
    num=int(input("enter Multiplication number "))
    i=1
    while(i<=10):
        print(num,"*",i,"=",num*i)
        i=i+1
    n=int(input("Do you want to continue"))
