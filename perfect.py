n = int(input("  Enter any Number: "))
Sum = 0
for i in range(1, n):
    if(n % i == 0):
        Sum = Sum + i
if (Sum == n):
    print("Perfect Number" ,n)
else:
    print("not a Perfect Number" ,n)