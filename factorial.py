#factorial
def factorail():
    n=int(input("Enter n value: "))
    if n<0:
        print('invalid number')
    elif n==0:
        print('factorial of 0 is 1')
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
        print("Factorial 0f {} is {} ".format(n,f))
factorail()