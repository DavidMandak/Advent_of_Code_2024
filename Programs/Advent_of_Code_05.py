from collections import defaultdict
input = open("../Inputs/Advent_of_Code_05").read().splitlines().split("")

rules = defaultdict(list)
pairs = input[0]
updates = input[1]

for a, b in map(int, pairs.split("|")):
  rules[b].append(a)

for update in updates:
  ...
