from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 6
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


@timing
def parse(data):
    rows = data.strip().split()
    grid = {}
    for i, row in enumerate(rows):
        for j, typ in enumerate(row):
            if typ == "^":
                start = (i, j)
                grid[(i, j)] = "."
            else:
                grid[(i, j)] = typ
    return start, grid


@timing
def part_1(start, grid):
    edge = max(grid)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visited = set()
    visited.add(start)

    loc = start
    dir_ind = 0

    while True:
        new_loc = (loc[0] + dirs[dir_ind][0], loc[1] + dirs[dir_ind][1])
        if (
            new_loc[0] < 0
            or new_loc[0] > edge[0]
            or new_loc[1] < 0
            or new_loc[1] > edge[1]
        ):
            return visited

        if grid[new_loc] == "#":
            dir_ind = (dir_ind + 1) % 4
            loc = (loc[0] + dirs[dir_ind][0], loc[1] + dirs[dir_ind][1])
        else:
            loc = new_loc

        visited.add(loc)


@timing
def part_2(start, grid, open_spots):
    edge = max(grid)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    blocked = []
    left = []
    open_spots.remove(start)

    for spot in open_spots:
        grid[spot] = "#"

        visited = set()

        loc = start
        dir_ind = 0

        visited.add((loc, dir_ind))

        while True:
            new_loc = (loc[0] + dirs[dir_ind][0], loc[1] + dirs[dir_ind][1])
            if (
                new_loc[0] < 0
                or new_loc[0] > edge[0]
                or new_loc[1] < 0
                or new_loc[1] > edge[1]
            ):
                left.append(spot)
                grid[spot] = "."
                break

            if (new_loc, dir_ind) in visited:
                blocked.append(spot)
                grid[spot] = "."
                break

            if grid[new_loc] == "#":
                dir_ind = (dir_ind + 1) % 4
                new_loc = (loc[0] + dirs[dir_ind][0], loc[1] + dirs[dir_ind][1])
                if grid[new_loc] == "#":
                    dir_ind = (dir_ind + 1) % 4
                    loc = (loc[0] + dirs[dir_ind][0], loc[1] + dirs[dir_ind][1])
                else:
                    loc = new_loc
            else:
                loc = new_loc

            visited.add((loc, dir_ind))

    return len(blocked)


start, grid = parse(puzzle)
visited = part_1(start, grid)
print("part 1: ", len(visited))
print("part 2: ", part_2(start, grid, visited))
