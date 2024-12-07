import re
from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 7
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def parse(data):
    eqs = []
    for line in iter(data.strip().splitlines()):
        eq = [int(x) for x in re.findall(r"(\d+)", line)]
        eqs.append(eq)
    return eqs


def eval(nums: list, ans: list):
    # print(nums)

    if len(nums) == 1:
        ans.append(nums[0])
        return

    num_1 = nums.pop(0)
    num_2 = nums.pop(0)

    eval([num_1 + num_2] + nums, ans)
    eval([num_1 * num_2] + nums, ans)


@timing
def part_1(eqs):
    tot = 0
    for eq in eqs:
        val = eq[0]
        nums = eq[1:]
        ans = []

        eval(nums, ans)

        tot += val if val in ans else 0
    return tot


def eval_2(nums: list, ans: list):
    # print(nums)

    if len(nums) == 1:
        ans.append(nums[0])
        return

    num_1 = nums.pop(0)
    num_2 = nums.pop(0)

    eval_2([num_1 + num_2] + nums, ans)
    eval_2([num_1 * num_2] + nums, ans)
    eval_2([int(str(num_1) + str(num_2))] + nums, ans)


@timing
def part_2(eqs):
    tot = 0
    for eq in eqs:
        val = eq[0]
        nums = eq[1:]
        ans = []

        eval_2(nums, ans)

        tot += val if val in ans else 0
    return tot


eqs = parse(puzzle)
# print("part 1: ", part_1(eqs))
print(part_2(eqs))
