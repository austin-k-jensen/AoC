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


def part_1(data, sub: bool = False):
    p1_answer = 0
    for line in iter(data.splitlines()):
        card = line.split(":")[1].split("|")
        win = card[0].split(" ")
        nums = card[1].split(" ")
        while "" in win:
            win.remove("")
        while "" in nums:
            nums.remove("")

        result = set(nums).intersection(win)
        matchs = len(result)
        if matchs != 0:
            p1_answer += 2 ** (matchs - 1)

    print("part 1: ", p1_answer)

    if sub:
        submit(p1_answer, part="a", year=YEAR, day=DAY)


part_1(puzzle, sub=False)


def part_2(data, sub: bool = False):
    p2_answer = 0
    cards = {}
    for line in iter(data.splitlines()):
        game = int(re.findall(r"(\d+):", line)[0])
        cards[game] = {"cnt": 1, "matchs": 0}
        card = line.split(":")[1].split("|")
        win = card[0].split(" ")
        nums = card[1].split(" ")
        while "" in win:
            win.remove("")
        while "" in nums:
            nums.remove("")

        result = set(nums).intersection(win)
        matchs = len(result)
        cards[game]["matchs"] += matchs

    for card in cards:
        for i in range(card + 1, card + cards[card]["matchs"] + 1):
            cards[i]["cnt"] += 1 * cards[card]["cnt"]
        p2_answer += cards[card]["cnt"]

    print("part 2: ", p2_answer)

    if sub:
        submit(p2_answer, part="b", year=YEAR, day=DAY)


part_2(puzzle, sub=False)
