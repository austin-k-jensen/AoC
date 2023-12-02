"""AOC 2023 Day 3"""
import re
from aocd import get_data
from aocd import submit  # pylint: disable=no-name-in-module

YEAR, DAY = 2023, 3
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
"""


def part_1(data, sub: bool = False):
    """Part 1 Function"""
    p1_answer = 0

    print("part 1: ", p1_answer)

    if sub:
        submit(p1_answer, part="a", year=YEAR, day=DAY)


part_1(TEST_1, sub=False)


def part_2(data, sub: bool = False):
    """Part 2 Function"""
    p2_answer = 0

    print("part 2: ", p2_answer)

    if sub:
        submit(p2_answer, part="b", year=YEAR, day=DAY)


# part_2(TEST_1, sub=False)
