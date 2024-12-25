from itertools import product
from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 25
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""


def parse(data: str):

    locks, keys = [], []
    for block in data.strip().split("\n\n"):
        rows = block.splitlines()
        is_lock, is_key = False, False

        for i, row in enumerate(rows):
            if i == 0 and row == "#####":
                is_lock = True
                lock = [0, 0, 0, 0, 0]
            elif i == 0 and row == ".....":
                is_key = True
                key = [6, 6, 6, 6, 6]

            elif i == 6 and is_lock:
                locks.append(lock)
            elif i == 6 and is_key:
                keys.append(key)

            for j, typ in enumerate(row):
                if is_lock and typ == "#" and i > 0:
                    lock[j] += 1
                elif is_key and typ == ".":
                    key[j] -= 1

    return locks, keys


def part_1(locks: list, keys: list):
    tot = 0
    for lock, key in product(locks, keys):
        result = all((x + y) < 6 for x, y in zip(lock, key))
        if result:
            tot += 1
    print(tot)


locks, keys = parse(puzzle)
part_1(locks, keys)
