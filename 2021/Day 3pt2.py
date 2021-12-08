import copy

oxy = ""
co = ""
ones = []
zeros = []
tmpNum = 0

with open("2021\day3.txt") as f:
    data = f.readlines()
    
newData = copy.deepcopy(data)

for pos in range(12):

    ones = 0
    zeros = 0
    for line in newData:
        if line[pos] == "1":
            ones += 1
        else:
            zeros += 1
    commonValue = 1 if ones>=zeros else 0
    print(commonValue)
    for i in newData:
        if i[pos] == commonValue:
            while i[pos] in newData:
                newData.remove(i)




print(f'Oxygen: {oxy}')
print(f'CO2: {co}')

print(ones)
print(zeros)