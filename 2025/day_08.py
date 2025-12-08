from itertools import combinations
from math import dist
from aocd import get_data

YEAR, DAY = 2025, 8
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""


def parse(data: str) -> dict:
    circuts = {}
    for i, row in enumerate(data.strip().splitlines()):
        x, y, z = row.split(",")
        circuts[i] = (int(x), int(y), int(z))

    return circuts


def day_8(circuts: dict, lim: int):
    dists = []

    for p1, p2 in combinations(circuts.values(), 2):
        dists.append((dist(p1, p2), (p1, p2)))
    dists.sort()

    for i in circuts:
        circuts[i] = {circuts[i]}

    for i, (_, (p1, p2)) in enumerate(dists):
        for circut in circuts:
            if p1 in circuts[circut]:
                c1 = circut
            if p2 in circuts[circut]:
                c2 = circut

        if c1 != c2:
            circuts[c1] = circuts[c1] | circuts[c2]
            del circuts[c2]

        if i == lim:
            lens = sorted([len(circut) for circut in circuts.values()], reverse=True)
            a1 = lens[0] * lens[1] * lens[2]

        if len(circuts) == 1:
            a2 = p1[0] * p2[0]
            break
    return a1, a2


circuts = parse(puzzle)
part_1, part_2 = day_8(circuts, 999)
print("part 1: ", part_1)
print("part 2: ", part_2)
