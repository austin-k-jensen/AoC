from aocd import get_data

YEAR, DAY = 2025, 5
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

TEST_2 = """
1-10
10-10
10-10

0
"""


def parse(data: str):
    _rngs, _ids = data.strip().split("\n\n")

    rngs = []
    for row in _rngs.splitlines():
        i, j = [int(x) for x in row.split("-")]
        rngs.append([i, j])

    ids = [int(row) for row in _ids.splitlines()]

    return rngs, ids


def part_1(rngs: list, ids: list) -> int:
    count = 0
    for id in ids:
        for rng in rngs:
            if id >= rng[0] and id <= rng[1]:
                count += 1
                break
    return count


def part_2(rngs: list) -> int:
    rngs.sort()

    merged = [rngs[0]]

    for rng in rngs[1:]:

        curr = merged[-1]

        if curr[1] >= rng[0]:
            curr[1] = max(curr[1], rng[1])
        else:
            merged.append(rng)

    count = 0
    for rng in merged:
        count += rng[1] - rng[0] + 1

    return count


rngs, ids = parse(puzzle)
print("part 1: ", part_1(rngs, ids))
print("part 2: ", part_2(rngs))
