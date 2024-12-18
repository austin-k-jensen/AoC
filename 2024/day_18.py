from heapq import heappush, heappop
from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 18
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""


def parse(data):
    blocks = []
    for line in data.strip().splitlines():
        x, y = line.split(",")
        blocks.append((int(x), int(y)))

    return blocks


def path(blocks: list, size: int, byte_cnt: int):
    blocks = set(blocks[:byte_cnt])
    start, end = (0, 0), (size, size)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    check = [(0, start)]
    visited = set()

    steps = 0
    while check:
        steps, loc = heappop(check)

        if loc == end:
            return steps

        if loc in visited:
            continue

        visited.add(loc)

        for dir in dirs:
            new_loc = (loc[0] + dir[0], loc[1] + dir[1])
            if (
                (0 <= new_loc[0] <= size)
                and (0 <= new_loc[1] <= size)
                and new_loc not in blocks
            ):
                heappush(check, (steps + 1, new_loc))


@timing
def part_1(blocks: list, size: int, byte_cnt: int):
    return path(blocks=blocks, size=size, byte_cnt=byte_cnt)


@timing
def part_2(blocks: list, size: int, start_byte: int):
    start, end = start_byte, len(blocks)

    while end - start > 1:
        block = start + (end - start) // 2

        if path(blocks=blocks, size=size, byte_cnt=block):
            start = block
        else:
            end = block

    return blocks[block - 1]


# part_1(blocks=parse(TEST_1), size=6, byte_cnt=12)
print("part 1: ", part_1(blocks=parse(puzzle), size=70, byte_cnt=1024))
# part_2(blocks=parse(TEST_1), size=6, start_byte=12)
print("part 2: ", part_2(blocks=parse(puzzle), size=70, start_byte=1024))
