import copy

oxy = ""
co = ""
ones = []
zeros = []
tmpNum = 0

with open("2021\Day3\day3.txt") as f:
    data = f.readlines()

newData = copy.deepcopy(data)
data = copy.deepcopy(newData)
print(len(data[0]))

for pos in range(12):
    ones = 0
    zeros = 0
    for line in data:
        if line[pos] == "1":
            ones += 1
        else:
            zeros += 1
    print(ones, zeros)


    commonValue = 1 if ones>=zeros else 0
    print(commonValue)


    for i in data:
        if i[pos] != commonValue:
            try:
                while True:
                    newData.remove(i)
            except ValueError:
                pass
    data = copy.deepcopy(newData)



print(f'Oxygen: {oxy}')
print(f'CO2: {co}')

print(ones)
print(zeros)