import statistics

with open("2021/Day10/day10.txt") as f:
    lines = f.read().split("\n")

openClose = {"(": ")", "[": "]", "{": "}", "<": ">"}
opens = []
scores = []


def findCompletionVal(open):
    vals = {"(": 1, "[": 2, "{": 3, "<": 4}
    tot = 0
    open.reverse()
    for char in open:
        tot *= 5
        tot += vals[char]
    return tot


for line in lines:
    opened = []
    broken = False
    for char in line:
        if char in ("[", "{", "<", "("):
            opened.append(char)
        elif openClose[opened[-1]] == char:
            opened.pop(-1)
        else:
            broken = True
            break
    if not broken:
        opens.append(opened)

## Why am I so bad at naming Variables??
for i in opens:
    scores.append(findCompletionVal(i))
print(statistics.median(scores))
