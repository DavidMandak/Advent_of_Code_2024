import re, math
lines = open("Advent_of_Code_8.txt").read().splitlines()
instructions = lines[0]
nodes = {}
for i in range(2, len(lines)):
    group = re.split(" = \(|, |\)", lines[i])
    nodes[group[0]] = (group[1], group[2])
starts = []
for node in nodes:
    if node[-1] == "A":
        starts.append(node)


def loop(pos):
    global steps, x
    for instruction in instructions:
        if instruction == "L":
            instruction = 0
        else:
            instruction = 1
        destination = nodes[pos][instruction]
        if destination[-1] == "Z":
            ends.append(steps)
            return False
        pos = destination
        steps += 1
    x = pos
    return True


x = None
ends = []
for pos in starts:
    steps = 1
    while loop(pos):
        pos = x
print(math.lcm(ends[0], ends[1], ends[2], ends[3], ends[4], ends[5]))
