
import cmath
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = (a + b + c) / 2
area = (cmath.sqrt(s*(s-a)*(s-b)*(s-c))) 
print('The area of the triangle is ', area)