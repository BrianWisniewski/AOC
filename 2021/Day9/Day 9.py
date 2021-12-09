with open("2021\Day9\day9.txt") as f:
    data = f.read()
data = data.split("\n")

potentials = []
done = []
total = 0

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

print(done)
print(total)