import re
from math import lcm
from aocd import get_data

YEAR, DAY = 2023, 20
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

TEST_2 = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""


def parse(data):
    modules = {}
    for module in data.strip().splitlines():
        module = re.findall(r"([%&])?(\w+) -> (\w+(?:, \w+)*)", module)[0]
        modules[module[1]] = {}
        modules[module[1]]["out"] = module[2].split(", ")
        modules[module[1]]["type"] = module[0]
        modules[module[1]]["state"] = False
        modules[module[1]]["mem"] = {}

    for mod, info in modules.items():
        for out in info["out"]:
            if out in modules:
                if modules[out]["type"] == "&":
                    modules[out]["mem"][mod] = 0

    return modules


def button(modules, rx_in={}, presses=0):
    check = [("button", "broadcaster", 0)]
    presses += 1
    low = 1
    high = 0

    while check:
        curr = check.pop(0)

        if curr[1] not in modules:
            continue

        if curr[1] == "broadcaster":
            pulse = 0
            for mod in modules[curr[1]]["out"]:
                low += 1
                check.append((curr[1], mod, pulse))

        if modules[curr[1]]["type"] == "%" and curr[2] == 0:
            modules[curr[1]]["state"] = not modules[curr[1]]["state"]
            for mod in modules[curr[1]]["out"]:
                if modules[curr[1]]["state"]:
                    pulse = 1
                    high += 1
                else:
                    pulse = 0
                    low += 1
                check.append((curr[1], mod, pulse))

        if modules[curr[1]]["type"] == "&":
            modules[curr[1]]["mem"][curr[0]] = curr[2]
            for mod in modules[curr[1]]["out"]:
                if all(value == 1 for value in modules[curr[1]]["mem"].values()):
                    pulse = 0
                    low += 1
                else:
                    pulse = 1
                    high += 1
                check.append((curr[1], mod, pulse))

        if curr[1] == "vr" and curr[2] == 1:
            if curr[1] not in rx_in:
                rx_in[curr[0]] = presses

    return low, high, rx_in, presses


def part_1(modules):
    low = 0
    high = 0
    for _ in range(1000):
        low_rnd, high_rnd, _, _ = button(modules)
        low += low_rnd
        high += high_rnd

    print("part 1: ", low * high)


def part_2(modules):
    rx_in = {}
    presses = 0

    while len(rx_in) < len(modules["vr"]["mem"]):
        _, _, rx_in, presses = button(modules, rx_in, presses)

    print("part 2: ", lcm(*[v for (_, v) in rx_in.items()]))


modules = parse(puzzle)
part_1(modules)
modules = parse(puzzle)
part_2(modules)
