import statistics

with open("2021\day7.txt") as f:
    data = f.read()


data = data.split(',')
newData = []
for i in data:
    newData.append(int(i))

median = int(statistics.mean(newData))

tot = 0
for i in newData:
    num = int(abs(i-median))
    for i in range(num):
        tot+=(i+1) 
print(median)
print(tot)