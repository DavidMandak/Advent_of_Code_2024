registers, program = open("../Inputs/Advent_of_Code_17.txt").read().split("\n\n")
registers = registers.splitlines()
for i in range(3):
    registers[i] = int(registers[i].split(": ")[1])
check = program.split(": ")[1][:-1]
program = list(map(int, program.split(": ")[1].split(",")))


def adv(operand, register):
    global registers
    combo_operand = operand if operand <= 3 else registers[operand-4]
    registers[register] = registers[0]//(2**combo_operand)


def bxl(operand):
    global registers
    registers[1] = registers[1] ^ operand


def bst(operand):
    global registers
    combo_operand = operand if operand <= 3 else registers[operand-4]
    registers[1] = combo_operand % 8


def jnz(operand):
    global registers, pos
    if registers[0] != 0:
        pos = operand-2

def bxc():
    global registers
    registers[1] = registers[1] ^ registers[2]


def out(operand):
    global registers, output
    combo_operand = operand if operand <= 3 else registers[operand-4]
    output += str(combo_operand % 8)+","


output = ""
pos = 0
while pos < len(program):
    instruction = program[pos]
    oper = program[pos+1]
    if instruction == 1:
        bxl(oper)
    elif instruction == 2:
        bst(oper)
    elif instruction == 3:
        jnz(oper)
    elif instruction == 4:
        bxc()
    elif instruction == 5:
        out(oper)
    else:
        adv(oper, instruction % 5)
    pos += 2
print(output[:-1])

a = 1619150575632384
diff = (2**51-2**48)//10000000
diff = -1
length = 0
while output[:-1] != check:
    registers = [a, 0, 0]
    output = ""
    pos = 0
    while pos < len(program):
        instruction = program[pos]
        oper = program[pos+1]
        if instruction == 1:
            bxl(oper)
        elif instruction == 2:
            bst(oper)
        elif instruction == 3:
            jnz(oper)
        elif instruction == 4:
            bxc()
        elif instruction == 5:
            out(oper)
        else:
            adv(oper, instruction % 5)
        pos += 2
    if output[-26:-1] == "1,7,5,1,4,0,3,4,5,5,5,3,0":
        print(a)
        print(output)
        exit()
    if len(output[:-1]) > length:
        print(a, length//2+1)
        length = len(output[:-1])
    print(output)
    a += diff
print(a+1)

if output[-4:-1] == "3,0":
    print(a)
    print(output)
    exit()

# Previous: 1619150575507484
# Current: 1619150575632384
