import re
from aocd import get_data

YEAR, DAY = 2019, 3
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
R8,U5,L5,D3
U7,R6,D4,L4
"""

TEST_2 = """
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
"""

TEST_3 = """
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
"""


def parse(data: str):
    wires = []
    for wire in data.strip().splitlines():
        moves = re.findall(r"(R|U|L|D)(\d+)", wire)
        wires.append(moves)

    return wires


def part_1(wires: list):
    dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    points = []
    for wire in wires:
        loc = (0, 0)
        point = []
        for dir, num in wire:
            for _ in range(int(num)):
                loc = (loc[0] + dirs[dir][0], loc[1] + dirs[dir][1])
                point.append(loc)
        points.append(point)

    crosses = list(set(points[0]) & set(points[1]))

    min = 1 * 10**9
    for cross in crosses:
        dist = abs(cross[0]) + abs(cross[1])
        if dist < min:
            min = dist
    return min


def part_2(wires: list):
    dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    points = []
    for wire in wires:
        loc = (0, 0)
        steps = 0
        point = {}
        for dir, num in wire:
            for _ in range(int(num)):
                loc = (loc[0] + dirs[dir][0], loc[1] + dirs[dir][1])
                steps += 1
                if loc not in point:
                    point[loc] = steps
        points.append(point)

    min = 1 * 10**9
    for point in points[0]:
        if point in points[1]:
            steps = points[0][point] + points[1][point]
            if steps < min:
                min = steps
    return min


wires = parse(puzzle)
print("Part 1: ", part_1(wires))
print("Part 2: ", part_2(wires))
