from aocd import get_data
import re

YEAR, DAY = 2025, 1
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def parse(data):
    moves = [(dir, int(dist)) for (dir, dist) in re.findall(r"([RL])(\d+)", data)]
    return moves


def part_1(moves):
    pos = 50
    count = 0

    for dir, dist in moves:
        if dir == "L":
            pos -= dist
            pos = pos % 100
        elif dir == "R":
            pos += dist
            pos = pos % 100

        if pos == 0:
            count += 1

    return count


def part_2(moves):
    pos = 50
    count = 0

    for dir, dist in moves:

        if dir == "L":
            for _ in range(dist):
                pos -= 1
                pos = pos % 100
                if pos == 0:
                    count += 1

        elif dir == "R":
            for _ in range(dist):
                pos += 1
                pos = pos % 100
                if pos == 0:
                    count += 1

    return count


moves = parse(puzzle)
print("part 1: ", part_1(moves))
print("part 2: ", part_2(moves))
