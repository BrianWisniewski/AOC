import copy

potentials = []
done = []
total = 0

with open("2021\Day9\day9.txt") as f:
    data = f.read()
data = data.split("\n")



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
            done.append((y, x, n))
            total+=(n+1) 
    elif y==99:
        if int(data[y-1][x])>n:
            done.append((y, x, n))
            total+=(n+1)    
    elif n<int(data[y+1][x]) and n<int(data[y-1][x]):
        done.append((y, x, n))
        total+=(n+1) 


basins = []

for i, j, n in done:

    basin = [(i,j)]

    filled=False
    while not filled:
        filled = True
        newWorking = []
        working = []

        for y, x in working:

            try:
                if data[y][x-1] != 9 and (y, x-1) not in basin:
                    basin.append((y, x-1))
                    newWorking.append((y, x-1))
                    filled = False

            except Exception:
                pass

            try:
                if data[y][x+1] != 9 and (y, x+1) not in basin:
                    newWorking.append((y, x+1))
                    basin.append((y, x+1))
                    filled = False

            except Exception:
                pass

            try:
                if data[y+1][x] != 9 and (y+1, x) not in basin:
                    newWorking.append((y+1, x))
                    basin.append((y+1, x))
                    filled = False

            except Exception:
                pass

            try:
                if data[y-1][x] != 9 and (y-1, x) not in basin:
                    newWorking.append((y-1, x))
                    basin.append((y-1, x))
                    filled = False    

            except Exception:
                pass

            working = copy.deepcopy(newWorking)
            newWorking = []
    basins.append(basin)
    print(basin)
