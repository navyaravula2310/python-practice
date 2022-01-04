'''a=0
b=1
for i in range(1,10):
    temp=a+b
    a=b
    b=temp
    print(temp,end=" " )'''
   
#with 0,1 also prints    
a=0
b=1
for i in range(1,11):
    print(a)
    temp=a
    a=b
    b=temp+a    
   
