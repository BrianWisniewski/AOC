eps = ""
gamma = ""
ones = []
zeros = []

with open("2021\day3.txt") as f:
    data = f.readlines()

for i in range(12):
    ones.append(0)
for i in range(12):
    zeros.append(0)


for data_i, num in enumerate(data):
    for num_i, char in enumerate(num):
        if char == "1":
            ones[num_i] += 1
        elif char == "0":
            zeros[num_i] += 1

for i in range(12):
    if ones[i] > zeros[i]:
        gamma += "1"
    else:
        gamma += "0"

for i in gamma:
    if i == "1":
        eps += "0"
    else:
        eps += "1"


print(f"Gamma: {gamma}")
print(f"Epsilon: {eps}")
print(f"Checksum: {int(gamma, 2) * int(eps, 2)}")
print(ones)
print(zeros)
