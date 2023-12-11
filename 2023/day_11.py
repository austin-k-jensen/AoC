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


def part_1(data):
    rows = [list(x) for x in data.split()]
    array = np.array(rows)

    rows_added = 0
    for i, row in enumerate(array):
        if np.all(row == "."):
            array = np.insert(array, (i + rows_added), row, axis=0)
            rows_added += 1

    columns_added = 0
    for i, column in enumerate(array.T):
        if np.all(column == "."):
            array = np.insert(array, (i + columns_added), column, axis=1)
            columns_added += 1

    points = np.argwhere(array == "#")
    dists = []
    for i, point_1 in enumerate(points):
        for point_2 in points[i:]:
            dist = abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])
            if dist != -1:
                dists.append(dist)
    print(sum(dists))


def part_2(data):
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

    added = 1
    points = np.argwhere(array == "#")
    for point in points:
        rc = 0
        for row in rows_added:
            if point[0] > (row + rc):
                point[0] += added
            rc += added

        cc = 0
        for column in columns_added:
            if point[1] > (column + cc):
                point[1] += added
            cc += added
    # print(points)

    dists = []
    for i, point_1 in enumerate(points):
        for point_2 in points[i:]:
            dist = abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])
            if dist != 0:
                dists.append(dist)
                # print(point_1, point_2, dist)
    print(sum(dists))


part_1(puzzle)
part_2(puzzle)
