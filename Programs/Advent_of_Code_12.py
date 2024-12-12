lines = open("../Inputs/Advent_of_Code_12.txt").read().splitlines()


def f(crop, x, y):
    global area, perimeter, lines
    dx, dy = 1, 0
    lines[y] = lines[y][:x]+lines[y][x].casefold()+lines[y][x+1:]
    for _ in range(4):
        next_x = x+dx
        next_y = y+dy
        if 0 <= next_x < len(lines[0]) and 0 <= next_y < len(lines):
            if lines[next_y][next_x] == crop:
                f(crop, x+dx, y+dy)
                area += 1
            elif crop.casefold() != lines[next_y][next_x]:
                perimeter += 1
        else:
            perimeter += 1
        temp = dy
        dy = -1*dx
        dx = temp


total = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if ord(lines[y][x]) < 91:
            area = 1
            perimeter = 0
            f(lines[y][x], x, y)
            total += area*perimeter
print(total)
