from aocd import get_data

YEAR, DAY = 2015, 1
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
()())
"""


def day_1(data):
    total = 0
    chars = 0
    locs = []
    for i in data.strip():
        if i == "(":
            total += 1
        if i == ")":
            total += -1
        chars += 1
        if total == -1:
            locs.append(chars)
    print("part 1: ", total)
    print("part 2: ", locs[0])


day_1(puzzle)
