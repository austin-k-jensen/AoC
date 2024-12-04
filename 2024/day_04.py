from aocd import get_data

YEAR, DAY = 2024, 4
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def parse(data):
    rows = data.strip().split()
    grid = {}
    for i, row in enumerate(rows):
        for j, letter in enumerate(row):
            grid[(i, j)] = letter
    return grid


def part_1(grid):
    max_x, max_y = max(grid)

    count = 0
    for i in range(max_x + 1):
        for j in range(max_y + 1):

            N = True if i > 2 else False
            E = True if (max_y - j) > 2 else False
            S = True if (max_x - i) > 2 else False
            W = True if j > 2 else False

            if grid[(i, j)] == "X":
                if N:
                    if grid[(i - 1, j)] == "M":
                        if grid[(i - 2, j)] == "A":
                            if grid[(i - 3, j)] == "S":
                                count += 1
                if E:
                    if grid[(i, j + 1)] == "M":
                        if grid[(i, j + 2)] == "A":
                            if grid[(i, j + 3)] == "S":
                                count += 1

                if S:
                    if grid[(i + 1, j)] == "M":
                        if grid[(i + 2, j)] == "A":
                            if grid[(i + 3, j)] == "S":
                                count += 1

                if W:
                    if grid[(i, j - 1)] == "M":
                        if grid[(i, j - 2)] == "A":
                            if grid[(i, j - 3)] == "S":
                                count += 1

                if N and E:
                    if grid[(i - 1, j + 1)] == "M":
                        if grid[(i - 2, j + 2)] == "A":
                            if grid[(i - 3, j + 3)] == "S":
                                count += 1
                if S and E:
                    if grid[(i + 1, j + 1)] == "M":
                        if grid[(i + 2, j + 2)] == "A":
                            if grid[(i + 3, j + 3)] == "S":
                                count += 1

                if N and W:
                    if grid[(i - 1, j - 1)] == "M":
                        if grid[(i - 2, j - 2)] == "A":
                            if grid[(i - 3, j - 3)] == "S":
                                count += 1

                if S and W:
                    if grid[(i + 1, j - 1)] == "M":
                        if grid[(i + 2, j - 2)] == "A":
                            if grid[(i + 3, j - 3)] == "S":
                                count += 1

    return count


def part_2(grid):
    max_x, max_y = max(grid)

    count = 0
    for i in range(1, max_x):
        for j in range(1, max_y):

            if grid[(i, j)] == "A":
                if (
                    (grid[(i - 1, j - 1)] == "M" and grid[(i + 1, j + 1)] == "S")
                    or (grid[(i - 1, j - 1)] == "S" and grid[(i + 1, j + 1)] == "M")
                ) and (
                    (grid[(i + 1, j - 1)] == "M" and grid[(i - 1, j + 1)] == "S")
                    or (grid[(i + 1, j - 1)] == "S" and grid[(i - 1, j + 1)] == "M")
                ):
                    count += 1
    return count


grid = parse(puzzle)
print("part 1: ", part_1(grid))
print("part 2: ", part_2(grid))
