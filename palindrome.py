
rev=0
n=int(input("enter n value"))
temp=n;
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if temp==rev:
    print("1")
else:
    print("0")