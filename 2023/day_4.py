import re
from aocd import get_data
from aocd import submit

YEAR, DAY = 2023, 4
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def parse(data):
    cards = {}
    for line in iter(data.splitlines()):
        game = int(re.findall(r"(\d+):", line)[0])
        cards[game] = {"cnt": 1, "matchs": 0}
        card = line.split(":")[1].split("|")
        win = card[0].split()
        nums = card[1].split()

        cards[game]["matchs"] += len(set(nums).intersection(win))

    return cards


def part_1(data, sub: bool = False):
    p1_answer = 0
    for card in data:
        if data[card]["matchs"] != 0:
            p1_answer += 2 ** (data[card]["matchs"] - 1)

    print("part 1: ", p1_answer)

    if sub:
        submit(p1_answer, part="a", year=YEAR, day=DAY)


def part_2(data, sub: bool = False):
    p2_answer = 0
    for card in data:
        for i in range(card + 1, card + data[card]["matchs"] + 1):
            data[i]["cnt"] += 1 * data[card]["cnt"]
        p2_answer += data[card]["cnt"]

    print("part 2: ", p2_answer)

    if sub:
        submit(p2_answer, part="b", year=YEAR, day=DAY)


cards = parse(puzzle)
part_1(cards, sub=False)
part_2(cards, sub=False)
