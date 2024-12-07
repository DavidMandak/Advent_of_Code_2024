lines = open("../Inputs/Advent_of_Code_07.txt").read().splitlines()


def f(pos, value):
    global total
    if pos == len(numbers):
        if value == result:
            total += result
            return True
    elif f(pos+1, value*numbers[pos]) or f(pos+1, value+numbers[pos]) or f(pos+1, int(str(value)+str(numbers[pos]))):
        return True


total = 0
for line in lines:
    line = line.split(": ")
    result = int(line[0])
    numbers = list(map(int, line[1].split()))
    f(1, numbers[0])
print(total)
