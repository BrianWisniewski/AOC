import copy

oxy = ""
co = ""
ones = []
zeros = []

with open("2021\Day3\day3.txt") as f:
    data = f.read().split('\n')

def countList(lines, pos: int):
    count = [0, 0]
    for nums in lines:
        if nums[pos] == '1':
            count[1] += 1
        elif nums[pos] == '0':
            count[0] += 1
    return count

for postition in range(len(data[0])):
    counts = countList(data, postition)
    if counts[1] >= counts[0]:
        numToRemove = 0
    else:
        numToRemove = 1
    print(counts, numToRemove)

    for i in range(len(data)):
        
        if int(data[i][postition]) == numToRemove:
            print(data[i])
            while data.count(str(data[i])) > 0:
                data.remove(data[i])          
print(data)

