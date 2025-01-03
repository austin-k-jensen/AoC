from itertools import permutations
from collections import defaultdict
from aocd import get_data

YEAR, DAY = 2019, 7
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
TEST_2 = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
TEST_3 = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
TEST_4 = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"


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


def run_program(memory: defaultdict, address: int = 0, input: list = []):
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
            return output, memory, address
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
            return None

        # print(memory)

    return None, memory, address


def part_1(program: defaultdict):
    best = 0
    for signal in permutations([0, 1, 2, 3, 4], 5):
        in_val = 0
        for val in signal:
            input = [val, in_val]
            memory = program.copy()
            in_val, _, _ = run_program(memory=memory, input=input)

        if in_val > best:
            best = in_val

    return best


def part_2(program: defaultdict):
    best = 0
    for signal in permutations([5, 6, 7, 8, 9], 5):
        mems = [
            program.copy(),
            program.copy(),
            program.copy(),
            program.copy(),
            program.copy(),
        ]
        adds = [0, 0, 0, 0, 0]
        ins = [[i] for i in signal]

        i = 0
        ins[i] = ins[i] + [0]
        last_out = None

        while True:
            input = ins[i]
            out, mems[i], adds[i] = run_program(
                memory=mems[i], address=adds[i], input=input
            )

            if out == None:
                if last_out > best:
                    best = last_out
                break

            last_out = out
            i = (i + 1) % 5
            ins[i] = ins[i] + [out]

    return best


program = parse(puzzle)
print("Part 1: ", part_1(program))
print("Part 2: ", part_2(program))
