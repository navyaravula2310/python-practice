#6. Python program to multiply all numbers of a list.
a = [2,4,6,8,10]
print(a)
b=int(input("enter the multiply="))
c=[]

for i in a:
    d=b*i
    c.append(d)
print("multiply of",b,"is",c)