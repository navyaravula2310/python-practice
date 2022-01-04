
n=int(input('enter end number'))
pm=[]
for i in range(2,n+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
              break
        else:
            print(i)
            pm.append(i)
print('number of prime numbers' ,len(pm))



