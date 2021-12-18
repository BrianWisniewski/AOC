

with open('2021/day4/day4Boards.txt') as f:
    boards = f.read().split('\n\n')

boards = []

for board in boards:
    board.split('\n')
    print(board)
