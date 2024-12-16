import copy

maze = open("../Inputs/test.txt").read().splitlines()
save = copy.deepcopy(maze)


def move(x, y, dx, dy, visited, score):
    pass


total = 0
move(2, len(maze)-2, 1, 0, save, 0)