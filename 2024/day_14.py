import re
from itertools import combinations
from math import sqrt
from aocd import get_data
from utils import timing


YEAR, DAY = 2024, 14
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


@timing
def parse(data: str):
    robots = []

    for robot in data.strip().splitlines():
        numbers = [int(x) for x in re.findall(r"-?\d+", robot)]
        robots.append(((numbers[0], numbers[1]), (numbers[2], numbers[3]))),

    return robots


@timing
def part_1(robots: list, edge: tuple, seconds: int):
    quads = {1: 0, 2: 0, 3: 0, 4: 0}

    X, Y = edge

    for p, v in robots:
        new_x = (p[0] + v[0] * seconds) % X
        new_y = (p[1] + v[1] * seconds) % Y

        if new_x < X // 2 and new_y < Y // 2:
            quads[1] += 1
        elif new_x > X // 2 and new_y < Y // 2:
            quads[2] += 1
        elif new_x < X // 2 and new_y > Y // 2:
            quads[3] += 1
        elif new_x > X // 2 and new_y > Y // 2:
            quads[4] += 1

    return quads[1] * quads[2] * quads[3] * quads[4]


@timing
def part_2(robots: list, edge: tuple, max_seconds: int):
    entropies = {}
    X, Y = edge

    for sec in range(1, max_seconds + 1):
        positions = []
        for p, v in robots:
            positions.append(((p[0] + v[0] * sec) % X, (p[1] + v[1] * sec) % Y))

        entropy = 0
        for (x1, y1), (x2, y2) in combinations(positions, 2):
            entropy += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        entropies[entropy] = (sec, positions)

    time, positions = entropies[min(entropies)]

    # print(time, positions)

    for y in range(Y):
        row = ""
        for x in range(X):
            if (x, y) in positions:
                row += "#"
            else:
                row += "."
        print(row)

    return time


robots = parse(puzzle)
# robots = [((2, 4), (2, -3))]
# part_1(robots, (11, 7), 100)
# print("part 1: ", part_1(robots, (101, 103), 100))
print("part 2: ", part_2(robots, (101, 103), 6000))
