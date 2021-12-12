import copy

oxy = ""
co = ""
ones = []
zeros = []

with open("2021\Day3\day3.txt") as f:
    data = f.read().split("\n")
inputLength = len(data[0])


def countList(lines, pos):
    count = [0, 0]
    for nums in lines:
        if nums[pos] == "1":
            count[1] += 1
        elif nums[pos] == "0":
            count[0] += 1
    return count


for postition in range(inputLength):
    counts = countList(data, postition)
    if counts[1] >= counts[0]:
        numToRemove = 1
    else:
        numToRemove = 0
    print(counts)

    data2 = copy.deepcopy(data)
    for line in data2:
        if int(line[postition]) == numToRemove:
            data.remove(line)
    if len(data) == 1:
        break
print(data[0])
print(int(data[0], base=2))
