from itertools import combinations
from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 8
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


@timing
def parse(data):
    rows = data.strip().split()
    antennas = {}
    for i, row in enumerate(rows):
        for j, typ in enumerate(row):
            edge = (i, j)
            if typ != ".":
                if typ in antennas:
                    antennas[typ].append((i, j))
                else:
                    antennas[typ] = [(i, j)]
    return antennas, edge


@timing
def part_1(antennas, edge):
    antinodes = set()
    for antenna in antennas:
        for (x1, y1), (x2, y2) in combinations(antennas[antenna], 2):
            x_diff = x2 - x1
            y_diff = y2 - y1

            x3 = x1 - x_diff
            y3 = y1 - y_diff
            x4 = x2 + x_diff
            y4 = y2 + y_diff

            if 0 <= x3 <= edge[0] and 0 <= y3 <= edge[1]:
                antinodes.add((x3, y3))
            if 0 <= x4 <= edge[0] and 0 <= y4 <= edge[1]:
                antinodes.add((x4, y4))
    return len(antinodes)


@timing
def part_2(antennas, edge):
    antinodes = set()
    for antenna in antennas:
        for (x1, y1), (x2, y2) in combinations(antennas[antenna], 2):
            antinodes.add((x1, y1))
            antinodes.add((x2, y2))

            x_diff = x2 - x1
            y_diff = y2 - y1

            x3 = x1
            y3 = y1
            x4 = x2
            y4 = y2

            check = True
            while check:
                x3 -= x_diff
                y3 -= y_diff
                check3 = True

                if 0 <= x3 <= edge[0] and 0 <= y3 <= edge[1]:
                    antinodes.add((x3, y3))
                else:
                    check3 = False

                x4 += x_diff
                y4 += y_diff
                check4 = True

                if 0 <= x4 <= edge[0] and 0 <= y4 <= edge[1]:
                    antinodes.add((x4, y4))
                else:
                    check4 = False

                check = check3 or check4

    return len(antinodes)


antennas, edge = parse(puzzle)
print("part 1: ", part_1(antennas, edge))
print("part 2: ", part_2(antennas, edge))
