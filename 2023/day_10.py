from aocd import get_data
from matplotlib.path import Path

YEAR, DAY = 2023, 10
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
.....
.S-7.
.|.|.
.L-J.
.....
"""

TEST_2 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

TEST_3 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""


def part_1(data):
    rows = data.split()

    start_loc = [
        (index, row.index("S")) for index, row in enumerate(rows) if "S" in row
    ][0]

    dirs = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
    }

    if (rows[start_loc[0]][start_loc[1] + 1] in ("-", "7", "J")) and (
        rows[start_loc[0] + 1][start_loc[1]] in ("|", "L", "J")
    ):
        start_char = "F"
    if (rows[start_loc[0]][start_loc[1] - 1] in ("-", "L", "F")) and (
        rows[start_loc[0] - 1][start_loc[1]] in ("|", "7", "F")
    ):
        start_char = "J"

    move = (dirs[start_char][0][0], dirs[start_char][0][1])
    new_loc = (
        start_loc[0] + 1 * move[0],
        start_loc[1] + 1 * move[1],
    )
    pipe = rows[new_loc[0]][new_loc[1]]

    visited = [start_loc, new_loc]

    steps = 1
    while pipe != "S":
        # print(new_loc, pipe)
        back = (move[0] * -1, move[1] * -1)
        for _dir in dirs[pipe]:
            if _dir != back:
                move = _dir
                break
        new_loc = (
            new_loc[0] + 1 * move[0],
            new_loc[1] + 1 * move[1],
        )
        visited.append(new_loc)
        pipe = rows[new_loc[0]][new_loc[1]]
        steps += 1
    print("part 1: ", steps // 2)

    return visited


def part_2(visited):
    path = Path(visited)

    min_x = min(loc[0] for loc in visited)
    max_x = max(loc[0] for loc in visited)
    min_y = min(loc[1] for loc in visited)
    max_y = max(loc[1] for loc in visited)

    contained = 0
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if (x, y) in visited:
                continue
            if path.contains_point((x, y)):
                contained += 1
    print("part 2: ", contained)


def part_2_tst(data, visited):
    rows = data.split()


visited = part_1(TEST_3)
part_2(visited)
part_2_tst(TEST_3, visited)
