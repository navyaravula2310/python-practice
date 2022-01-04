#fibonacci series

def fibonacci():
    a=0
    b=1
    n=int(input('enter number'))
    if n==1:
        print(a)
    else:
        for i in range(n):
            c=a+b
            a=b
            b=c
            print(c, end=' ')
fibonacci()      
        
   