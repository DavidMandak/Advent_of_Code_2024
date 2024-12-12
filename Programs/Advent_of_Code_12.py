lines = open("../Inputs/Advent_of_Code_12.txt").read().splitlines()


def f(crop, x, y):
    global total
    dx, dy = 1, 0
    for _ in range(4):
        if 0 <= x+dx < len(lines[0]) and 0 <= y+dy < len(lines) and lines[y+dy][x+dx] == crop:
            f(crop, x+dx, y+dy)
            area += 1



for