import cmath
a=int(input("enter first number"))
b=int(input("enter first number"))
c=int(input("enter first number"))

d = (b**2) - (4*a*c)

sol = (-b-cmath.sqrt(d))/(2*a)

print('The solution is ',sol)