str1 =  input ("enter the number of string1")
str2 =  input ("enter the number of string2") 
count=0
for i in range(0,len(str1)-1):
    for j in range(0,len(str1)-1):
        if str1[i]==str2[j]:
            count=count+1
if count>1:
    print("1")
else:
    print("-1")