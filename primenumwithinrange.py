n=int(input("enter start number"))
m=int(input("enter end number"))
for i in range(n,m):
    for j in range(n,i): #it divides from n to i(i-1)
        if i%j==0:
            break
    else:
        print(i)
           
         

         
         
         
         