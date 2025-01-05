from collections import defaultdict
from math import isclose
from aocd import get_data

YEAR, DAY = 2019, 10
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
.#..#
.....
#####
....#
...##
"""

TEST_2 = """
.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##
"""

TEST_3 = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""


def parse(data: str):
    rows = data.strip().splitlines()
    asteroids = set()
    for i, row in enumerate(rows):
        for j, typ in enumerate(row):
            if typ == "#":
                asteroids.add((j, i))
    return asteroids, (j, i)


def get_sign_of_difference(a, b):
    if a < b:
        return 1
    elif a > b:
        return -1
    else:
        return 0


def part_1(asteroids: set):
    ast_sights = defaultdict(set)

    for x1, y1 in asteroids:
        for x2, y2 in asteroids:
            if (x1, y1) == (x2, y2):
                continue

            x_diff = get_sign_of_difference(x1, x2)
            y_diff = get_sign_of_difference(y1, y2)

            if x1 == x2:
                line = (x1,)

            else:
                m = (y1 - y2) / (x1 - x2)
                b = -m * x1 + y1

                line = (round(m, 6), round(b, 7))

            ast_sights[(x1, y1)].add((line, (x_diff, y_diff)))

    best = 0

    for ast in ast_sights:
        if len(ast_sights[ast]) > best:
            best = len(ast_sights[ast])
            best_ast = ast

    return ast_sights, best, best_ast


def part_2(asteroids: set, edge: tuple, ast_sights: dict, best_ast: tuple):

    # print(ast_sights[best_ast], edge)
    removed = {}
    total_ast = len(asteroids)

    cnt = 1
    while asteroids and cnt < total_ast:

        if cnt > 200:
            return removed[200][0] * 100 + removed[200][1]

        for dir in [
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
        ]:
            # print(dir)
            lines = sorted(
                [line[0] for line in ast_sights[best_ast] if line[1] == dir],
                key=lambda x: x[0],
            )

            if dir[0] == 0:
                # print("\t", lines)
                loc = best_ast
                while 0 < loc[1] < edge[1]:
                    loc = (loc[0], loc[1] + dir[1])
                    if loc in asteroids:
                        # print("\t\t", loc)
                        removed[cnt] = loc
                        asteroids.discard(loc)
                        cnt += 1
                        break

            if dir[0] != 0 and dir[1] != 0:
                for line in lines:
                    loc = best_ast
                    # print("\t", line)
                    while 0 < loc[0] < edge[0]:
                        loc = (loc[0] + dir[0], loc[1] + line[0] * dir[0])
                        # print("\t\t", loc)
                        for ast in asteroids:
                            if loc[0] == ast[0] and isclose(
                                loc[1], ast[1], abs_tol=0.00001
                            ):
                                # print("\t\t\t", ast)
                                loc = ast
                                break
                        if loc in asteroids:
                            removed[cnt] = loc
                            asteroids.discard(loc)
                            cnt += 1
                            break

            if dir[1] == 0:
                # print("\t", lines)
                loc = best_ast
                while 0 < loc[0] < edge[0]:
                    loc = (loc[0] + dir[0], loc[1])
                    if loc in asteroids:
                        # print("\t\t", loc)
                        removed[cnt] = loc
                        asteroids.discard(loc)
                        cnt += 1
                        break

    print(removed)


asteroids, edge = parse(puzzle)
ast_sights, best, best_ast = part_1(asteroids)
print("Part 1: ", best)
print("Part 2: ", part_2(asteroids, edge, ast_sights, best_ast))
