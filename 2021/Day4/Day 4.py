import copy

with open('./nums.txt') as f:
  nums = f.read().split(',')

with open('./boards.txt') as f:
  boards = f.read().split('\n\n')

for i, board in enumerate(copy.copy(boards)):
  boards[i] = list(line.split() for line in board.split('\n'))

def hasWon(board, nums):
  hasWon = False

  #checks horizontal
  for i in range(5):
    line = board[i]
    inNums = 0
    for num in line:
      if num in nums:
        inNums += 1
    if inNums == 5:
      hasWon = True

  #checks vertical
  for i in range(5):
    col = [line[i] for line in board]
    bingo = 0
    for num in col:
      if num in nums:
        bingo += 1
    if bingo == 5:
      hasWon = True

  return hasWon

def totalUnusedNums(board, nums):
  total = 0
  for line in board:
    for num in line:
      if num not in nums:
        total += int(num)
  return total
        
# This is jank and I know it.
breakLoop = False
for i, _ in enumerate(nums):
  numRange = nums[:i+1]
  for board in boards:
    if hasWon(board, numRange):
      out = (board, numRange)
      breakLoop = True
      break
  if breakLoop:
    break
winningBoard, winningNums = out

anwser = totalUnusedNums(winningBoard, winningNums) * int(winningNums[-1])
print(anwser)