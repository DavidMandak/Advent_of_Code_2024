from collections import defaultdict
lines = open("../Inputs/Advent_of_Code_23.txt").read().splitlines()

total = 0
neighbours = defaultdict(list)
for pair in lines:
    a, b = pair.split("-")
    neighbours[a].append(b)
    neighbours[b].append(a)
groups = []
for pc in neighbours:
    if pc[0] == "t":
        for neighbour in neighbours[pc]:
            for third in neighbours[neighbour]:
                if pc in neighbours[third] and {pc:0, neighbour:0, third:0} not in groups:
                    groups.append({pc:0, neighbour:0, third:0})
                    total += 1
print(total)
