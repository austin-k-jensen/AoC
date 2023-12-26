import sys
from datetime import datetime
from aocd import get_data

sys.setrecursionlimit(1000000)

YEAR, DAY = 2023, 23
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""


def parse(data):
    scriptstart = datetime.now()

    rows = data.strip().split()
    grid = {}
    for i, row in enumerate(rows):
        for j, typ in enumerate(row):
            if i == 0 and typ == ".":
                start = (i, j)
                grid[(i, j)] = "."
            if i == len(rows) - 1 and typ == ".":
                end = (i, j)
                grid[(i, j)] = "."
            else:
                grid[(i, j)] = typ

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"{scriptend}: Parsing complete in seconds: {elapsed_sec}")
    return start, end, grid


def move_1(path, loc, end, grid, paths):
    edge = max(grid)
    dir_map = {
        ".": [(0, 1), (0, -1), (1, 0), (-1, 0)],
        "^": [(-1, 0)],
        ">": [(0, 1)],
        "v": [(1, 0)],
        "<": [0, -1],
    }

    if loc == end:
        paths.append(len(path) - 1)

    path.append(loc)

    for dir in dir_map[grid[loc]]:
        new_loc = (loc[0] + dir[0], loc[1] + dir[1])
        if (
            (0 <= new_loc[0] <= edge[0])
            and (0 <= new_loc[1] <= edge[1])
            and grid[new_loc] != "#"
            and new_loc not in path
        ):
            move_1(path.copy(), new_loc, end, grid, paths)


def part_1(start, end, grid):
    scriptstart = datetime.now()

    loc = start
    path = [start]
    paths = []
    move_1(path, loc, end, grid, paths)

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"\n{scriptend}: Part 1 complete in seconds: {elapsed_sec}")
    print("part 1: ", max(paths))


def condense_graph(start, end, grid):
    edge = max(grid)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    graph = {}

    nodes = [start]
    check = [start]
    visited = set()
    while check:
        loc = check.pop()

        if loc in visited:
            continue

        visited.add(loc)

        node_check = []
        for dir in dirs:
            new_loc = (loc[0] + dir[0], loc[1] + dir[1])
            if (
                (0 <= new_loc[0] <= edge[0])
                and (0 <= new_loc[1] <= edge[1])
                and grid[new_loc] != "#"
                and new_loc not in visited
            ):
                node_check.append(new_loc)
                check.append(new_loc)
        if len(node_check) > 1:
            nodes.append(loc)
    nodes.append(end)

    for node in nodes:
        graph[node] = []
        check = [(node, 0)]
        visited = set()
        while check:
            loc, dist = check.pop()
            visited.add(loc)

            for dir in dirs:
                new_loc = (loc[0] + dir[0], loc[1] + dir[1])
                if (
                    (0 <= new_loc[0] <= edge[0])
                    and (0 <= new_loc[1] <= edge[1])
                    and grid[new_loc] != "#"
                    and new_loc not in visited
                ):
                    if new_loc in nodes:
                        graph[node].append((new_loc, dist + 1))
                        continue
                    check.append((new_loc, dist + 1))

    return graph


def move_2(path, loc, end, graph, paths):
    if loc == end:
        paths.append(path)

    path.append(loc)

    for next in graph[loc]:
        new_loc = next[0]

        if new_loc not in path:
            move_2(path.copy(), new_loc, end, graph, paths)


def part_2(start, end, graph):
    scriptstart = datetime.now()

    path = []
    loc = start
    paths = []
    move_2(path, loc, end, graph, paths)

    dists = []
    for path in paths:
        dist = 0
        for i in range(len(path) - 1):
            for node in graph[path[i]]:
                if node[0] == path[i + 1]:
                    dist += node[1]

        dists.append(dist)

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"\n{scriptend}: Part 2 complete in seconds: {elapsed_sec}")
    print("part 2: ", max(dists))


start, end, grid = parse(puzzle)
graph = condense_graph(start, end, grid)
part_1(start, end, grid)
part_2(start, end, graph)
