import copy

with open('./nums.txt') as f:
  nums = f.read().split(',')

with open('./boards.txt') as f:
  boards = f.read().split('\n\n')

for i, board in enumerate(copy.copy(boards)):
  boards[i] = list(line.split() for line in board.split('\n'))

def hasWon(board, nums):
  #checks horizontal
  for i in range(5):
    line = board[i]
    inNums = 0
    for num in line:
      if num in nums:
        inNums += 1
    if inNums == 5:
      return True

  #checks vertical
  for i in range(5):
    col = [line[i] for line in board]
    bingo = 0
    for num in col:
      if num in nums:
        bingo += 1
    if bingo == 5:
      return True


def totalUnusedNums(board, nums):
  total = 0
  for line in board:
    for num in line:
      if num not in nums:
        total += int(num)
  return total

boardsLeft = copy.deepcopy(boards)

i = 1
while len(boardsLeft) != 1:
  numRange = nums[:i]
  for board in boardsLeft:
    if hasWon(board, numRange):
      boardsLeft.remove(board)
  i+=1

print(numRange[-1])
print(totalUnusedNums(boardsLeft[0], numRange))


anwser = totalUnusedNums(boardsLeft[0], numRange) * int(numRange[-1])
print(anwser)