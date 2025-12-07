from collections import defaultdict
from aocd import get_data

YEAR, DAY = 2025, 7
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""


def parse(data: str) -> dict:
    rows = data.strip().split()
    grid = {}
    for i, row in enumerate(rows):
        for j, typ in enumerate(row):
            if typ == "S":
                grid[(i, j)] = "|"
            else:
                grid[(i, j)] = typ
    return grid


def part_1(grid: dict) -> int:

    row_max, col_max = max(grid)
    split_cnt = 0

    block_cnt = defaultdict(int)
    block_cnt[(0, 7)] = 1

    for row in range(row_max):
        for col in range(col_max + 1):
            if grid[(row, col)] == "|":
                if grid[(row + 1, col)] == ".":
                    grid[(row + 1, col)] = "|"
                    block_cnt[(row + 1, col)] += block_cnt[(row, col)]
                elif grid[(row + 1, col)] == "^":
                    split_cnt += 1
                    grid[(row + 1, col - 1)] = "|"
                    grid[(row + 1, col + 1)] = "|"
                    block_cnt[(row + 1, col - 1)] += block_cnt[(row, col)]
                    block_cnt[(row + 1, col + 1)] += block_cnt[(row, col)]
    print(block_cnt)

    print(split_cnt)

    # for row in range(row_max + 1):
    #     out = ""
    #     for col in range(col_max + 1):
    #         out += grid[(row, col)]
    #     print(out)


grid = parse(TEST_1)
part_1(grid)
