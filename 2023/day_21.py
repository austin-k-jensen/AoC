import numpy as np
from aocd import get_data

YEAR, DAY = 2023, 21
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""


def parse(data):
    rows = data.strip().split()
    grid = {}
    for i, row in enumerate(rows):
        for j, typ in enumerate(row):
            if typ == "S":
                start = (i, j)
                grid[(i, j)] = "."
            else:
                grid[(i, j)] = typ
    return start, grid


def part_1(start, steps, grid):
    edge = max(grid)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    check = [start]

    for _ in range(steps):
        reached = []
        for _ in range(len(check)):
            loc = check.pop()
            for dir in dirs:
                new_loc = (loc[0] + dir[0], loc[1] + dir[1])
                if (0 <= new_loc[0] <= edge[0]) and (0 <= new_loc[1] <= edge[1]):
                    if grid[new_loc] == ".":
                        reached.append(new_loc)
        check = list(set(reached))

    return len(check)


def part_2_wrap(start, steps, grid):
    edge = max(grid)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    check = [start]

    for _ in range(steps):
        reached = []
        for _ in range(len(check)):
            loc = check.pop()
            for dir in dirs:
                new_loc = (loc[0] + dir[0], loc[1] + dir[1])

                check_x = (new_loc[0] + 1) % (edge[0] + 1)
                if check_x < 1:
                    check_x += edge[0] + 1

                check_y = (new_loc[1] + 1) % (edge[1] + 1)
                if check_y < 1:
                    check_y += edge[1] + 1

                check_loc = (check_x - 1, check_y - 1)

                if (0 <= check_loc[0] <= edge[0]) and (0 <= check_loc[1] <= edge[1]):
                    if grid[check_loc] == ".":
                        reached.append(new_loc)
        check = list(set(reached))

    return len(check)


def part_2_analysis(start, grid):
    steps = 26501365
    h, w = max(grid)[0] + 1, max(grid)[1] + 1
    print(h, w)
    grids = (steps - start[0]) // w
    rem = steps - grids * w
    print(grids, rem)
    even = part_2_wrap(start, 3 * w, grid)
    odd = part_2_wrap(start, 3 * w + 1, grid)
    print(even, odd)
    big_corner_steps = w + rem - 1
    little_corner_steps = rem
    big_corner = (
        part_2_wrap((0, 0), big_corner_steps, grid)
        + part_2_wrap((0, h - 1), big_corner_steps, grid)
        + part_2_wrap((w - 1, 0), big_corner_steps, grid)
        + part_2_wrap((w - 1, h - 1), big_corner_steps, grid)
    )
    little_corner = (
        part_2_wrap((0, 0), little_corner_steps, grid)
        + part_2_wrap((0, h - 1), little_corner_steps, grid)
        + part_2_wrap((w - 1, 0), little_corner_steps, grid)
        + part_2_wrap((w - 1, h - 1), little_corner_steps, grid)
    )
    print(big_corner, little_corner)
    tips = (
        part_2_wrap((0, start[1]), w - 1, grid)
        + part_2_wrap((start[0], 0), w - 1, grid)
        + part_2_wrap((w - 1, start[1]), w - 1, grid)
        + part_2_wrap((start[0], h - 1), w - 1, grid)
    )
    print(tips)

    dests = (
        ((grids - 1) ** 2) * odd
        + (grids**2) * even
        + (grids - 1) * big_corner
        + grids * little_corner
        + tips
    )

    print("part 2: ", dests)


def part_2_quad(start, steps, grid):
    h, w = max(grid)[0] + 1, max(grid)[1] + 1
    grids = (steps - start[0]) // w

    b0 = part_2_wrap(start, start[0], grid)
    b1 = part_2_wrap(start, start[0] + w, grid)
    b2 = part_2_wrap(start, start[0] + w * 2, grid)

    A = np.matrix([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
    b = np.array([b0, b1, b2])

    x = np.linalg.solve(A, b).astype(np.int64)
    print("part 2:", x[0] * grids**2 + x[1] * grids + x[2])


start, grid = parse(puzzle)
print("part 1: ", part_1(start, 64, grid))
part_2_quad(start, 26501365, grid)
