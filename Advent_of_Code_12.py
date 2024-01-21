lines = open("Advent_of_Code_12.txt").read().splitlines()
springs = []
records = []
total = 0
for line in lines:
    line = line.split(" ")
    springs.append(((line[0]+"?")*5)[:-1])
    record = line[1].split(",")*5
    for i in range(0, len(record)):
        record[i] = int(record[i])
    records.append(record)


def generate(j, place, row, record):
    if place == count:
        check(row, record)
    else:
        store = row
        for i in range(j, len(unknown)-count+1+place):
            row = store
            index = unknown[i]
            row = row[:index]+"#"+row[index+1:]
            if memoization(row, index, record) is False:
                continue
            generate(i+1, place+1, row, record)


def memoization(row, index, record):
    a = 0
    sequence = None
    checking = False
    for i in range(0, index+1):
        spring = row[i]
        if checking is True:
            if spring == "#":
                sequence -= 1
            elif sequence == 0:
                checking = False
                a += 1
            else:
                return False
        elif spring == "#":
            checking = True
            sequence = record[a]-1
    if sequence < 0:
        return False


def check(row, record):
    global total
    row += "."
    a = 0
    sequence = None
    checking = False
    for spring in row:
        if checking is True:
            if spring == "#":
                sequence -= 1
            elif sequence < 0:
                return
            elif sequence == 0:
                checking = False
                a += 1
            else:
                return
        elif spring == "#":
            checking = True
            sequence = record[a]-1
    total += 1


for i in range(0, len(lines)):
    row = springs[i]
    count = 0
    for num in records[i]:
        count += num
    unknown = []
    for j in range(0, len(row)):
        if row[j] == "#":
            count -= 1
        elif row[j] == "?":
            unknown.append(j)
    generate(0, 0, springs[i], records[i])
    break
print(total)
