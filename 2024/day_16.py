from heapq import heappush, heappop
from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 16
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

TEST_2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""


@timing
def parse(data):
    rows = data.strip().split()
    grid = {}
    for i, row in enumerate(rows):
        for j, typ in enumerate(row):
            if typ == "S":
                start = (i, j)
                grid[(i, j)] = "."
            elif typ == "E":
                end = (i, j)
                grid[(i, j)] = "."
            else:
                grid[(i, j)] = typ
    return start, end, grid


@timing
def part_1(start: tuple, end: tuple, grid: dict):

    dir_map = {
        (1, 0): [(1, 0), (0, 1), (0, -1)],
        (-1, 0): [(-1, 0), (0, 1), (0, -1)],
        (0, 1): [(0, 1), (1, 0), (-1, 0)],
        (0, -1): [(0, -1), (1, 0), (-1, 0)],
    }

    check = [(0, start, (0, 1))]
    visited = set()

    while check:
        score, loc, in_dir = heappop(check)

        if loc == end:
            return score

        if (loc, in_dir) in visited:
            continue

        visited.add((loc, in_dir))

        for dir in dir_map[in_dir]:
            score_change = 1
            new_loc = (loc[0] + dir[0], loc[1] + dir[1])
            if grid[new_loc] != "#":
                if dir != in_dir:
                    score_change += 1000
                heappush(check, (score + score_change, new_loc, dir))


@timing
def part_2(start: tuple, end: tuple, grid: dict, best: int):

    dir_map = {
        (1, 0): [(1, 0), (0, 1), (0, -1)],
        (-1, 0): [(-1, 0), (0, 1), (0, -1)],
        (0, 1): [(0, 1), (1, 0), (-1, 0)],
        (0, -1): [(0, -1), (1, 0), (-1, 0)],
    }

    check = [(0, start, (0, 1), [start])]
    visited = []
    best_pos = {}

    while check:
        score, loc, in_dir, path = heappop(check)

        if loc == end:
            visited += path

        if (loc, in_dir) in best_pos:
            if best_pos[(loc, in_dir)] >= score:
                best_pos[(loc, in_dir)] = score
            else:
                continue
        else:
            best_pos[(loc, in_dir)] = score

        if score > best:
            continue

        for dir in dir_map[in_dir]:
            score_change = 1
            new_loc = (loc[0] + dir[0], loc[1] + dir[1])
            if grid[new_loc] != "#":
                if dir != in_dir:
                    score_change += 1000
                new_path = list(path)
                new_path.append(new_loc)
                heappush(check, (score + score_change, new_loc, dir, new_path))

    return len(set(visited))


start, end, grid = parse(puzzle)
best = part_1(start, end, grid)
print("part 1: ", best)
print("part 2: ", part_2(start, end, grid, best))
