lines = open("Advent_of_Code_12.txt").read().splitlines()
springs = []
records = []
total = 0
for line in lines:
    line = line.split(" ")
    springs.append(line[0])
    record = line[1].split(",")
    for i in range(0, len(record)):
        record[i] = int(record[i])
    records.append(record)


def generate(j, place, row):
    if place == count:
        print(row)
        check(row)
    else:
        store = row
        for i in range(j, len(unknown)-count+1+place):
            row = store
            index = unknown[i]
            row = row[:index] + "#" + row[index+1:]
            generate(i+1, place+1, row)


def check(row):
    global total
    a = 0
    sequence = None
    checking = False
    for spring in row:
        if checking is True:
            if spring == "#":
                sequence -= 1
            elif sequence == 0:
                checking = False
                a += 1
            else:
                return
        elif spring == "#":
            checking = True
            sequence = records[0][a]-1
    total += 1


row = springs[0]
count = 0
for num in records[0]:
    count += num
unknown = []
for i in range(0, len(row)):
    if row[i] == "#":
        count -= 1
    elif row[i] == "?":
        unknown.append(i)
for i in range(0, len(unknown)-count+1):
    row = springs[0]
    index = unknown[i]
    row = row[:index]+"#"+row[index+1:]
    generate(i+1, 1, row)
print(total)
