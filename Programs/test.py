import copy
lines = ["89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732"
]

for y in range(len(lines)):
    lines[y] = list(map(int, lines[y]))
save = copy.deepcopy(lines)


def f():
    save[0][0] += 1


f()
print(lines)
print(save)
