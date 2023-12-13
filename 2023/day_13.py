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
##..##..##.
######..###
.####.##.##
..........#
.####.##.##
.####....##
..##..##..#
"""


def sym_check(grid, mult):
    cnt = []
    for row in range(len(grid) - 1):
        match = False
        if all(np.equal(grid[row], grid[row + 1])):
            if row == 0:
                cnt.append(mult)
            elif row + 2 == len(grid):
                cnt.append((row + 1) * mult)
            else:
                left, right = row, len(grid) - row - 2
                for i in range(1, min(left, right) + 1):
                    if all(np.equal(grid[row - i], grid[row + 1 + i])):
                        match = True
                    else:
                        match = False
                        break
        if match:
            cnt.append((left + 1) * mult)
    return cnt


def part_1(data):
    grids = data.strip().split("\n\n")

    total = 0
    for grid in grids:
        rows = [list(x) for x in grid.split()]
        grid = np.array(rows)

        total += sum(sym_check(grid.T, 1))
        total += sum(sym_check(grid, 100))

    print("part 1: ", total)


def part_2(data):
    grids = data.strip().split("\n\n")

    total = 0
    for grid in grids:
        rows = [list(x) for x in grid.split()]
        grid = np.array(rows)

        orig_col = sym_check(grid.T, 1)
        orig_row = sym_check(grid, 100)

        cnt = 0
        for x, y in np.ndindex(grid.shape):
            test_grid = grid.copy()

            if test_grid[x, y] == ".":
                test_grid[x, y] = "#"
            elif test_grid[x, y] == "#":
                test_grid[x, y] = "."
            new_col = sym_check(test_grid.T, 1)
            new_row = sym_check(test_grid, 100)

            new_col = list(set(new_col) - set(orig_col))
            new_row = list(set(new_row) - set(orig_row))

            if len(new_col) == 1 or len(new_row) == 1:
                cnt = sum(new_col + new_row)
        total += cnt
    print("part 2: ", total)


part_1(puzzle)
part_2(puzzle)
