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
                start = (i + 1, j + 1)
                grid[(i + 1, j + 1)] = "."
            else:
                grid[(i + 1, j + 1)] = typ
    return start, grid


def part_1(start, grid):
    edge = max(grid)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    check = [start]

    for _ in range(64):
        reached = []
        for _ in range(len(check)):
            loc = check.pop()
            for dir in dirs:
                new_loc = (loc[0] + dir[0], loc[1] + dir[1])
                if (1 <= new_loc[0] <= edge[0]) and (1 <= new_loc[1] <= edge[1]):
                    if grid[new_loc] == ".":
                        reached.append(new_loc)
        check = list(set(reached))

    print("part 1: ", len(check))


def part_2(start, grid):
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

                if (1 <= check_loc[0] <= edge[0]) and (1 <= check_loc[1] <= edge[1]):
                    if grid[check_loc] == ".":
                        reached.append(new_loc)
        check = list(set(reached))

    print(len(check))


start, grid = parse(TEST_1)
part_1(start, grid)
part_2(start, grid)
