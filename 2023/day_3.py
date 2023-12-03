"""AOC 2023 Day 3"""
import re
from aocd import get_data
from aocd import submit

YEAR, DAY = 2023, 3
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def part_1(data, sub: bool = False):
    """Part 1 Function"""
    p1_answer = 0
    y = 0
    symbol_pos = []
    num_pos = []
    for line in iter(data.splitlines()):
        symbol_xs = [m.start() for m in re.finditer(r"[^.\d\s]", line)]
        for x in symbol_xs:
            symbol_pos.append((y, x))

        num_xs = [m.start() for m in re.finditer(r"\d+", line)]
        nums = re.findall(r"(\d+)", line)
        for i in range(len(nums)):
            num_end = num_xs[i] + len(nums[i])
            start = (max(y - 1, 0), max(num_xs[i] - 1, 0))
            end = (y + 1, num_end)
            num_pos.append((int(nums[i]), start, end))

        y += 1

    for num in num_pos:
        for sym in symbol_pos:
            # print(num[1], num[2], sym)
            if (
                num[1][0] <= sym[0]
                and num[2][0] >= sym[0]
                and num[1][1] <= sym[1]
                and num[2][1] >= sym[1]
            ):
                p1_answer += num[0]

    print("part 1: ", p1_answer)

    if sub:
        submit(p1_answer, part="a", year=YEAR, day=DAY)


part_1(puzzle, sub=False)


def part_2(data, sub: bool = False):
    """Part 2 Function"""
    p2_answer = 0

    y = 0
    symbol_pos = []
    num_pos = []
    for line in iter(data.splitlines()):
        symbol_xs = [m.start() for m in re.finditer(r"\*", line)]
        for x in symbol_xs:
            symbol_pos.append((y, x))

        num_xs = [m.start() for m in re.finditer(r"\d+", line)]
        nums = re.findall(r"(\d+)", line)
        for i in range(len(nums)):
            num_end = num_xs[i] + len(nums[i])
            start = (max(y - 1, 0), max(num_xs[i] - 1, 0))
            end = (y + 1, num_end)
            num_pos.append((int(nums[i]), start, end))

        y += 1

    for sym in symbol_pos:
        nums = []
        for num in num_pos:
            if (
                num[1][0] <= sym[0]
                and num[2][0] >= sym[0]
                and num[1][1] <= sym[1]
                and num[2][1] >= sym[1]
            ):
                nums.append(num[0])
        if len(nums) == 2:
            p2_answer += nums[0] * nums[1]

    print("part 2: ", p2_answer)

    if sub:
        submit(p2_answer, part="b", year=YEAR, day=DAY)


part_2(puzzle, sub=False)
