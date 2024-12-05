from collections import defaultdict
lines = open("../Inputs/test.txt").read().split("\n\n")

rules = defaultdict(list)
pairs = lines[0].splitlines()
updates = lines[1].splitlines()
for pair in pairs:
    a, b = map(int, pair.split("|"))
    rules[b].append(a)

total = 0
for update in updates:
    line = map(int, update.split(","))
    check = [line[0]]
    for num in line[1:]:
        for x in rules[num]:
            if x in check:
              total -= 1
              break
