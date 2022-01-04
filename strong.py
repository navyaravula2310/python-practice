#145
'''num=int(input("enter number"))
temp=num
sum=0
f=1
while (num!=0):
    rem=num%10
    for i in range(1,rem+1):
        f=f*i
    sum=sum+f
    num=num//10
    f=1
if temp==sum:
    print('It is strong number')
else:
    print("not strong number")'''
        
       
        
'''a=50
b=500
sum=0
f=1
for j in range(a,b+1):
    rem=j%10
    temp=j
    if j>50:
        for i in range(a,rem+1):
            f=f*i
        sum=sum+f
        j=j//10
        f=1
if temp==sum:
    print(j)'''
    
    
    
#printing list of strong numbers between 50 to 500.    
a=50#int(input("enter the 1 value"))
b=500
#int(input("enter the 2 value"))
p=0
for i in range(a,b+1):
    
    temp=i
   
    d=str(i)
    c=len(d)
    for j in range(c):
       
        r=i%10
        i=i//10
      
        j=1
        for k in range(1,r+1):
            j=j*k
       
        p=p+j
   
    if temp==p:
        p=0
        print(temp,":strong")
    else:
        p=0    
    