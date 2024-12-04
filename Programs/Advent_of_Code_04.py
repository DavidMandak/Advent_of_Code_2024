lines = open("../Inputs/test.txt").read().splitlines()


def check(x, y, string):
  global total
  if lines[y][x:x+4] == string:
    total += 1
  for a, b in directions:
    if all(lines[y+i*a][x+i*a] == string[i] for i in range(1, 4)):
      total += 1


directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
total = 0
for y in range(len(lines)):
  for x in range(len(lines[0]))
    if lines[y][x] == "X":
      check(x, y, "XMAS")
    elif lines[y][x] == "S":
      check(x, y, "SAMX")
print(total)
