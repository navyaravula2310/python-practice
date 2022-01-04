

i = 1
positive = 0
negative = 0
for i in range(10):
    n = int(input("Enter Number"))
    if n > 0:
        positive = positive+n 
    elif n < 0:
        negative = negative +n
print("Sum of negatives :",negative)
print("Sum of Positive Number :",positive)