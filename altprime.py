
# Python program to display all the prime numbers within an interval
m = 2
n = 100
s= ""
for i in range(m,n):
    f = 0
    for j in range(2,i):
        if i%j == 0:
            f = f+1 
    if f == 0:
        s = s  + str(i) +" "
s = s.split()

for i in range (len(s)-1):
    if i%2 == 1:
        print(s[i])




