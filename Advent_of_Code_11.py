lines = open("Advent_of_Code_11.txt").read().splitlines()
galaxies = []
y_empty = []
empty_line = 30
total = 0
x_empty = []
for y in range(0, len(lines)):
    if lines[y] == lines[empty_line]:
        y_empty.append(y)


def column(x):
    for y in range(0, len(lines)):
        if lines[y][x] != ".":
            return False
    return True


for x in range(0, len(lines[0])):
    if column(x) is True:
        x_empty.append(x)
for y in range(0, len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "#":
            galaxies.append([x, y])
i = 1
for galaxy in galaxies:
    for j in range(i, len(galaxies)):
        destination = galaxies[j]
        total += abs(galaxy[0]-destination[0])+abs(galaxy[1]-destination[1])
    i += 1
print(total)
