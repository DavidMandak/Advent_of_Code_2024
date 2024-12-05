from collections import defaultdict
lines = open("../Inputs/Advent_of_Code_05.txt").read().split("\n\n")

rules = defaultdict(list)
pairs = lines[0].splitlines()
updates = lines[1].splitlines()
for pair in pairs:
    a, b = map(int, pair.split("|"))
    rules[a].append(b)

total = 0
for update in updates:
    line = list(map(int, update.split(",")))
    check = [line[0]]
    good = True
    for num in line[1:]:
        for x in rules[num]:
            if x in check:
                good = False
        if good is False:
            break
        check.append(num)
    if good is True:
        total += line[len(line)//2]
print(total)
