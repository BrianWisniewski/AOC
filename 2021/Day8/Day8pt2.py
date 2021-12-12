total = 0

# PART 1: Assign
with open("2021\Day8\day8.txt") as f:
    datas = f.read().split("\n")

for data in datas:

    # PART 2: Train
    trainAll = data.split(" | ")[0]
    train = trainAll.split()
    asignments = {}
    counts = {}
    for letter in "abcdefg":
        counts[letter] = trainAll.count(letter)

    for key, value in counts.items():
        if value == 4:
            asignments[5] = key
        elif value == 6:
            asignments[2] = key
        elif value == 9:
            asignments[6] = key

    for i in train:
        if len(i) == 2:
            one = i
        elif len(i) == 4:
            four = i
        elif len(i) == 3:
            seven = i

    if one[0] in asignments.values():
        asignments[3] = one[1]
    else:
        asignments[3] = one[0]

    for letter in seven:
        if letter not in one:
            asignments[1] = letter

    for letter in four:
        if letter not in asignments.values():
            asignments[4] = letter

    for letter in "abcdefg":
        if letter not in asignments.values():
            asignments[7] = letter

    # PART 3: Test
    test = data.split(" | ")[1].split()
    num = ""
    for set in test:
        if len(set) == 2:
            num += "1"
        elif len(set) == 3:
            num += "7"
        elif len(set) == 4:
            num += "4"
        elif len(set) == 7:
            num += "8"
        elif len(set) == 6:
            if asignments.get(4) not in set:
                num += "0"
            elif asignments.get(5) not in set:
                num += "9"
            else:
                num += "6"
        elif len(set) == 5:
            if asignments.get(2) in set:
                num += "5"
            elif asignments.get(5) not in set:
                num += "3"
            else:
                num += "2"
    total += int(num)
    print(num, asignments, data)
print(total)
