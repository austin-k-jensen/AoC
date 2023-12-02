from aocd import get_data
from aocd import submit
import re

YEAR, DAY = 2023, 2
puzzle = get_data(day=DAY, year=YEAR)

test1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def part_1(input, sub: bool = False):
    P1_ANSWER = 0
    P2_ANSWER = 0
    for line in iter(input.splitlines()):
        game = int(re.findall(r"(\d+):", line)[0])
        r = max([int(cube) for cube in re.findall(r"(\d+) r", line)])
        b = max([int(cube) for cube in re.findall(r"(\d+) b", line)])
        g = max([int(cube) for cube in re.findall(r"(\d+) g", line)])

        if r > 12 or g > 13 or b > 14:
            pass
        else:
            P1_ANSWER += game

        P2_ANSWER += r * b * g

    print("part 1: ", P1_ANSWER)
    print("part 2: ", P2_ANSWER)

    if sub:
        submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
        submit(P2_ANSWER, part="b", year=YEAR, day=DAY)


part_1(puzzle, sub=False)
