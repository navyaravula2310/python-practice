#4 perfect number
def num(Num):
    Sum = 0
    for i in range(1, Num):
     if(Num % i == 0):
        Sum = Sum + i
     if (Sum == Num):
         print("  is a Perfect Number" ,Num)
     else:
         print("  is not a Perfect Number" ,Num)
    
Num = int(input("  Enter any Number: "))    
print(num(Num))