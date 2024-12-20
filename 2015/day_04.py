import hashlib
from aocd import get_data
from utils.functions import timing

YEAR, DAY = 2015, 4
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "abcdef"
TEST_2 = "pqrstuv"


@timing
def part_1(s_key: str):
    num = 0
    while True:
        _hash = s_key + str(num)
        check = hashlib.md5(_hash.encode()).hexdigest()

        if check[0:5] == "00000":
            return num

        num += 1


@timing
def part_2(s_key: str):
    num = 0
    while True:
        _hash = s_key + str(num)
        check = hashlib.md5(_hash.encode()).hexdigest()

        if check[0:6] == "000000":
            return num

        num += 1


print("part 1: ", part_1(puzzle))
print("part 2: ", part_2(puzzle))
