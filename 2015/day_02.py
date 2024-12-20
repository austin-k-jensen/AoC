from aocd import get_data

YEAR, DAY = 2015, 2
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
2x3x4
1x1x10
"""


def parse(data):
    boxes = []
    for package in data.strip().splitlines():
        boxes.append([int(x) for x in package.split("x")])
    return boxes


def part_1(boxes: list):
    tot = 0
    for l, h, w in boxes:
        faces = [l * h, l * w, h * w]
        tot += sum([min(faces)] + faces * 2)
    return tot


def part_2(boxes: list):
    tot = 0
    for box in boxes:
        tot += sum(sorted(box)[:2] * 2)
        l, h, w = box
        tot += l * h * w
    return tot


boxes = parse(puzzle)
print("part 1: ", part_1(boxes))
print("part 2: ", part_2(boxes))
