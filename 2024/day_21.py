from functools import cache
from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 21
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
029A
980A
179A
456A
379A
"""


def parse(data: str):
    codes = data.strip().splitlines()
    return codes


@cache
def d_pad_moves(dirs: str, depth: int):

    dir_len = 0

    if depth == 0:
        dir_len += len(dirs)
        return dir_len

    new_dirs = ""
    loc = (0, 2)

    for dir in dirs:
        new_dirs = ""
        new_loc = d_pad[dir]
        dx, dy = new_loc[0] - loc[0], new_loc[1] - loc[1]

        if loc[0] == 0 and new_loc[1] == 0:
            new_dirs += "v" * dx
            new_dirs += "<" * abs(dy)
            dx, dy = 0, 0

        if loc[1] == 0 and new_loc[0] == 0:
            new_dirs += ">" * dy
            new_dirs += "^" * abs(dx)
            dx, dy = 0, 0

        if dy < 0:
            new_dirs += "<" * abs(dy)
        if dx > 0:
            new_dirs += "v" * dx
        if dx < 0:
            new_dirs += "^" * abs(dx)
        if dy > 0:
            new_dirs += ">" * dy

        new_dirs += "A"
        loc = new_loc

        dir_len += d_pad_moves(new_dirs, depth - 1)

    return dir_len


@timing
def both(codes: list):

    num_pad = {
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "0": (3, 1),
        "A": (3, 2),
    }

    tot_1 = 0
    tot_2 = 0
    for code in codes:
        dirs = ""
        loc = (3, 2)
        for button in code:
            new_loc = num_pad[button]
            dx, dy = new_loc[0] - loc[0], new_loc[1] - loc[1]

            if loc[0] == 3 and new_loc[1] == 0:
                dirs += "^" * abs(dx)
                dirs += "<" * abs(dy)
                dx, dy = 0, 0

            if loc[1] == 0 and new_loc[0] == 3:
                dirs += ">" * dy
                dirs += "v" * dx
                dx, dy = 0, 0

            if dy < 0:
                dirs += "<" * abs(dy)
            if dx > 0:
                dirs += "v" * dx
            if dx < 0:
                dirs += "^" * abs(dx)
            if dy > 0:
                dirs += ">" * dy
            dirs += "A"

            loc = new_loc

        dir_len_1 = d_pad_moves(dirs, 2)
        dir_len_2 = d_pad_moves(dirs, 25)

        tot_1 += dir_len_1 * int(code[:3])
        tot_2 += dir_len_2 * int(code[:3])

    return tot_1, tot_2


def main():
    global d_pad
    d_pad = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}

    codes = parse(puzzle)
    part_1, part_2 = both(codes)
    print("part 1: ", part_1)
    print("part 2: ", part_2)


if __name__ == "__main__":
    main()
