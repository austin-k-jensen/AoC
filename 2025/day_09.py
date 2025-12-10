from itertools import combinations
from shapely.geometry import Point, Polygon
from aocd import get_data

YEAR, DAY = 2025, 9
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


def parse(data: str) -> list:
    points = []
    for row in data.strip().splitlines():
        x, y = row.split(",")
        points.append((int(x), int(y)))

    return points


def part_1(points: list) -> int:
    max_a = 0
    for (x1, y1), (x2, y2) in combinations(points, 2):
        a = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if a > max_a:
            max_a = a

    return max_a


def part_2(points: list) -> int:
    shape = Polygon(points)

    max_a2 = 0

    for (x1, y1), (x2, y2) in combinations(points, 2):
        print(f"\t({x1},{y1})({x2},{y2})")
        a = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

        if a > max_a2:
            print(f"\tChecking polygon with area: {a}")

            if not (
                (shape.touches(Point(x1, y2)) or shape.within(Point(x1, y2)) or shape.contains(Point(x1, y2)))
                and (shape.touches(Point(x2, y1)) or shape.within(Point(x2, y1)) or shape.contains(Point(x2, y1)))
            ):
                print("\t\tCorners not in poly")
                continue

            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)

            print("\t\tChecking all points on edges")
            valid = True
            check = True
            for x in range(min_x, max_x + 1):
                if not (
                    (shape.touches(Point(x, y1)) or shape.within(Point(x, y1)) or shape.contains(Point(x, y1)))
                    and (shape.touches(Point(x, y2)) or shape.within(Point(x, y2)) or shape.contains(Point(x, y2)))
                ):
                    print("\t\tFound x point not in poly")
                    valid = False
                    check = False
                    break
            if check:
                for y in range(min_y, max_y + 1):
                    if not (
                        (shape.touches(Point(x1, y)) or shape.contains(Point(x1, y)) or shape.within(Point(x1, y)))
                        and (shape.touches(Point(x2, y)) or shape.contains(Point(x2, y)) or shape.within(Point(x2, y)))
                    ):
                        print("\t\tFoundy y point not in poly")
                        valid = False
                        break
                    # print((x, y1), (x, y2))

            if valid:
                max_a2 = a
                print(f"Max area is: {max_a2}")
    print(max_a2)

    # check = False
    # print((x1, y1), shape.touches(Point(3, 5)))


points = parse(puzzle)
# print("part 1: ", part_1(points))
part_2(points)
