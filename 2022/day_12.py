from heapq import heappush, heappop
from aocd import get_data

YEAR, DAY = 2022, 12
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def parse(data):
    rows = data.strip().split()
    grid = {}
    for i, row in enumerate(rows):
        for j, hight in enumerate(row):
            if hight == "S":
                start = (i, j)
                grid[(i, j)] = 0
            elif hight == "E":
                goal = (i, j)
                grid[(i, j)] = 25
            else:
                grid[(i, j)] = ord(hight) - 97
    return start, goal, grid


def part_1(start, goal, grid):
    edge = max(grid)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    check = [(0, start, (0, 0))]
    visited = set()

    while check:
        steps, loc, in_dir = heappop(check)

        if loc == goal:
            return steps

        if (loc, in_dir) in visited:
            continue

        visited.add((loc, in_dir))

        for dir in dirs:
            new_loc = (loc[0] + dir[0], loc[1] + dir[1])
            if (0 <= new_loc[0] <= edge[0]) and (0 <= new_loc[1] <= edge[1]):
                if grid[new_loc] <= grid[loc] + 1:
                    heappush(check, (steps + 1, new_loc, dir))


def part_2(goal, grid):
    starts = [loc for loc, height in grid.items() if height == 0]
    steps = []
    for start in starts:
        steps.append(part_1(start, goal, grid))
    print("part 2: ", min(x for x in steps if x is not None))


start, goal, grid = parse(puzzle)
print("part 1: ", part_1(start, goal, grid))
part_2(goal, grid)
