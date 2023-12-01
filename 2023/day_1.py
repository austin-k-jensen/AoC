from aocd import get_data
from aocd import submit
import re

YEAR, DAY = 2023, 1
puzzle = get_data(day=DAY, year=YEAR)

test1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

test2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def part_1(input, submit: bool = False):
    P1_ANSWER = 0
    for line in iter(input.splitlines()):
        nums = re.findall(r"\d", line)
        P1_ANSWER += int(nums[0] + nums[-1])
    print("part 1: ", P1_ANSWER)

    if submit:
        submit(P1_ANSWER, part="a", year=YEAR, day=DAY)


part_1(puzzle, submit=False)


def part_2(input, submit: bool = False):
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
    P2_ANSWER = 0
    for line in iter(input.splitlines()):
        nums = re.findall(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
        )
        for i in range(len(nums)):
            nums[i] = key[nums[i]] if nums[i] in key.keys() else nums[i]
        P2_ANSWER += int(nums[0] + nums[-1])
    print("part 2: ", P2_ANSWER)

    if submit:
        submit(P2_ANSWER, part="b", year=YEAR, day=DAY)


part_2(puzzle, submit=False)
