import re
from operator import itemgetter
from aocd import get_data

YEAR, DAY = 2023, 7
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


def part_1(data):
    order = "AKQJT98765432"
    hands = [[hand, int(bet)] for (hand, bet) in re.findall(r"(\S{5}) (\d+)", data)]

    for hand in hands:
        cards = dict.fromkeys(hand[0], 0)
        for card in hand[0]:
            cards[card] += 1
        counts = sorted(list(cards.values()), reverse=True)
        if counts[0] == 3 and counts[1] == 2:
            hand.insert(0, 3)
        elif counts[0] == 2 and counts[1] == 2:
            hand.insert(0, 5)
        elif counts[0] == 5:
            hand.insert(0, 1)
        elif counts[0] == 4:
            hand.insert(0, 2)
        elif counts[0] == 3:
            hand.insert(0, 4)
        elif counts[0] == 2:
            hand.insert(0, 6)
        elif counts[0] == 1:
            hand.insert(0, 7)

    sort_1 = sorted(hands, key=lambda word: [order.index(c) for c in word[1]])
    sorted_hands = sorted(sort_1, key=itemgetter(0))

    tot = 0
    for i, hand in enumerate(reversed(sorted_hands)):
        tot += (i + 1) * hand[2]
    print("part 1: ", tot)


def part_2(data):
    order = "AKQT98765432J"
    hands = [[hand, int(bet)] for (hand, bet) in re.findall(r"(\S{5}) (\d+)", data)]

    for hand in hands:
        cards = dict.fromkeys(hand[0], 0)
        for card in hand[0]:
            cards[card] += 1
        if "J" in (cards.keys()):
            if cards["J"] == 5:
                pass
            else:
                js = cards["J"]
                del cards["J"]
                cards[max(cards, key=cards.get)] += js

        counts = sorted(list(cards.values()), reverse=True)

        if counts[0] == 3 and counts[1] == 2:
            hand.insert(0, 3)
        elif counts[0] == 2 and counts[1] == 2:
            hand.insert(0, 5)
        elif counts[0] == 5:
            hand.insert(0, 1)
        elif counts[0] == 4:
            hand.insert(0, 2)
        elif counts[0] == 3:
            hand.insert(0, 4)
        elif counts[0] == 2:
            hand.insert(0, 6)
        elif counts[0] == 1:
            hand.insert(0, 7)

    sort_1 = sorted(hands, key=lambda word: [order.index(c) for c in word[1]])
    sorted_hands = sorted(sort_1, key=itemgetter(0))

    tot = 0
    for i, hand in enumerate(reversed(sorted_hands)):
        tot += (i + 1) * hand[2]
    print("part 2: ", tot)


part_1(puzzle)
part_2(puzzle)
