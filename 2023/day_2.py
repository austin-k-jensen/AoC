"""AOC 2023 Day 2"""
import re
from aocd import get_data
from aocd import submit  # pylint: disable=no-name-in-module


YEAR, DAY = 2023, 2
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def part_1(data, sub: bool = False):
    """Part 1 Function"""
    p1_answer = 0
    p2_answer = 0
    for line in iter(data.splitlines()):
        game = int(re.findall(r"(\d+):", line)[0])
        r = max([int(cube) for cube in re.findall(r"(\d+) r", line)])
        b = max([int(cube) for cube in re.findall(r"(\d+) b", line)])
        g = max([int(cube) for cube in re.findall(r"(\d+) g", line)])

        if r > 12 or g > 13 or b > 14:
            pass
        else:
            p1_answer += game

        p2_answer += r * b * g

    print("part 1: ", p1_answer)
    print("part 2: ", p2_answer)

    if sub:
        submit(p1_answer, part="a", year=YEAR, day=DAY)
        submit(p2_answer, part="b", year=YEAR, day=DAY)


part_1(puzzle, sub=False)
