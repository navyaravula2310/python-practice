#1.  Program for Adding, removing elements in the list.


list=[12,15,11,25,33]
n=int(input("enter the add value="))
list.insert(3,n)#add
print(list)
m=int(input("enter the remove value="))
list.remove(m)
print(list)