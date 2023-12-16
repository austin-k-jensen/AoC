from aocd import get_data

YEAR, DAY = 2023, 16
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""


dir_map = {
    ".": {(1, 0): [(1, 0)], (-1, 0): [(-1, 0)], (0, 1): [(0, 1)], (0, -1): [(0, -1)]},
    "\\": {(1, 0): [(0, 1)], (-1, 0): [(0, -1)], (0, 1): [(1, 0)], (0, -1): [(-1, 0)]},
    "/": {(1, 0): [(0, -1)], (-1, 0): [(0, 1)], (0, 1): [(-1, 0)], (0, -1): [(1, 0)]},
    "|": {
        (1, 0): [(0, 1), (0, -1)],
        (-1, 0): [(0, 1), (0, -1)],
        (0, 1): [(0, 1)],
        (0, -1): [(0, -1)],
    },
    "-": {
        (1, 0): [(1, 0)],
        (-1, 0): [(-1, 0)],
        (0, 1): [(1, 0), (-1, 0)],
        (0, -1): [(1, 0), (-1, 0)],
    },
}


def count_energized(rows, start):
    check = [start]
    visited = set()

    x_max, y_max = len(rows[0]), len(rows)

    while check:
        loc, in_dir = check.pop()
        if (loc, in_dir) in visited:
            continue
        if not (0 <= loc[0] < x_max and 0 <= loc[1] < y_max):
            continue
        visited.add((loc, in_dir))

        sym = rows[loc[1]][loc[0]]
        out_dir = dir_map[sym][in_dir]

        for d in out_dir:
            next_loc = (loc[0] + d[0], loc[1] + d[1])
            check.append((next_loc, d))

    energized = len(set([step[0] for step in visited]))

    return energized


def part_1(data):
    rows = data.split()
    start = ((0, 0), (1, 0))
    print("part 1: ", count_energized(rows, start))


def part_2(data):
    rows = data.split()
    x_max, y_max = len(rows[0]), len(rows)

    starts = []

    for x in range(x_max):
        starts.append(((x, 0), (0, 1)))
        starts.append(((x, y_max - 1), (0, -1)))

    for y in range(y_max):
        starts.append(((0, y), (1, 0)))
        starts.append(((x_max - 1, y), (-1, 0)))

    energized = []

    for start in starts:
        energized.append(count_energized(rows, start))

    print("part 2: ", max(energized))


part_1(puzzle)
part_2(puzzle)
