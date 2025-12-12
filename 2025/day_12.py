from aocd import get_data

YEAR, DAY = 2025, 12
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""


def parse(data: str):
    data = data.strip().split("\n\n")
    _boxes = data[:-1]
    _regions = data[-1]

    boxes = {}
    for box in _boxes:
        lines = box.splitlines()
        box_num = int(lines[0].split(":")[0])
        coords = []
        for i, line in enumerate(lines[1:]):
            for j, char in enumerate(line):
                if char == "#":
                    coords.append((i, j))
        boxes[box_num] = coords

    regions = {}
    for i, region in enumerate(_regions.splitlines()):
        dims, reqs = region.split(": ")
        dims = tuple(map(int, dims.split("x")))
        reqs = [int(x) for x in reqs.split()]
        regions[i] = (dims, reqs)

    return boxes, regions


def part_1(boxes: dict, regions: dict):

    posible = 0
    good = 0
    for region in regions.values():
        dims, reqs = region

        area = dims[0] * dims[1]
        min_size = 0
        for i, req in enumerate(reqs):
            if req > 0:
                min_size += len(boxes[i]) * req
        if area < min_size:
            continue
        posible += 1

        num_boxes = sum(reqs)
        min_pack = (dims[0] // 3) * (dims[1] // 3)

        if num_boxes <= min_pack:
            good += 1
            continue

    if posible == good:
        return good


boxes, regions = parse(puzzle)
print("Part 1: ", part_1(boxes, regions))
