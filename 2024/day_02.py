from aocd import get_data

YEAR, DAY = 2024, 2
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def parse(data):
    reports = []
    for row in data.strip().splitlines():
        reports.append([int(x) for x in row.split()])
    return reports


def check_safe(report):
    increase = all(i < j for i, j in zip(report, report[1:]))
    decrease = all(i > j for i, j in zip(report, report[1:]))
    safe_diff = all(0 < abs(i - j) < 4 for i, j in zip(report, report[1:]))

    safe = 1 if (increase or decrease) and safe_diff else 0
    return safe


def part_1(reports):
    safe_1 = 0
    safe_2 = 0
    unsafe = []

    for report in reports:
        if check_safe(report) == 1:
            safe_1 += 1
        else:
            unsafe.append(report)

    for report in unsafe:
        for i, _ in enumerate(report):
            test = report[:i] + report[i + 1 :]
            if check_safe(test) == 1:
                safe_2 += 1
                break

    safe_2 = safe_1 + safe_2

    return safe_1, safe_2


reports = parse(puzzle)
safe_1, safe_2 = part_1(reports)
print("part 1: ", safe_1, "\npart 2: ", safe_2)
