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


def part_2_wrap(start, grid):
    edge = max(grid)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    check = [start]

    for _ in range(100):
        reached = []
        for _ in range(len(check)):
            loc = check.pop()
            for dir in dirs:
                new_loc = (loc[0] + dir[0], loc[1] + dir[1])

                check_x = new_loc[0] % edge[0]
                if check_x < 1:
                    check_x += edge[0]

                check_y = new_loc[1] % edge[1]
                if check_y < 1:
                    check_y += edge[1]

                check_loc = (check_x, check_y)

                if (0 <= check_loc[0] <= edge[0]) and (0 <= check_loc[1] <= edge[1]):
                    if grid[check_loc] == ".":
                        reached.append(new_loc)
        check = list(set(reached))

    print(len(check))


def part_2_analysis(start, grid):
    steps = 26501365
    h, w = max(grid)[0] + 1, max(grid)[1] + 1
    print(h, w)
    grids = (steps - start[0]) // w
    print(grids)
    even = part_1(start, 3 * w, grid)
    odd = part_1(start, 3 * w + 1, grid)
    print(even, odd)
    big_corner_steps = (3 * w - 3) // 2
    little_corner_steps = (w - 3) // 2
    big_corner = (
        part_1((0, 0), big_corner_steps, grid)
        + part_1((0, h - 1), big_corner_steps, grid)
        + part_1((w - 1, 0), big_corner_steps, grid)
        + part_1((w - 1, h - 1), big_corner_steps, grid)
    )
    little_corner = (
        part_1((0, 0), little_corner_steps, grid)
        + part_1((0, h - 1), little_corner_steps, grid)
        + part_1((w - 1, 0), little_corner_steps, grid)
        + part_1((w - 1, h - 1), little_corner_steps, grid)
    )
    print(big_corner, little_corner)
    tips = (
        part_1((0, start[1]), w, grid)
        + part_1((start[0], 0), w, grid)
        + part_1((w - 1, start[1]), w, grid)
        + part_1((start[0], h - 1), w, grid)
    )
    print(tips)

    dests = (
        ((grids - 1) ** 2) * odd
        + (grids**2) * even
        + (grids - 1) * big_corner
        + grids * little_corner
        + tips
    )

    print(dests)


start, grid = parse(puzzle)
print("part 1: ", part_1(start, 64, grid))
# part_2_wrap(start, grid)
part_2_analysis(start, grid)
