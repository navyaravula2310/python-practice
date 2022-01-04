#product
def productofdigit(n):
    a=1
    b=str(n)
    c=len(b)
    print(("length",c))
    for i in range(1,c+1):
        j=n%10
        n=n//10
        a=a*j
    print(a)
            
f=int(input("enter value"))
print(productofdigit(f))