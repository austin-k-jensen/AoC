import re
from aocd import get_data
from aocd import submit

YEAR, DAY = 2023, 6
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """Time:      7  15   30
Distance:  9  40  200
"""


def parse(data):
    lines = data.splitlines()
    times = [int(time) for time in re.findall(r"(\d+)", lines[0])]
    dists = [int(dist) for dist in re.findall(r"(\d+)", lines[1])]
    return times, dists


def part_1(times, dists):
    tot = 1
    for i in range(len(times)):
        race = 0
        for j in range(times[i] + 1):
            if dists[i] < j * (times[i] - j):
                race += 1
        tot *= race
    print(tot)


def part_2(times, dists):
    times = [str(i) for i in times]
    time = int("".join(times))
    dists = [str(i) for i in dists]
    dist = int("".join(dists))

    race = 0
    for j in range(time + 1):
        if dist < j * (time - j):
            race += 1
    print(race)


times, dists = parse(puzzle)
part_1(times, dists)
part_2(times, dists)
