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
    rows = data.strip().split()
    max_dist = len(rows)
    t_rows = ("".join(s) for s in zip(*rows))

    moved = shift_rocks_NW(t_rows)

    load = 0
    for row in moved:
        for i, space in enumerate(row):
            load += (max_dist - i) if space == "O" else 0

    print("part 1: ", load)


def part_2(data):
    rows = tuple(data.strip().split())
    max_dist = len(rows)

    seen = set()
    cycles = 0
    while rows not in seen:
        seen.add(rows)
        rows = shift_cycle(rows)
        cycles += 1

    first_cycle = rows
    rows = shift_cycle(rows)
    cycle_length = 1
    while rows != first_cycle:
        rows = shift_cycle(rows)
        cycle_length += 1

    remain = (1000000000 - (cycles - cycle_length)) % cycle_length

    for i in range(remain):
        rows = shift_cycle(rows)

    moved = ("".join(s) for s in zip(*rows))

    load = 0
    for row in moved:
        for i, space in enumerate(row):
            load += (max_dist - i) if space == "O" else 0

    print("part 2: ", load)


part_1(puzzle)
part_2(puzzle)
