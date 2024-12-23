lines = open("../Inputs/Advent_of_Code_21.txt").read().splitlines()
pad = {
    "7":(0, 0), "8":(1, 0), "9":(2, 0),
    "4":(0, 1), "5":(1, 1), "6":(2, 1),
    "1":(0, 2), "2":(1, 2), "3":(2, 2),
    "A":(2, 3), "0":(1, 3),
    "0,-1":(1, 0), "0,0":(2, 0),
    "-1,0":(0, 1), "0,1":(1, 1), "1,0":(2, 1)
}
total = 0
for line in lines:
    px, py = 2, 3
    code = line
    for _ in range(3):
        ey = py
        path = ""
        for num in code:
            x, y = pad[num]
            diff_x = x-px
            diff_y = y-py
            if px == 0 and y == ey or (diff_x < 0 and (x != 0 or py != ey)):
                if diff_x != 0:
                    path += f"{diff_x//abs(diff_x)},0 "*abs(diff_x)
                if diff_y != 0:
                    path += f"0,{diff_y//abs(diff_y)} "*abs(diff_y)
                path += "0,0 "
            else:
                if diff_y != 0:
                    path += f"0,{diff_y//abs(diff_y)} "*abs(diff_y)
                if diff_x != 0:
                    path += f"{diff_x//abs(diff_x)},0 "*abs(diff_x)
                path += "0,0 "
            px, py = x, y
        code = path.split()
        px, py = 2, 0
    total += len(path.split())*int(line[:-1])
print(total)

memo = {depth: {} for depth in range(26)}
total = 0
for line in lines:
    px, py = 2, 3
    code = [button+" " for button in line]
    for _ in range(26):
        result = ""
        ey = py
        for seg in code:
            if seg not in memo[_]:
                path = ""
                for num in seg.split():
                    x, y = pad[num]
                    diff_x = x-px
                    diff_y = y-py
                    if px == 0 and y == ey or (diff_x < 0 and (x != 0 or py != ey)):
                        if diff_x != 0:
                            path += f"{diff_x//abs(diff_x)},0 "*abs(diff_x)
                        if diff_y != 0:
                            path += f"0,{diff_y//abs(diff_y)} "*abs(diff_y)
                        path += "0,0 "
                    else:
                        if diff_y != 0:
                            path += f"0,{diff_y//abs(diff_y)} "*abs(diff_y)
                        if diff_x != 0:
                            path += f"{diff_x//abs(diff_x)},0 "*abs(diff_x)
                        path += "0,0 "
                    px, py = x, y
                if _ != 0:
                    memo[_][seg] = path
                result += path
            else:
                result += memo[_][seg]
        code = [seg+"0,0" for seg in result.split("0,0 ")]
        px, py = 2, 0
    total += (len(result.split())-2)*int(line[:-1])
    print("done")
print(total)

for direction in result.split():
    if direction == "1,0":
        print(">", end="")
    elif direction == "-1,0":
        print("<", end="")
    elif direction == "0,-1":
        print("^", end="")
    elif direction == "0,1":
        print("v", end="")
    else:
        print("A", end="")
print()
