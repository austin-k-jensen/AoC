from collections import defaultdict
from aocd import get_data

YEAR, DAY = 2019, 2
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "1,9,10,3,2,3,11,0,99,30,40,50"
TEST_2 = "1,0,0,0,99"
TEST_3 = "2,3,0,3,99"
TEST_4 = "2,4,4,5,99,0"
TEST_5 = "1,1,1,4,99,5,6,0,99"


def parse(data: str):
    program = defaultdict(int)
    for i, code in enumerate(data.split(",")):
        program[i] = int(code)
    return program


def run_program(program: defaultdict):
    address = 0
    while True:
        opcode = program[address]
        # print(address, opcode)

        if opcode == 99:
            break
        elif opcode == 1:
            program[program[address + 3]] = (
                program[program[address + 1]] + program[program[address + 2]]
            )
        elif opcode == 2:
            program[program[address + 3]] = (
                program[program[address + 1]] * program[program[address + 2]]
            )

        address += 4

    return program


def part_1(program: defaultdict):
    mem = program.copy()
    mem[1] = 12
    mem[2] = 2
    mem = run_program(mem)
    return mem[0]


def part_2(program: defaultdict):
    for noun in range(100):
        for verb in range(100):
            mem = program.copy()
            mem[1] = noun
            mem[2] = verb
            mem = run_program(mem)
            if mem[0] == 19690720:
                return 100 * noun + verb


program = parse(puzzle)
print("Part 1: ", part_1(program))
print("Part 2: ", part_2(program))
