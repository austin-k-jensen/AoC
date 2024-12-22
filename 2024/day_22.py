from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 22
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
1
10
100
2024
"""

TEST_2 = """
1
2
3
2024
"""


def parse(data: str):
    codes = [int(x) for x in data.strip().splitlines()]
    return codes


@timing
def both(codes: list):
    comb_dict = {}
    tot = 0
    for code in codes:
        comp_dict = {}
        for i in range(2000):
            digit = code % 10
            if i == 0:
                last_digit = digit
                diffs = []
            if 0 < i < 4:
                diff = digit - last_digit
                diffs.append(diff)
                last_digit = digit
            else:
                diff = digit - last_digit
                last_digit = digit
                comps = tuple(diffs[1:]) + (diff,)
                diffs = list(comps)
            if comps == (0,):
                pass
            elif comps in comp_dict:
                pass
            else:
                comp_dict[comps] = digit

            code = code ^ code * 64 % 16777216
            code = code ^ code // 32 % 16777216
            code = code ^ code * 2048 % 16777216

        tot += code

        for comb in comp_dict:
            if comb in comb_dict:
                comb_dict[comb] += comp_dict[comb]
            else:
                comb_dict[comb] = comp_dict[comb]

    best = 0
    for k, v in comb_dict.items():
        if v > best:
            out = k
            best = v

    return tot, best


codes = parse(puzzle)
part_1, part_2 = both(codes)
print("part 1: ", part_1)
print("part 2: ", part_2)
