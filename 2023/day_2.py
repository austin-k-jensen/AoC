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
    for line in iter(input.splitlines()):
        game = re.findall(r"(\d+):", line)
        draws = re.findall(r"(\d+) ([rbg])", line)

        for draw in draws:
            if (
                (draw[1] == "r" and int(draw[0]) > 12)
                or (draw[1] == "g" and int(draw[0]) > 13)
                or (draw[1] == "b" and int(draw[0]) > 14)
            ):
                game[0] = 0

        P1_ANSWER += int(game[0])

    print("part 1: ", P1_ANSWER)

    if sub:
        submit(P1_ANSWER, part="a", year=YEAR, day=DAY)


part_1(puzzle, sub=False)


def part_2(input, sub: bool = False):
    P2_ANSWER = 0
    for line in iter(input.splitlines()):
        draws = re.findall(r"(\d+) ([rbg])", line)

        r_max = 0
        b_max = 0
        g_max = 0

        for draw in draws:
            if draw[1] == "r":
                if int(draw[0]) > r_max:
                    r_max = int(draw[0])
            if draw[1] == "b":
                if int(draw[0]) > b_max:
                    b_max = int(draw[0])
            if draw[1] == "g":
                if int(draw[0]) > g_max:
                    g_max = int(draw[0])

        P2_ANSWER += r_max * b_max * g_max

    print("part 2: ", P2_ANSWER)

    if sub:
        submit(P2_ANSWER, part="b", year=YEAR, day=DAY)


part_2(puzzle, sub=False)
