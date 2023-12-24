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


def part_2_seq(start, grid):
    # history = [part_2_wrap(start, 65 + i * 131, grid) for i in range(4)]

    steps = 458
    cnt = 3
    history = [2722, 25621, 71435, 140107]
    while steps < 26501365:
        steps += 131
        cnt += 1

        checks = []
        while not all(i == 0 for i in history):
            checks.append(history)
            next = []
            for i in range(len(history) - 1):
                next.append(history[i + 1] - history[i])
            history = next
        for i in range(len(checks) - 1, 0, -1):
            checks[i - 1].append(checks[i - 1][-1] + checks[i][-1])

        history = checks[0]
    print(steps, cnt, checks[0][-1])


start, grid = parse(puzzle)
# print("part 1: ", part_1(start, 64, grid))
# part_2_wrap(start, 100, grid)
# part_2_analysis(start, grid)
# part_2_seq(start, grid)
