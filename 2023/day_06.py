import re
from aocd import get_data
from aocd import submit

YEAR, DAY = 2023, 6
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """Time:      7  15   30
Distance:  9  40  200
"""


def part_1(data):
    lines = data.splitlines()
    times = [int(time) for time in re.findall(r"(\d+)", lines[0])]
    dists = [int(dist) for dist in re.findall(r"(\d+)", lines[1])]

    tot = 1
    for i in range(len(times)):
        race = 0
        for j in range(times[i] + 1):
            if dists[i] < j * (times[i] - j):
                race += 1
        tot *= race
    print("part 1: ", tot)


def part_2(data):
    lines = data.splitlines()
    time = int("".join(re.findall(r"(\d+)", lines[0])))
    dist = int("".join(re.findall(r"(\d+)", lines[1])))

    race = 0
    for j in range(time + 1):
        if dist < j * (time - j):
            race += 1
    print("part 2 ", race)


part_1(puzzle)
part_2(puzzle)
