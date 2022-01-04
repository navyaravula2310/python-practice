str=input("enter string: ")
ccount=0
dcount=0
scount=0
for i in str:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        ccount=ccount+1
    elif i>='0' and i<='9':
        dcount=dcount+1
    elif i!=' ':
        scount=scount+1
print("- Number of characters : ",ccount,"- Number of digits :",dcount,"- Number of special characters :",scount) 