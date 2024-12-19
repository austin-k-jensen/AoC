from functools import cache
from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 19
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""


def parse(data: str):
    patterns, designs = data.strip().split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.splitlines()
    return patterns, designs


@cache
def check_designs(design: str):
    possible = 0
    for pattern in patterns:
        if pattern == design:
            possible += 1
        elif design[: len(pattern)] == pattern:
            possible += check_designs(design[len(pattern) :])
        else:
            continue
    return possible


@timing
def both(designs: list):
    tot = 0
    tot_2 = 0
    for design in designs:
        out = check_designs(design)
        tot_2 += out
        if out > 0:
            tot += 1
    return tot, tot_2


global patterns
patterns, designs = parse(puzzle)
part_1, part_2 = both(designs)
print("part 1: ", part_1)
print("part 2: ", part_2)
