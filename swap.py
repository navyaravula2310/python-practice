#Write a Python program to read two numbers from the user and swap the values of both the numbers and display the values.
a=int(input("enter first number"))
b=int(input("Second number"))
print("before swaping","a=",a,"b=",b)
temp=a
a=b
b=temp
print("after Swaping","a=",a,"b=",b)