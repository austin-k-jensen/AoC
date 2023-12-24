import re
from itertools import combinations
import numpy as np
import sympy
from aocd import get_data

YEAR, DAY = 2023, 24
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""


def part_1(data):
    stones = []
    for stone in data.strip().splitlines():
        stone = [int(coord) for coord in re.findall(r"(-?\d+)", stone)]
        stones.append(stone)

    cnt = 0
    # bounds = (7, 27)
    bounds = (200000000000000, 400000000000000)
    for (x1, y1, _, vx1, vy1, _), (x2, y2, _, vx2, vy2, _) in combinations(stones, 2):
        A = np.array([[vx1, vx2 * -1], [vy1, vy2 * -1]])
        b = np.array([x2 - x1, y2 - y1])
        try:
            ts = np.linalg.solve(A, b)
            px, py = x1 + vx1 * ts[0], y1 + vy1 * ts[0]
            if (
                ts[0] > 0
                and ts[1] > 0
                and bounds[0] <= px <= bounds[1]
                and bounds[0] <= py <= bounds[1]
            ):
                cnt += 1
        except:
            pass
    print("part 1: ", cnt)


def part_2(data):
    xr = sympy.Symbol("xr")
    yr = sympy.Symbol("yr")
    zr = sympy.Symbol("zr")
    vxr = sympy.Symbol("vxr")
    vyr = sympy.Symbol("vyr")
    vzr = sympy.Symbol("vzr")
    t1 = sympy.Symbol("t1")
    t2 = sympy.Symbol("t2")
    t3 = sympy.Symbol("t3")

    stones = data.strip().splitlines()[:3]

    x1, y1, z1, vx1, vy1, vz1 = [
        int(coord) for coord in re.findall(r"(-?\d+)", stones[0])
    ]
    x2, y2, z2, vx2, vy2, vz2 = [
        int(coord) for coord in re.findall(r"(-?\d+)", stones[1])
    ]
    x3, y3, z3, vx3, vy3, vz3 = [
        int(coord) for coord in re.findall(r"(-?\d+)", stones[2])
    ]

    xeq1 = xr + vxr * t1 - x1 - vx1 * t1
    yeq1 = yr + vyr * t1 - y1 - vy1 * t1
    zeq1 = zr + vzr * t1 - z1 - vz1 * t1
    xeq2 = xr + vxr * t2 - x2 - vx2 * t2
    yeq2 = yr + vyr * t2 - y2 - vy2 * t2
    zeq2 = zr + vzr * t2 - z2 - vz2 * t2
    xeq3 = xr + vxr * t3 - x3 - vx3 * t3
    yeq3 = yr + vyr * t3 - y3 - vy3 * t3
    zeq3 = zr + vzr * t3 - z3 - vz3 * t3

    solve = sympy.solve_poly_system(
        [xeq1, yeq1, zeq1, xeq2, yeq2, zeq2, xeq3, yeq3, zeq3],
        [xr, yr, zr, vxr, vyr, vzr, t1, t2, t3],
    )[0]
    print("part 2: ", solve[0] + solve[1] + solve[2])


part_1(puzzle)
part_2(puzzle)
