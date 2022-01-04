s="navya vijayawada navya city is city vijayawada navi city"
b=s.split(" ")
k=0;
count=1
l=len(s)
for i in b:
    k=k+1
    for j in range(k,len(b)):
        if b[j]=="0":
            pass
        elif i==b[j]:
            count=count+1
            b[j]="0"
    if i!="0":
        print(i,count)
        count=1