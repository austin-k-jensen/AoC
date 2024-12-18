from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 17
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

TEST_2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""


def parse(data):
    register_lines, program_line = data.strip().split("\n\n")

    registers = {}
    for line in register_lines.splitlines():
        registers[line.split()[1][0]] = int(line.split(" ")[2])

    program = [int(x) for x in program_line.split()[1].split(",")]

    return registers, program


def part_1(registers, program):
    pointer = 0
    run = True
    ops = 0

    # print(program)

    out = []
    while run:
        combo_dict = {
            0: 0,
            1: 1,
            2: 3,
            3: 3,
            4: registers["A"],
            5: registers["B"],
            6: registers["C"],
            7: "inv",
        }
        # print(f"\tPointer: {pointer}")

        if pointer > (len(program) - 1):
            break
        instruction = program[pointer]
        operand = program[pointer + 1]

        # print(f"\t\tinstruction: {instruction}")
        # print(f"\t\toperand: {operand}")
        # print(f"\t\tcombo: {combo_dict[operand]}")
        # print(f"\t\tregisters: {registers}")

        if instruction == 0:
            registers["A"] = registers["A"] // (2 ** combo_dict[operand])

        elif instruction == 1:
            registers["B"] = registers["B"] ^ operand

        elif instruction == 2:
            registers["B"] = combo_dict[operand] % 8

        elif instruction == 3:
            if registers["A"] == 0:
                pointer += 2
                continue
            else:
                pointer = operand
                continue

        elif instruction == 4:
            registers["B"] = registers["B"] ^ registers["C"]

        elif instruction == 5:
            out.append(combo_dict[operand] % 8)

        elif instruction == 6:
            registers["B"] = registers["A"] // (2 ** combo_dict[operand])

        elif instruction == 7:
            registers["C"] = registers["A"] // (2 ** combo_dict[operand])

        pointer += 2
        ops += 1
        # run = False if ops == 100 else True
    # print(f"registers: {registers}")
    # print(f"Output:{out}")
    return out


def find_bit(program, ub, step, matches):
    # print(program, ub, step)
    new_ub = ub
    for _ in range(8):
        # print(new_ub)
        registers["A"], registers["B"], registers["C"] = new_ub, 0, 0
        check = part_1(registers, program)
        # print(check)
        # print(check[step])
        if check == program:
            matches.append(new_ub)
            break
        if len(check) != len(program):
            break
        if check[step] == program[step]:
            # print(check)
            find_bit(program, new_ub, step - 1, matches)
        new_ub -= 8**step


@timing
def part_2(registers, program):

    start = 8 ** (len(program) - 1)
    end = 8 ** (len(program)) - 1
    # print(start, end)

    matches = []
    find_bit(program, end, len(program) - 1, matches)
    print(min(matches))

    # new_end = end
    # for i in range(len(program) - 1, 14, -1):
    #     print(i)
    #     for _ in range(8):
    #         registers["A"], registers["B"], registers["C"] = new_end, 0, 0
    #         out = part_1(registers, program)
    #         if out[i] == program[i]:
    #             # print(f"{registers['A']}: {out[i]}")
    #             new_start = new_end - 8**i + 1
    #             break
    #         new_end = new_end - 8**i

    # print(new_end - new_start)
    # print(program[14:])

    # registers["A"], registers["B"], registers["C"] = new_start - 1, 0, 0
    # print(registers)
    # print(part_1(registers, program))

    # registers["A"], registers["B"], registers["C"] = new_start, 0, 0
    # print(registers)
    # print(part_1(registers, program))

    # registers["A"], registers["B"], registers["C"] = new_end, 0, 0
    # print(registers)
    # print(part_1(registers, program))

    # registers["A"], registers["B"], registers["C"] = new_end + 1, 0, 0
    # print(registers)
    # print(part_1(registers, program))

    # a = new_start
    # last_a = new_start
    # for a in range(0, 8**3 + 1):
    #     registers["A"], registers["B"], registers["C"] = a, 0, 0
    #     print(f"{a}: {part_1(registers, program)}")
    # while True:
    #     registers["A"], registers["B"], registers["C"] = a, 0, 0
    #     # print(f"{a}: {part_1(registers, program)}")
    #     check = part_1(registers, program)
    #     if check == program:
    #         print(a)
    #         break
    #     if check[13:] == program[13:]:
    #         print(a, a - last_a, check)
    #         last_a = a
    #     a += 1


registers, program = parse(puzzle)
# print("part 1: ", part_1(registers, program))
part_2(registers, program)

# TEST_2 = """
# Register A: 0
# Register B: 0
# Register C: 9

# Program: 2,6
# """
# registers, program = parse(TEST_2)
# part_1(registers, program)

########################################################

# TEST_3 = """
# Register A: 10
# Register B: 0
# Register C: 0

# Program: 5,0,5,1,5,4
# """
# registers, program = parse(TEST_3)
# part_1(registers, program)

########################################################

# TEST_4 = """
# Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0
# """
# registers, program = parse(TEST_4)
# part_1(registers, program)

########################################################

# TEST_5 = """
# Register A: 0
# Register B: 29
# Register C: 0

# Program: 1,7
# """
# registers, program = parse(TEST_5)
# part_1(registers, program)

########################################################

# TEST_6 = """
# Register A: 0
# Register B: 2024
# Register C: 43690

# Program: 4,0
# """
# registers, program = parse(TEST_6)
# part_1(registers, program)
