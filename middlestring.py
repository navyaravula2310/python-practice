str='Anushya'
length=len(str)
if length>=7:
    words= int(len(str)/2)
    res = str[words - 1:words + 2]
    print('Anushya Middle three chars:',res)
else:
     print(str)
        
    