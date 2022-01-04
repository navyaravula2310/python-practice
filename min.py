nums={23,45,89,22,77,44,90,75}
l=list(nums)
min=l[0]
smin=l[0]
for i in nums:
if min>i:
smin=min
min=i
elif smin>i:
smin=i

print("Min value: ",min)
print("Second min value: ",smin)