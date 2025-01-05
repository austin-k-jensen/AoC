from collections import defaultdict
from aocd import get_data

YEAR, DAY = 2019, 11
puzzle = get_data(day=DAY, year=YEAR)


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


def get_param(
    memory: defaultdict, address: int, rel_base: int, param_mode: int, inc: int
):
    if param_mode == 0:
        param = memory[memory[address + inc]]
    elif param_mode == 1:
        param = memory[address + inc]
    elif param_mode == 2:
        param = memory[memory[address + inc] + rel_base]
    else:
        print("Error: Invalid Param Mode")

    return param


def op_1(
    memory: defaultdict,
    address: int,
    rel_base: int,
    param_1_mode: int,
    param_2_mode: int,
    param_3_mode: int,
):
    param_1 = get_param(memory, address, rel_base, param_1_mode, 1)
    param_2 = get_param(memory, address, rel_base, param_2_mode, 2)
    inc = rel_base if param_3_mode == 2 else 0

    memory[memory[address + 3] + inc] = param_1 + param_2
    address += 4

    return memory, address


def op_2(
    memory: defaultdict,
    address: int,
    rel_base: int,
    param_1_mode: int,
    param_2_mode: int,
    param_3_mode: int,
):
    param_1 = get_param(memory, address, rel_base, param_1_mode, 1)
    param_2 = get_param(memory, address, rel_base, param_2_mode, 2)
    inc = rel_base if param_3_mode == 2 else 0

    memory[memory[address + 3] + inc] = param_1 * param_2
    address += 4

    return memory, address


def op_3(
    memory: defaultdict, address: int, rel_base: int, param_1_mode: int, input: list
):
    inc = rel_base if param_1_mode == 2 else 0

    if len(input) > 0:
        input = input.pop(0)
        memory[memory[address + 1] + inc] = input
        address += 2
    else:
        print("Input to short")
        address = None

    return memory, address


def op_4(memory: defaultdict, address: int, rel_base: int, param_1_mode: int):
    param_1 = get_param(memory, address, rel_base, param_1_mode, 1)
    address += 2

    return address, param_1


def op_5(
    memory: defaultdict,
    address: int,
    rel_base: int,
    param_1_mode: int,
    param_2_mode: int,
):
    param_1 = get_param(memory, address, rel_base, param_1_mode, 1)
    param_2 = get_param(memory, address, rel_base, param_2_mode, 2)
    if param_1 != 0:
        address = param_2
    else:
        address += 3

    return address


def op_6(
    memory: defaultdict,
    address: int,
    rel_base: int,
    param_1_mode: int,
    param_2_mode: int,
):
    param_1 = get_param(memory, address, rel_base, param_1_mode, 1)
    param_2 = get_param(memory, address, rel_base, param_2_mode, 2)
    if param_1 == 0:
        address = param_2
    else:
        address += 3

    return address


def op_7(
    memory: defaultdict,
    address: int,
    rel_base: int,
    param_1_mode: int,
    param_2_mode: int,
    param_3_mode: int,
):
    param_1 = get_param(memory, address, rel_base, param_1_mode, 1)
    param_2 = get_param(memory, address, rel_base, param_2_mode, 2)
    inc = rel_base if param_3_mode == 2 else 0

    if param_1 < param_2:
        out = 1
    else:
        out = 0

    memory[memory[address + 3] + inc] = out
    address += 4

    return memory, address


def op_8(
    memory: defaultdict,
    address: int,
    rel_base: int,
    param_1_mode: int,
    param_2_mode: int,
    param_3_mode: int,
):
    param_1 = get_param(memory, address, rel_base, param_1_mode, 1)
    param_2 = get_param(memory, address, rel_base, param_2_mode, 2)
    inc = rel_base if param_3_mode == 2 else 0

    if param_1 == param_2:
        out = 1
    else:
        out = 0

    memory[memory[address + 3] + inc] = out
    address += 4

    return memory, address


def op_9(memory: defaultdict, address: int, rel_base: int, param_1_mode: int):
    param_1 = get_param(memory, address, rel_base, param_1_mode, 1)

    rel_base += param_1
    address += 2

    # print("\tNew rel_base:", rel_base)

    return memory, address, rel_base


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
            memory, address = op_1(
                memory, address, rel_base, param_1_mode, param_2_mode, param_3_mode
            )
        elif op_code == 2:
            memory, address = op_2(
                memory, address, rel_base, param_1_mode, param_2_mode, param_3_mode
            )
        elif op_code == 3:
            memory, address = op_3(memory, address, rel_base, param_1_mode, input)
        elif op_code == 4:
            address, output = op_4(memory, address, rel_base, param_1_mode)
            # print("Output:", output)
            return output, memory, address, rel_base
        elif op_code == 5:
            address = op_5(memory, address, rel_base, param_1_mode, param_2_mode)
        elif op_code == 6:
            address = op_6(memory, address, rel_base, param_1_mode, param_2_mode)
        elif op_code == 7:
            memory, address = op_7(
                memory, address, rel_base, param_1_mode, param_2_mode, param_3_mode
            )
        elif op_code == 8:
            memory, address = op_8(
                memory, address, rel_base, param_1_mode, param_2_mode, param_3_mode
            )
        elif op_code == 9:
            memory, address, rel_base = op_9(memory, address, rel_base, param_1_mode)
        else:
            print("error")
            return None, memory, address, rel_base

        # print(memory)

    return None, memory, address, rel_base


def part_1(program: defaultdict, start_col: int = 0):

    memory = program.copy()
    address = 0
    rel_base = 0
    input = []
    visited = defaultdict(lambda: 0)
    loc = (0, 0)
    dir = (0, -1)

    visited[loc] = start_col

    turn_dir = {
        (0, -1): {0: (-1, 0), 1: (1, 0)},
        (1, 0): {0: (0, -1), 1: (0, 1)},
        (0, 1): {0: (1, 0), 1: (-1, 0)},
        (-1, 0): {0: (0, 1), 1: (0, -1)},
    }

    step = 0
    while True:
        # print(
        #     f"Step: {step}. Starting loc: {loc}. Starting dir: {dir}. Starting color: {visited[loc]}"
        # )

        if step % 2 == 0:
            input.append(visited[loc])

        output, memory, address, rel_base = run_program(
            memory, address, rel_base, input
        )

        if output == None:
            break

        if step % 2 == 0 and output == 1:
            visited[loc] = 1
            # print(f"\tOutput: {output}. Painted White")
        elif step % 2 == 0 and output == 0:
            visited[loc] = 0
            # print(f"\tOutput: {output}. Painted Black")
        if step % 2 == 1 and output == 1:
            dir = turn_dir[dir][output]
            loc = (loc[0] + dir[0], loc[1] + dir[1])
            # print(f"\tOutput: {output}. Turned right. New loc: {loc}. New dir: {dir}")
        elif step % 2 == 1 and output == 0:
            # visited[loc] = 0
            dir = turn_dir[dir][output]
            loc = (loc[0] + dir[0], loc[1] + dir[1])
            # print(f"\tOutput: {output}. Turned right. New loc: {loc}. New dir: {dir}")

        step += 1

    return visited


def part_2(program: defaultdict):
    grid = part_1(program, 1)
    max_x = 0
    max_y = 0

    for x, y in grid:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    print("Part 2:")
    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            if grid[(x, y)] == 1:
                line += "#"
            else:
                line += " "
        print("\t", line)


program = parse(puzzle)
print("Part 1: ", len(part_1(program, 0)))
part_2(program)
