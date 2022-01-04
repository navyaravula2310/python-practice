nums={23,45,89,22,77,44,90,75}
max=0
smax=0
for i in nums:
    if max<i:
    smax=max
    max=i
elif smax<i:
smax=i

print("MAX value: ",max)
print("Second max value: ",smax)