from functools import cache
from aocd import get_data

YEAR, DAY = 2025, 11
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

TEST_2 = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""


def part_2(data: str):

    devices = {}
    for device in data.strip().splitlines():
        device, cons = device.split(": ")[0], device.split(": ")[1].split()
        devices[device] = cons

    @cache
    def count_paths(loc: str, end: str):
        paths = 0
        if loc == end:
            return 1
        if loc == "out":
            return 0
        else:
            for next_loc in devices[loc]:
                paths += count_paths(next_loc, end)

        return paths

    part_1 = count_paths("you", "out")

    part_2 = (
        count_paths("svr", "fft")
        * count_paths("fft", "dac")
        * count_paths("dac", "out")
    ) + (
        count_paths("svr", "dac")
        * count_paths("dac", "fft")
        * count_paths("fft", "out")
    )

    return part_1, part_2


a1, a2 = part_2(puzzle)
print("part 1: ", a1)
print("part 2: ", a2)
