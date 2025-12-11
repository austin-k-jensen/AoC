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


def parse(data: str):
    devices = {}
    for device in data.strip().splitlines():
        device, cons = device.split(": ")[0], device.split(": ")[1].split()
        devices[device] = cons

    return devices


def part_1(devices: dict) -> int:

    start = "you"
    check = [start]
    paths = 0

    while check:
        loc = check.pop()
        if loc == "out":
            paths += 1
            continue
        check += devices[loc]

    return paths


def part_2(devices: dict):

    start = "svr"
    check = [[start]]
    paths = 0

    while check:
        path = check.pop()
        loc = path[-1]
        # print(path)

        if loc == "out":
            if "fft" in path and "dac" in path:
                print(path)
                paths += 1
            continue

        for next_loc in devices[loc]:
            if next_loc in path:
                print("hmm")
            next_path = path + [next_loc]
            check.append(next_path)

    print(paths)


devices = parse(puzzle)
# print("part 1: ", part_1(devices))
part_2(devices)
