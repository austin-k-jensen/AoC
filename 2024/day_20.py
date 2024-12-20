from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 20
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""


@timing
def parse(data: str):
    rows = data.strip().split()
    path = set()
    walls = set()
    for i, row in enumerate(rows):
        for j, typ in enumerate(row):
            if typ == "S":
                start = (i, j)
                path.add((i, j))
            elif typ == "E":
                end = (i, j)
                path.add((i, j))
            elif typ == ".":
                path.add((i, j))
            elif typ == "#":
                walls.add((i, j))
    return start, end, path, walls


@timing
def part_1(start: tuple, end: tuple, path: set, walls: set):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    path_times = {start: 0}

    check = [start]

    while check:
        loc = check.pop()

        if loc == end:
            break

        for dir in dirs:
            new_loc = (loc[0] + dir[0], loc[1] + dir[1])
            if new_loc in path_times:
                continue
            elif new_loc in path:
                path_times[new_loc] = path_times[loc] + 1
                check.append(new_loc)

    savings = []
    for spot in path:
        for dir_1 in dirs:
            check_loc = (spot[0] + dir_1[0], spot[1] + dir_1[1])
            if check_loc in walls:
                for dir_2 in dirs:
                    new_loc = (check_loc[0] + dir_2[0], check_loc[1] + dir_2[1])
                    if new_loc in path:
                        if path_times[new_loc] - path_times[spot] - 2 > 0:
                            savings.append(path_times[new_loc] - path_times[spot] - 2)

    large_savings = [x for x in savings if x >= 100]
    return path_times, len(large_savings)


@timing
def part_2(path_times: dict):
    savings_dict = {}
    dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

    for loc in path_times:
        steps = 20

        for dx in range(steps + 1):
            for dy in range(steps + 1 - dx):
                dist = dx + dy

                for dir in dirs:
                    new_loc = (loc[0] + dir[0] * dx, loc[1] + dir[1] * dy)

                    if new_loc in path_times:
                        if path_times[new_loc] - path_times[loc] - dist > 0:
                            saving = path_times[new_loc] - path_times[loc] - dist
                            if (loc, new_loc) in savings_dict:
                                savings_dict[(loc, new_loc)] = max(
                                    savings_dict[(loc, new_loc)], saving
                                )
                            else:
                                savings_dict[(loc, new_loc)] = saving

    large_savings = [x for x in savings_dict.values() if x >= 100]
    return len(large_savings)


start, end, path, walls = parse(puzzle)
path_times, part_1_ans = part_1(start, end, path, walls)
print("part 1: ", part_1_ans)
print("part 2: ", part_2(path_times))
