"""AOC 2023 Day 1"""
import re
from aocd import get_data
from aocd import submit


YEAR, DAY = 2023, 1
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

TEST_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def part_1(data, sub: bool = False):
    """Part 1 Function"""
    p1_answer = 0
    for line in iter(data.splitlines()):
        nums = re.findall(r"\d", line)
        p1_answer += int(nums[0] + nums[-1])
    print("part 1: ", p1_answer)

    if sub:
        submit(p1_answer, part="a", year=YEAR, day=DAY)


part_1(puzzle, sub=False)


def part_2(data, sub: bool = False):
    """Part 2 Function"""
    key = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    p2_answer = 0
    for line in iter(data.splitlines()):
        nums = re.findall(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
        )
        for i in enumerate(nums):
            nums[i[0]] = key[nums[i[0]]] if nums[i[0]] in key else nums[i[0]]
        p2_answer += int(nums[0] + nums[-1])
    print("part 2: ", p2_answer)

    if sub:
        submit(p2_answer, part="b", year=YEAR, day=DAY)


part_2(puzzle, sub=False)
