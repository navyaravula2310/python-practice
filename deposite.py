
print("enter the period of time")
time=int(input("enter the time="))
amount=int(input("enter the amount="))
if time>=7:
    interest=(time*amount*7.5)/100
    print("interest for ",time ," years is",interest)
else:
         interest=(time*amount*4.5)/100
         print("interest for ",time ,"is",interest)