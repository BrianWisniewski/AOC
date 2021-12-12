import copy

potentials = []
definite = []
total = 0

with open("2021\Day9\day9.txt") as f:
    data = f.read().split("\n")

for pos, line in enumerate(data):
    for i, num in enumerate(line):
        num = int(num)
        if i == 0 and num<int(line[i+1]):
            potentials.append((pos, i, num))
        elif i == len(line)-1 and num<int(line[i-1]):
            potentials.append((pos, i, num))
        elif num<int(line[i-1]) and num<int(line[i+1]):
            potentials.append((pos, i, num))

for y, x, n in potentials:

    n = int(n)
    if y==0:
        if int(data[y+1][x])>n:
            definite.append((y, x, n))
            total+=(n+1) 
    elif y==4:
        if int(data[y-1][x])>n:
            definite.append((y, x, n))
            total+=(n+1)    
    elif n<int(data[y+1][x]) and n<int(data[y-1][x]):
        definite.append((y, x, n))
        total+=(n+1) 

basins = []
for i, j, n in definite:

    basin = [(i,j)]

    filled = False
    newWorking = []
    working = [(i,j)]
    while not filled:
        filled = True
        for y, x in working:
            print(f'{working} \n')
            y = int(y)
            x = int(x)

            tmp = max(x-1, 0)
            print(tmp)
            if data[y][tmp] != '9' and (y, tmp) not in basin:
                basin.append((y, tmp))
                newWorking.append((y, tmp))
                filled = False

            tmp = min(x+1, 10)
            print(tmp)
            if data[y][tmp] != '9' and (y, tmp) not in basin:
                newWorking.append((y, tmp))
                basin.append((y, tmp))
                filled = False

            tmp = min(y+1, 10)
            print(tmp)
            if data[tmp][x] != '9' and (tmp, x) not in basin:
                newWorking.append((tmp, x))
                basin.append((tmp, x))
                filled = False

            tmp = max(y-1, 0)
            if data[tmp][x] != '9' and (tmp, x) not in basin:
                newWorking.append((tmp, x))
                basin.append((tmp, x))
                filled = False    

            working = copy.deepcopy(newWorking)
            newWorking = []

    basins.append(basin)
lengths = []
for i in basins:
    lengths.append(len(i))
lengths.sort()
print(definite, basins, lengths)