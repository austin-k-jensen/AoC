import numpy as np
from aocd import get_data

YEAR, DAY = 2023, 13
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

TEST_2 = """
.#..#.###.#..##
.#..#.###.#..##
#.##..#..####..
#.#####..#..#..
#..#..#.#...###
..#.##.##.##.##
..#..##.#.##.##
####.##...#..#.
..#...#..#.#...
###.#.#..#...##
.#..#######..##
###.#.#.###....
.#.....#.....##
"""


def sym_check(grid, mult):
    cnt = 0
    for row in range(len(grid) - 1):
        match = False
        if all(np.equal(grid[row], grid[row + 1])):
            if row == 0:
                cnt += mult
            elif row + 2 == len(grid):
                cnt += (row + 1) * mult
            else:
                left, right = row, len(grid) - row - 2
                for i in range(1, min(left, right) + 1):
                    if all(np.equal(grid[row - i], grid[row + 1 + i])):
                        match = True
                    else:
                        match = False
                        break
        if match:
            cnt += (left + 1) * mult
    return cnt


def part_1(data):
    grids = data.strip().split("\n\n")

    total = 0
    for grid in grids:
        rows = [list(x) for x in grid.split()]
        grid = np.array(rows)

        total += sym_check(grid.T, 1)
        total += sym_check(grid, 100)

    print("part 1: ", total)


part_1(puzzle)
