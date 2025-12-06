import itertools
from aocd import get_data

YEAR, DAY = 2025, 6
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def parse(data: str) -> dict:
    rec = {}
    for i, row in enumerate(data.strip().splitlines()):
        # print(i, row)
        for j, item in enumerate(row.split()):
            rec[(i, j)] = item

    return rec


def part_1(rec: dict) -> int:
    sign_row, probs = max(rec)
    tot = 0

    for i in range(probs + 1):
        sign = rec[(sign_row, i)]
        if sign == "*":
            num = 1
        elif sign == "+":
            num = 0

        num = int(rec[(0, i)])

        for j in range(sign_row - 1):
            # print(rec[(j + 1, i)])
            if sign == "*":
                num *= int(rec[(j + 1, i)])
            elif sign == "+":
                num += int(rec[(j + 1, i)])

        tot += num

    return tot


def parse_2(data: str):
    lines = data.splitlines()

    opps = lines[-1].split()
    nums = len(lines) - 1
    transposed_lines = list(zip(*lines[:-1]))

    reversed_lines = []
    for col in transposed_lines:
        reversed_lines.append("".join(col))

    probs = [
        list(y)
        for x, y in itertools.groupby(reversed_lines, lambda z: z == (" " * nums))
        if not x
    ]

    tot = 0
    for i, opp in enumerate(opps):
        num_tot = int(probs[i][0])

        for num in probs[i][1:]:
            if opp == "*":
                num_tot *= int(num)
            elif opp == "+":
                num_tot += int(num)

        tot += num_tot

    return tot


rec = parse(puzzle)
print("part 1: ", part_1(rec))
print("part 2: ", parse_2(puzzle))
