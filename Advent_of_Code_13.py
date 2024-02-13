patterns = open("Advent_of_Code_13.txt").read().split("\n\n")
practise = ["#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.",
            "#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#"
]

vertical = 0
horizontal = 0


def search(grid, axis):
    for i in range(1, len(grid)):
        if grid[i] == grid[i-1]:
            if len(grid)-i < i:
                if check(i, len(grid)-i, grid, axis) is not False:
                    return True
            else:
                if check(i, i, grid, axis) is not False:
                    return True


def check(i, size, grid, axis):
    global horizontal, vertical
    for y in range(1, size+1):
        if grid[i+y-1] != grid[i-y]:
            return False
    if axis == "y":
        vertical += i
    else:
        horizontal += i


for pattern in patterns:
    pattern = pattern.splitlines()
    if search(pattern, "x") is not True:
        columns = []
        for x in range(0, len(pattern[0])):
            column = ""
            for y in range(0, len(pattern)):
                column += pattern[y][x]
            columns.append(column)
        search(columns, "y")
print(vertical+100*horizontal)
