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


def run_program(registers, program):
    pointer = 0
    run = True
    ops = 0

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

    return out


@timing
def part_1(registers, program):
    output = ",".join(map(str, run_program(registers, program)))
    return output


def find_bit(program, ub, step, matches):
    new_ub = ub
    for _ in range(8):
        registers["A"], registers["B"], registers["C"] = new_ub, 0, 0
        check = run_program(registers, program)

        if check == program:
            matches.append(new_ub)
            break

        if len(check) != len(program):
            break

        if check[step] == program[step]:
            find_bit(program, new_ub, step - 1, matches)

        new_ub -= 8**step


@timing
def part_2(program):
    end = 8 ** (len(program)) - 1

    matches = []
    find_bit(program, end, len(program) - 1, matches)

    return min(matches)


registers, program = parse(puzzle)
print("part 1: ", part_1(registers, program))
print("part 2: ", part_2(program))
