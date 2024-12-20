from aocd import get_data

YEAR, DAY = 2015, 3
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = ">"
TEST_2 = "^>v<"
TEST_3 = "^v^v^v^v^v"


def part_1(input: str):
    move_dir = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
    loc = (0, 0)

    visited = set()
    visited.add(loc)

    for dir in input:
        loc = (loc[0] + move_dir[dir][0], loc[1] + move_dir[dir][1])
        visited.add(loc)

    return len(visited)


def part_2(input: str):
    move_dir = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
    loc = (0, 0)

    visited = set()
    visited.add(loc)

    for dir in input[::2]:
        loc = (loc[0] + move_dir[dir][0], loc[1] + move_dir[dir][1])
        visited.add(loc)

    loc = (0, 0)
    for dir in input[1::2]:
        loc = (loc[0] + move_dir[dir][0], loc[1] + move_dir[dir][1])
        visited.add(loc)

    return len(visited)


print("part 1: ", part_1(puzzle))
print("part 2: ", part_2(puzzle))
