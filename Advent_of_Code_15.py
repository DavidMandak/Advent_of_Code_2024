strings = open("Advent_of_Code_15.txt").read().split(",")
total = 0
current = 0
for string in strings:
    for character in string:
        current += ord(character)
        current *= 17
        current %= 256
    total += current
    current = 0
print(total)
