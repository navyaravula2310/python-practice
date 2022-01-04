num=int(input("Enter number to check it is armstrong number or not"))
digits= len(str(num))
rem=0
sum=0
temp=num
while num!=0:
    rem=num%10 
    sum=sum+(rem**digits)
    num=num//10
    if temp==sum:
        print("armstrong number")
    
else:
    print("Not a armstrong number")
     
     
     

     
     
 
 

         
     
     
     
     
     
     
     