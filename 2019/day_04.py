import re
from aocd import get_data

YEAR, DAY = 2019, 4
puzzle = get_data(day=DAY, year=YEAR)


def part_1():
    goods = []
    for num in range(377777, 800000):
        d0 = int(str(num)[0])
        d1 = int(str(num)[1])
        d2 = int(str(num)[2])
        d3 = int(str(num)[3])
        d4 = int(str(num)[4])
        d5 = int(str(num)[5])
        if (d0 <= d1 <= d2 <= d3 <= d4 <= d5) and (
            d0 == d1 or d1 == d2 or d2 == d3 or d3 == d4 or d4 == d5
        ):
            goods.append(str(num))

    return goods


def part_2(pos: list):
    cnt = 0
    for num in pos:
        matches = re.findall(r"(?=(\d)\1)", num)

        if len(matches) == 1:
            pass
        else:
            removes = set()
            for i in range(len(matches) - 1):
                if matches[i] == matches[i + 1]:
                    removes.add(matches[i])

            for val in removes:
                matches = list(filter((val).__ne__, matches))

        if len(matches) > 0:
            cnt += 1

    return cnt


goods = part_1()
print("Part 1:", len(goods))
print("Part 2:", part_2(goods))
