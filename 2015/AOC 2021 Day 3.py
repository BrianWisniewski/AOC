tmp = input()
numsIn = tmp.split()
ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
epsilon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for num in numsIn:
    for i, binary in enumerate(num):
        if int(binary) == 0:
            zeros[i] += 1
        else:
            ones[i] += 1

for i in range(len(ones)):
    if ones[i] > zeros[i]:
        gamma[i] = 1
        epsilon[i] = 0
    else:
        gamma[i] = 0
        epsilon[i] = 1


def concat(lists):
    out = ""
    for i in lists:
        out = out + str(i)
    return out


print(ones)
print(zeros)
print("Gamma:   " + concat(gamma))
print("Epsilon: " + concat(epsilon))
