import re
from itertools import combinations
import numpy as np
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
    print(cnt)


part_1(puzzle)
