with open("2021/Day10/day10.txt") as f:
    lines = f.read().split("\n")

openClose = {'(': ')', '[': ']', '{': '}', '<': '>'}
pointTotal = 0

for line in lines:
    opened = []
    for char in line:
        if char in ("[", "{", "<", "("):
            opened.append(char)
        elif openClose[opened[-1]] == char:
            opened.pop(-1)
        else:
            print(f'Expected: {openClose[opened[-1]]} but found {char} instead.')
            if char == '>':
                pointTotal += 25137
            elif char == '}':
                pointTotal += 1197
            elif char == ']':
                pointTotal += 57
            elif char == ')':
                pointTotal += 3
            break
print(pointTotal)