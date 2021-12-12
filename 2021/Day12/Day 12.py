connections = []
with open("2021\Day12\day12.txt") as f:
    data = f.read().split("\n")
for line in data:
    connections.append(line.split("-"))

print(connections)
