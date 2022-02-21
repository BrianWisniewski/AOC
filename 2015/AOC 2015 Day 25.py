row = 3
col = 2
last = 20151125


def regen(last):
    return (last * 252533) % 33554393


for tmpRow in range(row):
    for tmpCol in range(tmpRow + 1):
        tmp = last
        last = regen(last)
        if tmpRow + 1 == row and tmpCol + 1 == col:
            break


print(last)
