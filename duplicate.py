# print duplicate words in a given string # hi hello hi hello bitLabs hi nagul nagul hello vijayawada

str=input("Enter your string ")
count=1 #comparing with 1 element initially so
words=str.split(" ")
for i in range(len(words)): # i starts from 0 to len(words) #2nd iteration i=1
    for j in range(i+1,len(words)): #0+1=1 j compares value of i from 1st index to last index in first iteration. #2nd itr j=2 to last index
        if words[i]==words[j]: # 0-1, 0-2, 0-3,0-4.../1-2,1-3,1-4../2-3,2-4,2..
            count=count+1
            words[j]=None
        if count>1 and words[i]!=None:
            print(words[i])
            count=1
            

    
  
    
    
    
    
