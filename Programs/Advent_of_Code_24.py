values, lines = open("../Inputs/Advent_of_Code_24.txt").read().split("\n\n")
lines = [line.split() for line in lines.splitlines()]
wires = {name:int(value) for name, value in [(start.split(": ")) for start in values.splitlines()]}


def check(wires, lines):
    total = []
    while len(lines) > 0:
        for inp1, gate, inp2, _, out in lines:
            if inp1 in wires and inp2 in wires:
                if gate == "AND":
                    if wires[inp1]+wires[inp2] == 2:
                        save = 1
                    else:
                        save = 0
                elif gate == "OR":
                    if wires[inp1]+wires[inp2] >= 1:
                        save = 1
                    else:
                        save = 0
                else:
                    if wires[inp1]+wires[inp2] == 1:
                        save = 1
                    else:
                        save = 0
                wires[out] = save
                if out[0] == "z":
                    i = int(out[1:])
                    if i >= len(total):
                        total.extend([None]*(i-len(total)))
                        total.append(save)
                    else:
                        total[i] = save
                lines.remove([inp1, gate, inp2, _, out])
    return int(str(list(reversed(total)))[1:-1].replace(", ", ""), 2)


print(check(wires.copy(), lines.copy()))
