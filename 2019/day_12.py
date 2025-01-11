import re
from itertools import combinations
from math import lcm
from aocd import get_data

YEAR, DAY = 2019, 12
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""

TEST_2 = """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""


def parse(data: str):
    rows = data.strip().splitlines()
    moons = {0: {}, 1: {}, 2: {}, 3: {}}
    for i, row in enumerate(rows):
        moons[i]["pos"] = [int(x) for x in re.findall(r"-?\d+", row)]
        moons[i]["vel"] = [0, 0, 0]

    return moons


def part_1(moons: dict):
    for i in range(1000):
        for m1, m2 in combinations(moons, 2):
            for i in range(3):
                if moons[m1]["pos"][i] > moons[m2]["pos"][i]:
                    moons[m1]["vel"][i] -= 1
                    moons[m2]["vel"][i] += 1
                elif moons[m1]["pos"][i] < moons[m2]["pos"][i]:
                    moons[m1]["vel"][i] += 1
                    moons[m2]["vel"][i] -= 1

        for moon in moons:
            for i in range(3):
                moons[moon]["pos"][i] += moons[moon]["vel"][i]

    tot = 0
    for moon in moons:
        pot = 0
        kin = 0
        for i in range(3):
            pot += abs(moons[moon]["pos"][i])
            kin += abs(moons[moon]["vel"][i])
        tot += pot * kin
    return tot


def part_2(moons: dict):
    cycle_length = [0, 0, 0]
    for i in range(3):
        states = set()
        states.add(
            (
                moons[0]["pos"][i],
                moons[0]["vel"][i],
                moons[1]["pos"][i],
                moons[1]["vel"][i],
                moons[2]["pos"][i],
                moons[2]["vel"][i],
                moons[3]["pos"][i],
                moons[3]["vel"][i],
            )
        )
        # print(states)

        steps = 0
        while True:
            for m1, m2 in combinations(moons, 2):
                if moons[m1]["pos"][i] > moons[m2]["pos"][i]:
                    moons[m1]["vel"][i] -= 1
                    moons[m2]["vel"][i] += 1
                elif moons[m1]["pos"][i] < moons[m2]["pos"][i]:
                    moons[m1]["vel"][i] += 1
                    moons[m2]["vel"][i] -= 1

            for moon in moons:
                moons[moon]["pos"][i] += moons[moon]["vel"][i]

            steps += 1

            state = (
                moons[0]["pos"][i],
                moons[0]["vel"][i],
                moons[1]["pos"][i],
                moons[1]["vel"][i],
                moons[2]["pos"][i],
                moons[2]["vel"][i],
                moons[3]["pos"][i],
                moons[3]["vel"][i],
            )

            if state in states:
                cycle_length[i] = steps
                break

    return lcm(*cycle_length)


moons = parse(puzzle)
print("Part 1: ", part_1(moons))
print("Part 2: ", part_2(moons))
