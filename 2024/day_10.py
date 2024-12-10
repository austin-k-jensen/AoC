from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 10
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


@timing
def parse(data):
    rows = data.strip().split()
    starts = []
    grid = {}
    for i, row in enumerate(rows):
        for j, elv in enumerate(row):
            if elv == "0":
                starts.append((i, j))
            grid[(i, j)] = int(elv)
    return starts, grid


@timing
def part_1(starts, grid):
    edge = max(grid)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # starts = [(5, 2)]

    tot = 0
    tot_2 = 0
    for start in starts:
        check = [start]
        reached = []
        # print(start, reached)

        while check:
            loc = check.pop()
            # print(f"Checking loc: {loc}")
            for dir in dirs:
                new_loc = (loc[0] + dir[0], loc[1] + dir[1])
                # print(f"\tNew loc: {new_loc}")
                if (0 <= new_loc[0] <= edge[0]) and (0 <= new_loc[1] <= edge[1]):
                    if grid[new_loc] == grid[loc] + 1:
                        if grid[new_loc] == 9:
                            reached.append(new_loc)
                        else:
                            check.append(new_loc)
        # print(start, reached)
        tot += len(set(reached))
        tot_2 += len(reached)
    # print(tot_2)
    return tot, tot_2


starts, grid = parse(puzzle)
ans_1, ans_2 = part_1(starts, grid)
print("part 1: ", ans_1)
print("part 2: ", ans_2)
