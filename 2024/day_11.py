from aocd import get_data
from functools import cache
from utils import timing

YEAR, DAY = 2024, 11
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "125 17"


@cache
def blink(stone: str, blinks_rem: int):
    new_stones = []
    blinks_rem -= 1

    if stone == "0":
        new_stones.append("1")
    elif len(stone) % 2 == 0:
        midpoint = len(stone) // 2
        new_stones.append(str(int(stone[:midpoint])))
        new_stones.append(str(int(stone[midpoint:])))
    else:
        new_stones.append(str(int(stone) * 2024))

    out = 0
    if blinks_rem == 0:
        out += len(new_stones)
    else:
        for stone in new_stones:
            out += blink(stone, blinks_rem)

    return out


@timing
def solve(data: str, blinks: int):
    stones = data.split()

    tot = 0
    for stone in stones:
        tot += blink(stone, blinks)

    return tot


print("part 1: ", solve(puzzle, 25))
print("part 2: ", solve(puzzle, 75))
