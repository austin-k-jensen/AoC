from re import match
from aocd import get_data

YEAR, DAY = 2025, 2
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def parse(data: str):
    rngs = []
    for rng in data.strip().split(","):
        x, y = rng.split("-")
        rngs.append((int(x), int(y)))
    return rngs


def part_1(rngs: list):
    ids = []
    for rng in rngs:
        for i in range(rng[0], rng[1] + 1):
            str_i = str(i)
            str_len = len(str_i)
            if str_len % 2 == 0:
                if str_i[: (str_len // 2)] == str_i[(str_len // 2) :]:
                    ids.append(i)

    return sum(ids)


def part_2(rngs: list):
    ids = []
    for rng in rngs:
        for i in range(rng[0], rng[1] + 1):
            if match(r"^(\d+)\1+$", str(i)):
                ids.append(i)

    return sum(ids)


rngs = parse(puzzle)
print("part 1: ", part_1(rngs))
print("part 2: ", part_2(rngs))
