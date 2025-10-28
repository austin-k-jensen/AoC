from collections import defaultdict
import re
from aocd import get_data
from functools import wraps
from time import time

YEAR, DAY = 2015, 6
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
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


@timing
def parse(data):
    insrcts = []

    for insrct in data.strip().split("\n"):
        # print(insrct)

        if insrct.startswith("turn on"):
            order = 1
        elif insrct.startswith("toggle"):
            order = 0
        elif insrct.startswith("turn off"):
            order = -1
        else:
            raise
        # print(order)

        coords = [int(x) for x in re.findall(r"\d+", insrct)]
        # print(coords)

        insrcts.append((order, (coords[0], coords[1]), (coords[2], coords[3])))

    return insrcts


@timing
def both(insrcts: list):
    state_1 = defaultdict(int)
    state_2 = defaultdict(int)

    for insrct in insrcts:
        for i in range(insrct[1][0], insrct[2][0] + 1):
            for j in range(insrct[1][1], insrct[2][1] + 1):
                if insrct[0] == -1:
                    state_1[(i, j)] = 0

                    if state_2[(i, j)] > 0:
                        state_2[(i, j)] += -1

                elif insrct[0] == 1:
                    state_1[(i, j)] = 1
                    state_2[(i, j)] += 1
                elif insrct[0] == 0:
                    state_1[(i, j)] = abs(state_1[(i, j)] - 1)
                    state_2[(i, j)] += 2

    return sum(state_1.values()), sum(state_2.values())


insrcts = parse(puzzle)
part_1, part_2 = both(insrcts)
print("part 1: ", part_1)
print("part 2: ", part_2)
