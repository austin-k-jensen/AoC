import re
from aocd import get_data

YEAR, DAY = 2024, 3
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
TEST_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def part_1(data):
    instructions = re.findall(r"mul\((\d+),(\d+)\)", data)

    tot = 0

    for instruction in instructions:
        tot += int(instruction[0]) * int(instruction[1])

    return tot


def part_2(data):
    instructions = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", data)

    enable = True
    tot = 0

    for instruction in instructions:
        if instruction == "don't()":
            enable = False
        elif instruction == "do()":
            enable = True
        elif instruction[0:3] == "mul" and enable:
            nums = re.findall(r"(\d+),(\d+)", instruction)[0]
            tot += int(nums[0]) * int(nums[1])

    return tot


print("part 1: ", part_1(puzzle))
print("part 2: ", part_2(puzzle))
