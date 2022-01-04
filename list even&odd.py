#3. Program to create two lists with EVEN numbers and ODD numbers from a list.
list1 = [11, 22, 33, 44, 55]

listOdd = []
listEven = []


for num in list1:
	if num%2 == 0:
		listEven.append(num)
	else:
		listOdd.append(num) 

print ("list1:    ", list1 )
print ("listEven: ", listEven)
print ("listOdd:  ", listOdd)