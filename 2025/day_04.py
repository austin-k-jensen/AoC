from aocd import get_data

YEAR, DAY = 2025, 4
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def parse(data: str) -> set:
    rows = data.strip().split()
    rolls = set()
    for i, row in enumerate(rows):
        for j, letter in enumerate(row):
            if letter == "@":
                rolls.add((i, j))

    return rolls


def part_1(rolls: set) -> int:
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    count = 0
    for roll in rolls:
        nieghbors = 0
        for dir in dirs:
            if (roll[0] + dir[0], roll[1] + dir[1]) in rolls:
                nieghbors += 1

        if nieghbors < 4:
            count += 1

    return count


def remove_rolls(rolls: set) -> set:
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for roll in rolls.copy():
        nieghbors = 0
        for dir in dirs:
            if (roll[0] + dir[0], roll[1] + dir[1]) in rolls:
                nieghbors += 1

        if nieghbors < 4:
            rolls.remove(roll)

    return rolls


def part_2(rolls: set) -> int:
    start_count = len(rolls)
    count = start_count

    while True:
        rolls = remove_rolls(rolls)
        new_count = len(rolls)
        if new_count == count:
            break
        count = new_count

    return start_count - count


rolls = parse(puzzle)
print("part 1: ", part_1(rolls))
print("part 2: ", part_2(rolls))
