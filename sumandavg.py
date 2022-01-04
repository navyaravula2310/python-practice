t = "English=78 Science=83 Math=68 History=65"

st = t.split()

sum = 0
for i in range(4):
    print(st[i])
    sub = st[i]
    sum = sum + int(sub[-2:])
print("sum : ", sum)
print("avg : ", sum/4)