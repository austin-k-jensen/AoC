from aocd import get_data

YEAR, DAY = 2024, 1
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def parse(data):
    numbers = data.strip().split()
    numbers = [int(x) for x in numbers]
    left = numbers[::2]
    right = numbers[1::2]
    return left, right


def part_1(left, right):
    left.sort()
    right.sort()

    tot = 0
    for l, r in zip(left, right):
        tot += abs(r - l)

    return tot


def part_2(left, right):
    tot = 0
    for l in left:
        tot += l * right.count(l)
    return tot


left, right = parse(puzzle)
print("part 1: ", part_1(left, right))
print("part 2: ", part_2(left, right))
