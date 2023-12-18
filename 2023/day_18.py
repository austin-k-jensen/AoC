import re
from matplotlib.path import Path
from aocd import get_data

YEAR, DAY = 2023, 18
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""


def part_1(data):
    digs = [(dir, int(dist)) for (dir, dist) in re.findall(r"([UDRL]) (\d+)", data)]

    loc = [0, 0]
    visited = [loc]

    for dir, dist in digs:
        for _ in range(dist):
            if dir == "U":
                loc[1] += -1
            elif dir == "D":
                loc[1] += 1
            elif dir == "R":
                loc[0] += 1
            elif dir == "L":
                loc[0] += -1
            visited.append([loc[0], loc[1]])

    path = Path(visited, closed=True)

    min_x = min(loc[0] for loc in visited)
    max_x = max(loc[0] for loc in visited)
    min_y = min(loc[1] for loc in visited)
    max_y = max(loc[1] for loc in visited)

    contained = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in visited:
                continue
            if path.contains_point((x, y)):
                contained += 1
    print("part 1: ", contained + len(visited) - 1)


def part_2(data):
    digs = [(int(code[5]), int(code[:5], 16)) for (code) in re.findall(r"#(\w+)", data)]

    start = (0, 0)
    visited = [start]
    area = 0
    boarder = 0
    for dir, dist in digs:
        boarder += dist
        loc = visited[-1]
        # for _ in range(dist):
        if dir == 3:
            new_loc = (loc[0], loc[1] + dist * -1)
        elif dir == 1:
            new_loc = (loc[0], loc[1] + dist)
        elif dir == 0:
            new_loc = (loc[0] + dist, loc[1])
        elif dir == 2:
            new_loc = (loc[0] + dist * -1, loc[1])
        visited.append((new_loc))
        # print(loc, new_loc)
        area += (new_loc[0] - loc[0]) * ((new_loc[1] + loc[1]) / 2)
    print(abs(area) + boarder / 2 + 1)

    # path = Path(visited, closed=True)

    # min_x = min(loc[0] for loc in visited)
    # max_x = max(loc[0] for loc in visited)
    # min_y = min(loc[1] for loc in visited)
    # max_y = max(loc[1] for loc in visited)

    # contained = 0
    # for y in range(min_y, max_y + 1):
    #     for x in range(min_x, max_x + 1):
    #         if (x, y) in visited:
    #             continue
    #         if path.contains_point((x, y)):
    #             contained += 1
    # print("part 2: ", contained + len(visited) - 1)


# part_1(TEST_1)
part_2(puzzle)
