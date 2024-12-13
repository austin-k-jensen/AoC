from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 12
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
AAAA
BBCD
BBCC
EEEC
"""

TEST_2 = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""

TEST_3 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""


@timing
def parse(data):
    grid = {}
    for i, row in enumerate(data.strip().split()):
        for j, plot in enumerate(row):
            grid[(i, j)] = plot
    return grid


def search(grid: dict, edge: tuple, plot_ids: dict, plot: tuple, region_id: int):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    plot_ids[plot] = region_id

    # print(f"Checking {plot}:{grid[plot]}")

    for dir in dirs:
        new_plot = (plot[0] + dir[0], plot[1] + dir[1])
        if (0 <= new_plot[0] <= edge[0]) and (0 <= new_plot[1] <= edge[1]):
            # print(f"\tChecking {new_plot}:{grid[new_plot]}")
            if new_plot in plot_ids:
                continue
            if grid[new_plot] == grid[plot]:
                plot_ids[new_plot] = region_id
                search(grid, edge, plot_ids, new_plot, region_id)


@timing
def make_regions(grid):
    edge = max(grid)

    plot_ids = {}
    id = 0
    for plot in grid:
        if plot not in plot_ids:
            search(grid, edge, plot_ids, plot, id)
            id += 1

    regions = {}
    for plot, id in plot_ids.items():
        if id in regions:
            regions[id].append(plot)
        else:
            regions[id] = [plot]

    return regions


def is_out(edge: tuple, polt: tuple):
    out = False
    if polt[0] < 0 or polt[0] > edge[0] or polt[1] < 0 or polt[1] > edge[1]:
        out = True

    return out


@timing
def part_1(grid: dict, regions: dict):
    edge = max(grid)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    tot = 0
    for id in regions:
        area = 0
        perim = 0

        for plot in regions[id]:
            area += 1
            for dir in dirs:
                new_plot = (plot[0] + dir[0], plot[1] + dir[1])
                if is_out(edge, new_plot):
                    perim += 1
                else:
                    if grid[plot] != grid[new_plot]:
                        perim += 1
        tot += area * perim
    return tot


@timing
def part_2(grid: dict, regions: dict):
    edge = max(grid)

    NW = ((-1, 0), (0, -1), (-1, -1))
    NE = ((-1, 0), (0, 1), (-1, 1))
    SE = ((1, 0), (0, 1), (1, 1))
    SW = ((1, 0), (0, -1), (1, -1))
    dirs = [NW, NE, SE, SW]

    tot = 0
    for id in regions:
        area = 0
        corner = 0

        for plot in regions[id]:
            area += 1
            for dir in dirs:
                dx = (plot[0] + dir[0][0], plot[1] + dir[0][1])
                dy = (plot[0] + dir[1][0], plot[1] + dir[1][1])
                dxy = (plot[0] + dir[2][0], plot[1] + dir[2][1])

                x_diff = False
                y_diff = False
                xy_diff = False

                if is_out(edge, dx):
                    x_diff = True
                elif grid[dx] != grid[plot]:
                    x_diff = True

                if is_out(edge, dy):
                    y_diff = True
                elif grid[dy] != grid[plot]:
                    y_diff = True

                if is_out(edge, dxy):
                    xy_diff = True
                elif grid[dxy] != grid[plot]:
                    xy_diff = True

                if x_diff and y_diff:
                    corner += 1
                if not x_diff and not y_diff and xy_diff:
                    corner += 1
        tot += area * corner

    return tot


grid = parse(puzzle)
regions = make_regions(grid)
print("part 1: ", part_1(grid, regions))
print("part 2: ", part_2(grid, regions))
