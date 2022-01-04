'''n=145
s=str(n)
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")'''
    
#without predefined    
n=341
b=str(n)
sum=0
for i in range(len(b)):
    r=n%10
    sum=sum*10+r
    n=n//10
print(sum)    