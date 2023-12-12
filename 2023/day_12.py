import re
from datetime import datetime
from functools import cache
from aocd import get_data

YEAR, DAY = 2023, 12
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


@cache
def spring_count(record, cnts):
    if len(record) == 0 and len(cnts) == 0:
        return 1
    if len(record) == 0 and len(cnts) > 0:
        return 0
    if record[0] == ".":
        return spring_count(record[1:], cnts)
    if record[0] == "?":
        return spring_count("." + record[1:], cnts) + spring_count(
            "#" + record[1:], cnts
        )
    if record[0] == "#":
        if len(cnts) == 0:
            return 0
        if len(record) < sum(cnts):
            return 0
        if "." in record[: cnts[0]]:
            return 0
        if len(cnts) > 1:
            if record[cnts[0]] == "#":
                return 0
            else:
                return spring_count(record[cnts[0] + 1 :], cnts[1:])
        if len(cnts) == 1:
            return spring_count(record[cnts[0] :], cnts[1:])


def part_1(data):
    scriptstart = datetime.now()

    records = [
        (string, tuple([int(x) for x in lst.split(",")]))
        for (string, lst) in re.findall(r"([?.#]+) (\d+(?:,*\d+)+)", data)
    ]

    arrangements = 0
    for record, cnts in records:
        arrangements += spring_count(record, cnts)

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"{scriptend}: Part 1 complete in seconds: {elapsed_sec}")
    print("part 1: ", arrangements)


def part_2(data):
    scriptstart = datetime.now()

    records = [
        ("?".join([string] * 5), tuple([int(x) for x in lst.split(",")] * 5))
        for (string, lst) in re.findall(r"([?.#]+) (\d+(?:,*\d+)+)", data)
    ]

    arrangements = 0
    for record, cnts in records:
        arrangements += spring_count(record, cnts)

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"\n{scriptend}: Part 2 complete in seconds: {elapsed_sec}")
    print("part 2: ", arrangements)


part_1(puzzle)
part_2(puzzle)
