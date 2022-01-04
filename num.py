#check number is even and divisible by 8
num=int(input("enter the number"))
if num%2==0:
    if num%8==0:
        print('number ids even and divisible by 8')
else:
        print("not divisible by 8")
else:
    print("not even number")