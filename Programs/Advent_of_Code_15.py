import copy
warehouse, moves = open("../Inputs/Advent_of_Code_15.txt").read().split("\n\n")
warehouse = list(map(list, warehouse.splitlines()))
save = copy.deepcopy(warehouse)
moves = moves.replace("\n", "")

start_x, start_y = 4, 4
warehouse[start_y][start_x] = "."
for move in moves:
    if move == "^":
        dx, dy = 0, -1
    elif move == ">":
        dx, dy = 1, 0
    elif move == "<":
        dx, dy = -1, 0
    else:
        dx, dy = 0, 1
    x, y = start_x+dx, start_y+dy
    if warehouse[y][x] == ".":
        start_x, start_y = x, y
    elif warehouse[y][x] == "O":
        i = 1
        while warehouse[y+i*dy][x+i*dx] != "#":
            if warehouse[y+i*dy][x+i*dx] == ".":
                warehouse[y+i*dy][x+i*dx] = "O"
                warehouse[y][x] = "."
                start_x, start_y = x, y
                break
            i += 1
total = 0
for y in range(1, len(warehouse)-1):
    for x in range(1, len(warehouse[y])-1):
        if warehouse[y][x] == "O":
            total += 100*y+x
print(total)

warehouse = save
start_x, start_y = 0, 0
for y in range(len(warehouse)):
    for x in range(0, 2*len(warehouse[y]), 2):
        tile = warehouse[y][x]
        if tile == "#":
            warehouse[y].insert(x, "#")
        elif tile == ".":
            warehouse[y].insert(x, ".")
        elif tile == "O":
            warehouse[y][x] = "]"
            warehouse[y].insert(x, "[")
        else:
            start_x, start_y = x, y
            warehouse[y][x] = "."
            warehouse[y].insert(x, ".")


def horizontal(x, y, dx):
    global warehouse
    tile = warehouse[y][x]
    if tile == "#":
        return False
    elif tile == ".":
        return True
    elif horizontal(x+dx, y, dx):
        warehouse[y][x+dx] = warehouse[y][x+dx]
        warehouse[y][x+dx] = tile
        return True
    return False


def vertical(x, y, dy):
    global warehouse
    tile = warehouse[y][x]
    if tile == "#":
        return False
    elif tile == ".":
        return True
    elif tile == "[":
        k = 1
    else:
        k = -1
    if vertical(x, y+dy, dy) and vertical(x+k, y+dy, dy):
        warehouse[y+dy][x] = warehouse[y][x]
        warehouse[y+dy][x+k] = warehouse[y][x+k]
        warehouse[y][x+k] = "."
        return True
    return False


for move in moves:
    if move == "^":
        dx, dy = 0, -1
    elif move == ">":
        dx, dy = 1, 0
    elif move == "<":
        dx, dy = -1, 0
    else:
        dx, dy = 0, 1
    x, y = start_x+dx, start_y+dy
    if warehouse[y][x] == ".":
        start_x, start_y = x, y
    elif warehouse[y][x] == "[" or warehouse[y][x] == "]":
        if move == ">" or move == "<":
            if horizontal(x, y, dx):
                warehouse[y][x] = "."
                start_x, start_y = x, y
        elif vertical(x, y, dy):
            warehouse[y][x] = "."
            start_x, start_y = x, y
total = 0
for y in range(1, len(warehouse)-1):
    for x in range(2, len(warehouse[y])-2):
        if warehouse[y][x] == "[":
            total += 100*y+x
print(total)

for line in warehouse:
    for tile in line:
        print(tile, end="")
    print()
print()