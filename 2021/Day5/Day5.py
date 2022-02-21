import copy
import typing

board = []
sideLength = 10
for i in range(sideLength):
    line = []
    for j in range(sideLength):
        line.append(0)
    board.append(line)
print("Board created")

points = [ (7, 6, 3, 9), (5, 6, 1, 2), (5, 2, 5, 9), (1, 3, 5, 3)]
# with open("./lines.txt") as f:
#     f = f.read().split("\n")
#     for line in f:
#         start, end = line.split(" -> ")
#         x1, y1 = start.split(",")
#         x2, y2 = end.split(",")
#         points.append((x1, y1, x2, y2))
print("Points imported")


def createVerticalLine(board: list, yStart: int, yStop: int, xVal: int) -> list:
    col = [line[xVal] for line in board]
    for i, _ in enumerate(col):
        if i >= yStart and i <= yStop:
            board[i][xVal] += 1
    return board


def createHorizontalLine(board: list, xStart: int, xStop: int, yVal: int) -> list:
    boardCopy = copy.deepcopy(board)
    for i, _ in enumerate(boardCopy[yVal]):
        if i >= xStart and i <= xStop:
            board[yVal][i] += 1
    return board


def createDiagonalLineRight(board: list, startingPoint: tuple, endingPoint: tuple) -> list:
    pointToMod = startingPoint  # Takes the form of (x, y)
    for _ in range(startingPoint[0] - endingPoint[0]):
        board[pointToMod[1]][pointToMod[0]] += 1
        pointToMod = (pointToMod[0] + 1, pointToMod[1] + 1)
    return board


def createDiagonalLineLeft(board: list, startingPoint: tuple, endingPoint: tuple) -> list:
    pointToMod = startingPoint  # Takes the form of (x, y)
    for _ in range(startingPoint[0] - endingPoint[0]):
        board[pointToMod[1]][pointToMod[0]] += 1
        pointToMod = (pointToMod[0] - 1, pointToMod[1] + 1)
    return board


for i, pointSet in enumerate(points):
    x1, y1, x2, y2 = pointSet
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if y1 == y2:
        start = min(x1, x2)
        end = max(x1, x2)
        board = createHorizontalLine(board, start, end, y1)
    elif x1 == x2:
        start = min(y1, y2)
        end = max(y1, y2)
        board = createVerticalLine(board, start, end, x1)
    else:
        leftPoint = (x1, y1) if x1 < x2 else (x2, y2)
        rightPoint = (x1, y1) if x1 > x2 else (x2, y2)
        print(leftPoint, rightPoint)
        if rightPoint[0] - leftPoint[0] == rightPoint[1] - leftPoint[1]:
            board = createDiagonalLineRight(board, leftPoint, rightPoint)

        elif rightPoint[0] - leftPoint[0] == leftPoint[1] - rightPoint[1]:
            board = createDiagonalLineLeft(board, rightPoint, leftPoint)

    print(f"Lines drawn: {i+1}/{len(points)}")
print("All lines drawn")

for line in board:
    print(line)

totalIntersections = 0
for line in board:
    for number in line:
        if number > 1:
            totalIntersections += 1
print(f"Total Intersections: {totalIntersections}")
