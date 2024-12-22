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


def parse(data: str):
    codes = [int(x) for x in data.strip().splitlines()]
    return codes


@timing
def part_1(codes: list):
    tot = 0
    for code in codes:
        for _ in range(2000):
            code = code ^ code * 64 % 16777216
            code = code ^ code // 32 % 16777216
            code = code ^ code * 2048 % 16777216
        tot += code
    print(tot)


codes = parse(puzzle)
# codes = [123]
part_1(codes)
