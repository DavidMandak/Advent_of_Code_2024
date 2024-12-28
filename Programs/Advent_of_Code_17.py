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

a = int("5600137262025050", 8)
diff = (2**51-2**48)//10000000
diff = 1
length = 0
i = 1
sequences = []
seq = ""
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
    if output[:-1] == check:
        print(a)
        print(output)
        exit()
    if output[:-1] == check[len(check)-len(output)+1:] and len(output) > length:
        print(oct(a))
        print(output)
    a += diff
pattern = str(sequences)[1:-1].replace("\'", "").replace(", ", "")

i = 0
seq += output[0]
if i == 8:
    if seq in sequences:
        print(seq)
        print(sequences)
        #break
    else:
        sequences.append(seq)
    seq = ""
    i = 0
i += 1
# Previous: 1619150575507484
# Current: 1619150575632384
# output[-26:-1] == "1,7,5,1,4,0,3,4,5,5,5,3,0"
