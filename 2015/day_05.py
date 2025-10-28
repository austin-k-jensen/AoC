from aocd import get_data
from functools import wraps
from time import time

YEAR, DAY = 2015, 5
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
"""

TEST_2 = """
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy
"""


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"Function {f.__name__} took {te-ts:2.4f} seconds")
        return result

    return wrap


def parse(data):
    strs = [x for x in data.strip().splitlines()]
    return strs


@timing
def part_1(strs: list):
    nice = 0
    for i in strs:
        # print(i)

        vowels = "aeiouAEIOU"
        three_vowls = True if sum([1 for char in i if char in vowels]) >= 3 else False
        # print(f"\tThree Vowels: {three_vowls}")

        dbl_letter = False
        for j in range(len(i) - 1):
            if i[j] == i[j + 1]:
                dbl_letter = True
                break
        # print(f"\tDouble Letter: {dbl_letter}")

        bad_strs = ["ab", "cd", "pq", "xy"]
        bad_str = True
        for bad_i in bad_strs:
            if bad_i in i:
                bad_str = False
                break
        # print(f"\tBad string: {bad_str}")

        if three_vowls and dbl_letter and bad_str:
            nice += 1

    return nice


@timing
def part_2(strs: list):
    nice = 0
    for i in strs:
        # print(i)

        c1 = False
        for j in range(len(i) - 1):
            if i.count(i[j : j + 2]) > 1:
                c1 = True
                break
        # print(f"\tC1: {c1}")

        c2 = False
        for j in range(len(i) - 2):
            if i[j] == i[j + 2]:
                c2 = True
                break
        # print(f"\tC2: {c2}")

        if c1 and c2:
            nice += 1
    return nice


strs = parse(puzzle)
print("part 1: ", part_1(strs))
print("part 2: ", part_2(strs))
