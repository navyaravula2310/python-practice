#3factors
def fact(n):
    fact=1
    for i in range(1,n):
        if n%i==0:
            print(i)
            
f=int(input("enter number"))
print(fact(f))

