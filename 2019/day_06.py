from collections import defaultdict
from heapq import heappush, heappop
from aocd import get_data

YEAR, DAY = 2019, 6
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""


def parse(data: str):
    orbiting = defaultdict(str)
    orbits = defaultdict(list)
    for pair in data.strip().splitlines():
        obj_1, obj_2 = pair.split(")")
        orbiting[obj_2] = obj_1
        orbits[obj_1].append(obj_2)

    return orbiting, orbits


def part_1(orbiting: defaultdict):
    tot = 0
    for object in orbiting:
        check_object = object
        end = False
        orbs = 1

        while not end:
            if orbiting[check_object] == "COM":
                tot += orbs
                end = True
            else:
                check_object = orbiting[check_object]
                orbs += 1

    return tot


def part_2(orbiting: defaultdict, orbits: defaultdict):
    start, end = orbiting["YOU"], orbiting["SAN"]
    check = [(0, start, "YOU")]
    visited = set()

    while check:
        trans, loc, in_loc = heappop(check)

        if loc == end:
            # print(trans)
            return trans

        if (loc, in_loc) in visited:
            continue

        visited.add((loc, in_loc))

        for object in orbits[loc] + [orbiting[loc]]:
            heappush(check, (trans + 1, object, loc))


orbiting, orbits = parse(puzzle)
print("Part 1: ", part_1(orbiting))
print("Part 2: ", part_2(orbiting, orbits))
