import copy

board = []
sideLength = 1000
for i in range(sideLength):
    line = []
    for j in range(sideLength):
        line.append(0)
    board.append(line)
print("Board created")

points = []
with open("./lines.txt") as f:
    f = f.read().split("\n")
    for line in f:
        start, end = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        points.append((x1, y1, x2, y2))
print("Points created")


def createVerticalLine(board, yStart, yStop, xVal):
    col = [line[xVal] for line in board]
    for i, _ in enumerate(col):
        if i >= yStart and i <= yStop:
            board[i][xVal] += 1
    return board


def createHorizontalLine(board, xStart, xStop, yVal):
    boardCopy = copy.deepcopy(board)
    for i, _ in enumerate(boardCopy[yVal]):
        if i >= xStart and i <= xStop:
            board[yVal][i] += 1
    return board


linesDrawn = 0
for pointSet in points:
    x1, y1, x2, y2 = pointSet
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if y1 == y2:
        start = min(x1, x2)
        end = max(x1, x2)
        board = createHorizontalLine(board, start, end, y1)
        linesDrawn += 1
    elif x1 == x2:
        start = min(y1, y2)
        end = max(y1, y2)
        board = createVerticalLine(board, start, end, x1)
        linesDrawn += 1
    print(f"Lines drawn: {linesDrawn}")
print("All lines drawn")


totalIntersections = 0
for line in board:
    for number in line:
        if number > 1:
            totalIntersections += 1
print(totalIntersections)
