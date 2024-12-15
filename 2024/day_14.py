import re
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
def part_2(robots: list, edge: tuple, time_range: tuple):
    scores = {}
    X, Y = edge

    start, stop = time_range

    for sec in range(start, stop + 1):
        positions = []
        quads = {1: 0, 2: 0, 3: 0, 4: 0}
        for p, v in robots:

            new_x = (p[0] + v[0] * sec) % X
            new_y = (p[1] + v[1] * sec) % Y

            if new_x < X // 2 and new_y < Y // 2:
                quads[1] += 1
            elif new_x > X // 2 and new_y < Y // 2:
                quads[2] += 1
            elif new_x < X // 2 and new_y > Y // 2:
                quads[3] += 1
            elif new_x > X // 2 and new_y > Y // 2:
                quads[4] += 1

            positions.append((new_x, new_y))

        scores[quads[1] * quads[2] * quads[3] * quads[4]] = (sec, positions)

    time, positions = scores[min(scores)]

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
print("part 1: ", part_1(robots, (101, 103), 100))
print("part 2: ", part_2(robots, (101, 103), (1, 10000)))
