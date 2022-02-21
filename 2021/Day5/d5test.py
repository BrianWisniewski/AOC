import copy

board = []
sideLength = 10
for i in range(sideLength):
  line = []
  for j in range(sideLength):
    line.append(0)
  board.append(line)
  
points = [('8', '2', '8', '6')]

def createVerticalLine(board, yStart, yStop, xVal):
    col = [line[xVal] for line in board]
    for i, num in enumerate(col):
        if i >= yStart and i <= yStop:
            board[i][xVal] += 1
    return board


def createHorizontalLine(board, xStart, xStop, yVal):
    print(xStart, xStop, yVal)
    boardCopy = copy.deepcopy(board)
    for i, num in enumerate(boardCopy[yVal]):
        if i >= xStart and i <= xStop:
          print(board[yVal], yVal)  
          board[yVal][i] += 1
          print(board[yVal], yVal)
          print('')
    return board


for pointSet in points:

    x1, y1, x2, y2 = tuple(map(lambda x: int(x), pointSet))
    print(pointSet)
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if y1 == y2:  #If creating a horizontal line
        start = min(x1, x2)
        end = max(x1, x2)
        board = createHorizontalLine(board, start, end, y1)
    elif x1 == x2:  #If creating a vertical line
        start = min(y1, y2)
        end = max(y1, y2)
        board = createVerticalLine(board, start, end, x1)
for line in board:
    print(line)
