import numpy as np
from aocd import get_data

YEAR, DAY = 2023, 11
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""


def day_11(data, expand):
    rows = [list(x) for x in data.split()]
    array = np.array(rows)

    rows_added = []
    for i, row in enumerate(array):
        if np.all(row == "."):
            rows_added.append(i)

    columns_added = []
    for i, column in enumerate(array.T):
        if np.all(column == "."):
            columns_added.append(i)

    expand = expand
    points = np.argwhere(array == "#")
    for point in points:
        rc = 0
        for row in rows_added:
            if point[0] > (row + rc):
                point[0] += expand
            rc += expand

        cc = 0
        for column in columns_added:
            if point[1] > (column + cc):
                point[1] += expand
            cc += expand

    dists = []
    for i, point_1 in enumerate(points):
        for point_2 in points[i:]:
            dists.append(abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1]))
    return sum(dists)


print(day_11(puzzle, 1))
print(day_11(puzzle, 999999))
