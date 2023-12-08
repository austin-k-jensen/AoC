import re
from aocd import get_data
from itertools import cycle
from math import lcm

YEAR, DAY = 2023, 8
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

TEST_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

TEST_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""


def part_1(data):
    turns = re.findall(r"([RL]+)\n", data)[0]
    maps = re.findall(r"(\w{3}) = \((\w{3}), (\w{3})", data)

    nodes = {}
    for i, k, j in maps:
        nodes[i] = (k, j)

    steps = 0
    cur_loc = "AAA"
    for turn in cycle(turns):
        if cur_loc == "ZZZ":
            break
        else:
            steps += 1
            if turn == "R":
                cur_loc = nodes[cur_loc][1]
            if turn == "L":
                cur_loc = nodes[cur_loc][0]
    print("part 1: ", steps)


def part_2(data):
    turns = re.findall(r"([RL]+)\n", data)[0]
    maps = re.findall(r"(\w{3}) = \((\w{3}), (\w{3})", data)
    starts = re.findall(r"(\w{2}A) =", data)

    nodes = {}
    for i, k, j in maps:
        nodes[i] = (k, j)

    all_steps = []
    for start in starts:
        steps = 0
        for turn in cycle(turns):
            if start[2] == "Z":
                break
            else:
                steps += 1
                if turn == "R":
                    start = nodes[start][1]
                if turn == "L":
                    start = nodes[start][0]
        all_steps.append(steps)
    print("part 2: ", lcm(*all_steps))


part_1(puzzle)
part_2(puzzle)
