str1 = input("enter string1")
str2 = input("enter string2")
c = 0 
if len(str1)<len(str2):
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            c = c+1 
else:
    for i in range(len(str2)):
        if str1[i]==str2[i]:
            c=c+1
    
print(c)    