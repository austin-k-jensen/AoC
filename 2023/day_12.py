import re
from datetime import datetime
from itertools import product
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

TEST_2 = """
.??..??...?##. 1,1,3
"""


def part_1(data):
    scriptstart = datetime.now()

    records = [
        (string, [int(x) for x in lst.split(",")])
        for (string, lst) in re.findall(r"([?.#]+) (\d+(?:,*\d+)+)", data)
    ]

    arrangement = 0
    for record, cnts in records:
        chk = "^\.*"
        for cnt in cnts:
            chk += f"#{{{cnt}}}\.+"
        chk = chk[:-1] + "*$"

        for p in map(iter, product(".#", repeat=record.count("?"))):
            tst = "".join(c if c != "?" else next(p) for c in record)
            if re.match(chk, tst):
                arrangement += 1

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"{scriptend}: Part 1 complete in seconds: {elapsed_sec}")
    print("part 1: ", arrangement, "\n")


def spring_count(record, cnts):
    print(record, cnts)
    if len(record) == 0 and len(cnts) == 0:
        return 1
    if len(record) == 0 and len(cnts) > 0:
        return 0
    if record[0] == ".":
        spring_count(record[1:], cnts)


def part_2(data):
    scriptstart = datetime.now()

    # records = [
    #     ("?".join([string] * 5), [int(x) for x in lst.split(",")] * 5)
    #     for (string, lst) in re.findall(r"([?.#]+) (\d+(?:,*\d+)+)", data)
    # ]

    records = [
        (string, tuple([int(i) for i in lst.split(",")]))
        for (string, lst) in re.findall(r"([?.#]+) (\d+(?:,*\d+)+)", data)
    ]

    for record, cnts in records:
        spring_count(record, cnts)

    arrangement = 0
    # for record, cnts in records:
    #     chk = "^\.*"
    #     for cnt in cnts:
    #         chk += f"#{{{cnt}}}\.+"
    #     chk = chk[:-1] + "*$"
    #     print(chk)
    #     print(record, "\n")

    #     for p in map(iter, product(".#", repeat=record.count("?"))):
    #         tst = "".join(c if c != "?" else next(p) for c in record)
    #         if re.match(chk, tst):
    #             # print(tst)
    #             arrangement += 1

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"{scriptend}: Part 2 complete in seconds: {elapsed_sec}")
    print("part 2: ", arrangement)


# part_1(TEST_1)
part_2(TEST_2)
