from re import split
from collections import defaultdict
from aocd import get_data

YEAR, DAY = 2023, 15
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def hash_map(item):
    val = 0
    for char in item:
        val += ord(char)
        val *= 17
        val %= 256
    return val


def part_1(data):
    seq = data.split(",")

    total = 0
    for step in seq:
        total += hash_map(step)
    print("part 1: ", total)


def part_2(data):
    seq = [split("=|-", step) for step in data.split(",")]

    boxes = defaultdict(list)

    for label, lense in seq:
        if lense != "":
            if any(label in item for item in boxes[hash_map(label)]):
                for item in boxes[hash_map(label)]:
                    if label in item:
                        item[1] = lense
            else:
                boxes[hash_map(label)].append([label, lense])
        else:
            for item in boxes[hash_map(label)]:
                if label in item:
                    boxes[hash_map(label)].remove(item)

    total = 0
    for box in boxes:
        for i, item in enumerate(boxes[box]):
            total += (box + 1) * (i + 1) * int(item[1])
    print("part 2: ", total)


part_1(puzzle)
part_2(puzzle)
