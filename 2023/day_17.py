from heapq import heappush, heappop
from aocd import get_data

YEAR, DAY = 2023, 17
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

TEST_2 = """
111111111111
999999999991
999999999991
999999999991
999999999991
"""


def parse(data):
    rows = data.strip().split()
    grid = {}
    for i, row in enumerate(rows):
        for j, loss in enumerate(row):
            grid[(i, j)] = int(loss)
    return grid


def part_1(grid):
    goal = max(grid)

    dir_map = {
        (1, 0): [(0, 1), (0, -1)],
        (-1, 0): [(0, 1), (0, -1)],
        (0, 1): [(1, 0), (-1, 0)],
        (0, -1): [(1, 0), (-1, 0)],
    }

    check = [(0, (0, 0), (0, 1)), (0, (0, 0), (1, 0))]
    visited = set()

    while check:
        heat, loc, in_dir = heappop(check)

        if loc == goal:
            print("part 1: ", heat)
            return heat

        if (loc, in_dir) in visited:
            continue

        visited.add((loc, in_dir))

        for dir in dir_map[in_dir]:
            heat_loss = 0
            for step in range(1, 4):
                new_loc = (loc[0] + dir[0] * step, loc[1] + dir[1] * step)
                if (0 <= new_loc[0] <= goal[0]) and (0 <= new_loc[1] <= goal[1]):
                    heat_loss += grid[new_loc]
                    heappush(check, (heat + heat_loss, new_loc, dir))


def part_2(grid):
    goal = max(grid)

    dir_map = {
        (1, 0): [(0, 1), (0, -1)],
        (-1, 0): [(0, 1), (0, -1)],
        (0, 1): [(1, 0), (-1, 0)],
        (0, -1): [(1, 0), (-1, 0)],
    }

    check = [(0, (0, 0), (0, 1)), (0, (0, 0), (1, 0))]
    visited = set()

    while check:
        heat, loc, in_dir = heappop(check)

        if loc == goal:
            print("part 2: ", heat)
            break

        if (loc, in_dir) in visited:
            continue

        visited.add((loc, in_dir))

        for dir in dir_map[in_dir]:
            heat_loss = 0
            for step in range(1, 11):
                new_loc = (loc[0] + dir[0] * step, loc[1] + dir[1] * step)
                if (0 <= new_loc[0] <= goal[0]) and (0 <= new_loc[1] <= goal[1]):
                    heat_loss += grid[new_loc]
                    if step >= 4:
                        heappush(check, (heat + heat_loss, new_loc, dir))


grid = parse(puzzle)
part_1(grid)
part_2(grid)
