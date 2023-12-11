import re
from aocd import get_data

YEAR, DAY = 2023, 9
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def day_9(data):
    p1_answer = 0
    p2_answer = 0
    for line in iter(data.splitlines()):
        history = [int(point) for point in re.findall(r"-?\d+", line)]
        checks = []
        while not all(i == 0 for i in history):
            checks.append(history)
            next = []
            for i in range(len(history) - 1):
                next.append(history[i + 1] - history[i])
            history = next
        for i in range(len(checks) - 1, 0, -1):
            checks[i - 1].append(checks[i - 1][-1] + checks[i][-1])
            checks[i - 1].insert(0, checks[i - 1][0] - checks[i][0])
        p1_answer += checks[0][-1]
        p2_answer += checks[0][0]
    print("part 1: ", p1_answer, "\npart 2: ", p2_answer)


day_9(puzzle)
