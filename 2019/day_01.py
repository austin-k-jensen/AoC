from aocd import get_data

YEAR, DAY = 2019, 1
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
12
14
1969
100756
"""


def part_1(data: str):
    tot = 0
    for line in data.strip().splitlines():
        # print(line)
        mass = int(line) // 3 - 2
        tot += mass

    return tot


def part_2(data: str):
    tot = 0
    for line in data.strip().splitlines():
        mass = int(line)
        while mass > 0:
            mass = mass // 3 - 2
            if mass > 0:
                tot += mass
    return tot


print(part_1(puzzle))
print(part_2(puzzle))
