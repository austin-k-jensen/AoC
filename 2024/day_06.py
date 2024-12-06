from aocd import get_data

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


def part_2(start, grid, open_spots):
    edge = max(grid)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    blocked = []
    left = []
    open_spots.remove(start)

    for spot in open_spots:
        test_grid = grid.copy()
        test_grid[spot] = "#"

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
                break

            if (new_loc, dir_ind) in visited:
                blocked.append(spot)
                break

            if test_grid[new_loc] == "#":
                dir_ind = (dir_ind + 1) % 4
                new_loc = (loc[0] + dirs[dir_ind][0], loc[1] + dirs[dir_ind][1])
                if test_grid[new_loc] == "#":
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
