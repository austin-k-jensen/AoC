from collections import defaultdict
from aocd import get_data

YEAR, DAY = 2019, 9
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
TEST_2 = "1102,34915192,34915192,7,4,7,99,0"
TEST_3 = "104,1125899906842624,99"


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


def op_3(memory: defaultdict, address: int, input: list):

    if len(input) > 0:
        input = input.pop(0)
        memory[memory[address + 1]] = input
        address += 2
    else:
        print("Input to short")
        address = None

    return memory, address


def op_4(memory: defaultdict, address: int, param_1_mode: int):
    param_1 = get_param(memory, address, param_1_mode, 1)
    address += 2

    return address, param_1


def op_5(memory: defaultdict, address: int, param_1_mode: int, param_2_mode: int):
    param_1 = get_param(memory, address, param_1_mode, 1)
    param_2 = get_param(memory, address, param_2_mode, 2)
    if param_1 != 0:
        address = param_2
    else:
        address += 3

    return address


def op_6(memory: defaultdict, address: int, param_1_mode: int, param_2_mode: int):
    param_1 = get_param(memory, address, param_1_mode, 1)
    param_2 = get_param(memory, address, param_2_mode, 2)
    if param_1 == 0:
        address = param_2
    else:
        address += 3

    return address


def op_7(memory: defaultdict, address: int, param_1_mode: int, param_2_mode: int):
    param_1 = get_param(memory, address, param_1_mode, 1)
    param_2 = get_param(memory, address, param_2_mode, 2)

    if param_1 < param_2:
        out = 1
    else:
        out = 0

    memory[memory[address + 3]] = out
    address += 4

    return memory, address


def op_8(memory: defaultdict, address: int, param_1_mode: int, param_2_mode: int):
    param_1 = get_param(memory, address, param_1_mode, 1)
    param_2 = get_param(memory, address, param_2_mode, 2)

    if param_1 == param_2:
        out = 1
    else:
        out = 0

    memory[memory[address + 3]] = out
    address += 4

    return memory, address


def run_program(
    memory: defaultdict, address: int = 0, rel_base: int = 0, input: list = []
):
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
            address, output = op_4(memory, address, param_1_mode)
            # print("Output:", output)
            return output, memory, address, rel_base
        elif op_code == 5:
            address = op_5(memory, address, param_1_mode, param_2_mode)
        elif op_code == 6:
            address = op_6(memory, address, param_1_mode, param_2_mode)
        elif op_code == 7:
            memory, address = op_7(memory, address, param_1_mode, param_2_mode)
        elif op_code == 8:
            memory, address = op_8(memory, address, param_1_mode, param_2_mode)
        else:
            print("error")

        # print(memory)

    return None, memory, address, rel_base


program = parse(puzzle)
