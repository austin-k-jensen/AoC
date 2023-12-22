import re
from collections import defaultdict
from aocd import get_data

YEAR, DAY = 2023, 22
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
1,0,1~1,2,1
0,2,3~2,2,3
0,0,4~0,2,4
1,1,8~1,1,9
2,0,5~2,2,5
0,0,2~2,0,2
0,1,6~2,1,6
"""


def parse(data):
    bricks = []
    for brick in data.strip().splitlines():
        brick = [int(coord) for coord in re.findall(r"(\d+)", brick)]
        bricks.append(brick)
    bricks = sorted(bricks, key=lambda x: x[2])
    return bricks


def stack(bricks):
    tops = defaultdict(int)
    stack = []
    is_stable = []
    for x1, y1, z1, x2, y2, z2 in bricks:
        top = []
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                top.append(tops[(x, y)])
        top = max(top) + 1
        if z1 == top:
            is_stable.append(True)
        else:
            is_stable.append(False)
        stack.append([x1, y1, top, x2, y2, top + z2 - z1])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                tops[(x, y)] = top + z2 - z1
    return stack, is_stable


def day_22(bricks):
    init_stack, _ = stack(bricks)

    stable = 0
    unstable = 0
    for i in range(len(init_stack)):
        test_stack = init_stack[:i] + init_stack[i + 1 :]
        _, is_stable = stack(test_stack)
        unstable += is_stable.count(False)
        if all(is_stable):
            stable += 1

    print("part 1: ", stable, "\npart 2: ", unstable)


bricks = parse(puzzle)
day_22(bricks)
