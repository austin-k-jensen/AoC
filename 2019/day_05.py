from collections import defaultdict
from aocd import get_data

YEAR, DAY = 2019, 5
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "1,9,10,3,2,3,11,0,99,30,40,50"
TEST_2 = "1,0,0,0,99"
TEST_3 = "2,3,0,3,99"
TEST_4 = "2,4,4,5,99,0"
TEST_5 = "1,1,1,4,99,5,6,0,99"
TEST_6 = "1002,4,3,4,33"
TEST_7 = "1101,100,-1,4,0"
TEST_8 = "3,0,4,0,99"
TEST_9 = "3,225,1,225,6,6,1100,1,238,225,104,0,99"


def parse(data: str):
    program = defaultdict(int)
    for i, code in enumerate(data.split(",")):
        program[i] = int(code)
    return program


def parse_instruction(instruction: int):
    op_code = instruction % 100
    param_1_mode = instruction // 100 % 10
    param_2_mode = instruction // 1000 % 10
    param_3_mode = instruction // 10000 % 10

    return op_code, param_1_mode, param_2_mode, param_3_mode


def get_param(memory: defaultdict, address: int, param_mode: int, inc: int):
    if param_mode:
        param = memory[address + inc]
    else:
        param = memory[memory[address + inc]]

    return param


def op_1(memory: defaultdict, address: int, param_1_mode: int, param_2_mode: int):
    param_1 = get_param(memory, address, param_1_mode, 1)
    param_2 = get_param(memory, address, param_2_mode, 2)

    memory[memory[address + 3]] = param_1 + param_2
    address += 4

    return memory, address


def op_2(memory: defaultdict, address: int, param_1_mode: int, param_2_mode: int):
    param_1 = get_param(memory, address, param_1_mode, 1)
    param_2 = get_param(memory, address, param_2_mode, 2)

    memory[memory[address + 3]] = param_1 * param_2
    address += 4

    return memory, address


def op_3(memory: defaultdict, address: int, input: int):
    memory[memory[address + 1]] = input
    address += 2

    return memory, address


def op_4(memory: defaultdict, address: int, param_1_mode: int):
    param_1 = get_param(memory, address, param_1_mode, 1)
    print("Output:", param_1)
    address += 2

    return address


def run_program(program: defaultdict, input: int = 0):
    address = 0
    memory = program.copy()

    while True:
        op_code, param_1_mode, param_2_mode, param_3_mode = parse_instruction(
            memory[address]
        )
        # print(memory[address], op_code)

        if op_code == 99:
            break
        elif op_code == 1:
            memory, address = op_1(memory, address, param_1_mode, param_2_mode)
        elif op_code == 2:
            memory, address = op_2(memory, address, param_1_mode, param_2_mode)
        elif op_code == 3:
            memory, address = op_3(memory, address, input)
        elif op_code == 4:
            address = op_4(memory, address, param_1_mode)
        else:
            print("error")
            break
        # print(memory)

    return memory


program = parse(puzzle)
# print(program)
run_program(program, 1)
