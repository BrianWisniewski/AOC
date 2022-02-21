newData = []
with open("2021\day8.txt") as f:
    data = f.readlines()
for i in data:
    newData.append(i.split(" | ")[1])
one = 0
four = 0
seven = 0
eight = 0
data.clear()
for i in newData:
    for j in i.split():
        data.append(j)
for i in data:
    if len(i) == 2:
        one += 1
    elif len(i) == 4:
        four += 1
    elif len(i) == 3:
        seven += 1
    elif len(i) == 7:
        eight += 1
print(one)
print(four)
print(seven)
print(eight)
print(one + four + seven + eight)
