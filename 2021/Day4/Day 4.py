import copy

with open('./nums.txt') as f:
  nums = f.read().split(',')

with open('./boards.txt') as f:
  boards = f.read().split('\n\n')

for i, board in enumerate(copy.copy(boards)):
  boards[i] = list(line.split() for line in board.split('\n'))
print(boards)


def hasWon(board, nums):
  hasWon = False

  #checks horizontal
  for i in range(5):
    if board[i].count(board[i][0]) == 5 and board[i][0] in nums:
      hasWon = True

  #checks vertical
  for i in range(5):
    subList = []
    for j in range(5):
      subList.append(board[j][i])
    if subList.count(board[i][0]) == 5 and subList[0] in nums:
      hasWon = True

  #checks diagnal
  topLeft = board[0][0]
  topRight = board[0][4]

  for i in range(5):
    if board[i][i] == topLeft and topLeft in nums:
      if i == 4:
        hasWon = True
    else:
      break

    if board[i][-(i+1)] == topRight and topRight in nums:
      if i == 4:
        hasWon = True
    else:
      break
    
    return hasWon
  
for i in boards:
  print(hasWon(i, nums))