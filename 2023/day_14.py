import numpy as np
from datetime import datetime
from functools import cache
from aocd import get_data

YEAR, DAY = 2023, 14
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


@cache
def shift_rocks_NW(rows):
    moved = []
    for row in rows:
        sections = row.split("#")
        moved_sections = []
        for section in sections:
            rnd = section.count("O")
            rolled = "" + ("O" * rnd) + ("." * (len(section) - rnd))
            moved_sections.append(rolled)
        moved.append("#".join(moved_sections))
    return tuple(moved)


@cache
def shift_rocks_SE(rows):
    moved = []
    for row in rows:
        sections = row.split("#")
        moved_sections = []
        for section in sections:
            rnd = section.count("O")
            rolled = "" + ("." * (len(section) - rnd)) + ("O" * rnd)
            moved_sections.append(rolled)
        moved.append("#".join(moved_sections))
    return tuple(moved)


@cache
def shift_cycle(rows):
    N_rows = ("".join(s) for s in zip(*rows))
    N_moved = shift_rocks_NW(N_rows)
    W_rows = ("".join(s) for s in zip(*N_moved))
    W_moved = shift_rocks_NW(W_rows)
    S_rows = ("".join(s) for s in zip(*W_moved))
    S_moved = shift_rocks_SE(S_rows)
    E_rows = ("".join(s) for s in zip(*S_moved))
    E_moved = shift_rocks_SE(E_rows)

    return E_moved


def part_1(data):
    scriptstart = datetime.now()
    rows = data.strip().split()
    max_dist = len(rows)
    t_rows = ("".join(s) for s in zip(*rows))

    moved = shift_rocks_NW(t_rows)

    load = 0
    for row in moved:
        for i, space in enumerate(row):
            load += (max_dist - i) if space == "O" else 0
    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"{scriptend}: Part 1 complete in seconds: {elapsed_sec}")
    print("part 1: ", load)


def part_2(data):
    scriptstart = datetime.now()
    rows = tuple(data.strip().split())
    max_dist = len(rows)

    for i in range(1000000000):
        rows = shift_cycle(rows)

    moved = ("".join(s) for s in zip(*rows))

    load = 0
    for row in moved:
        for i, space in enumerate(row):
            load += (max_dist - i) if space == "O" else 0
    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"\n{scriptend}: Part 2 complete in seconds: {elapsed_sec}")
    print("part 2: ", load)


part_1(puzzle)
part_2(puzzle)
