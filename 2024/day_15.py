from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 15
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

TEST_2 = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv
<v>>v<<
"""

TEST_3 = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""


@timing
def parse(data: str):
    grid, moves = data.strip().split("\n\n")

    moves = moves.replace("\n", "")

    walls = []
    boxes = []
    for i, row in enumerate(grid.splitlines()):
        for j, typ in enumerate(row):
            if typ == "@":
                start = (i, j)
            elif typ == "#":
                walls.append((i, j))
            elif typ == "O":
                boxes.append((i, j))

    return moves, start, walls, boxes


@timing
def part_1(moves: str, start: tuple, walls: list, boxes: list):

    move_dir = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}

    loc = start

    for move in moves:
        dir = move_dir[move]

        # print(f"move: {move}")
        new_loc = (loc[0] + dir[0], loc[1] + dir[1])
        check = new_loc

        to_move = []
        checking = True
        move_boxes = True

        while checking:
            # print(f"\tChecking: {check}")
            if check in walls:
                # print("\tFound Wall, not moving")
                move_boxes, checking = False, False
            elif check in boxes:
                # print("\tFound box, adding to list")
                to_move.append(boxes.pop(boxes.index(check)))
                check = (check[0] + dir[0], check[1] + dir[1])
            else:
                # print("\tFound open spot, moving")
                loc = new_loc
                checking = False

        # print(f"\tmoved: {to_move}")

        for box in to_move:
            if move_boxes:
                boxes.append((box[0] + dir[0], box[1] + dir[1]))
            else:
                boxes.append(box)

        # print(f"\tboxes: {boxes}")
        # print(f"\tloc: {loc}")

    tot = 0
    for i, j in boxes:
        tot += i * 100 + j
    return tot


@timing
def parse_2(data: str):
    grid, moves = data.strip().split("\n\n")

    moves = moves.replace("\n", "")
    grid = grid.replace("#", "##")
    grid = grid.replace("O", "[]")
    grid = grid.replace(".", "..")
    grid = grid.replace("@", "@.")

    walls = []
    boxes = []
    for i, row in enumerate(grid.splitlines()):
        for j, typ in enumerate(row):
            if typ == "@":
                start = (i, j)
            elif typ == "#":
                walls.append((i, j))
            elif typ == "[":
                boxes.append(((i, j), (i, j + 1)))

    return moves, start, walls, boxes


@timing
def part_2(moves: str, start: tuple, walls: list, boxes: list):

    move_dir = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}

    loc = start

    for move in moves:
        dir = move_dir[move]

        # print(f"move: {move}")
        new_loc = (loc[0] + dir[0], loc[1] + dir[1])
        to_check = [new_loc]
        to_move = []
        move_boxes = True

        while to_check:
            check = to_check.pop()
            # print(f"\tChecking: {check}")

            if check in walls:
                # print("\tFound Wall, not moving")
                move_boxes = False
                break

            elif move in "<>":
                if (check, (check[0], check[1] + dir[1])) in boxes:
                    # print("\tFound box, adding to list")
                    to_move.append(
                        boxes.pop(boxes.index((check, (check[0], check[1] + dir[1]))))
                    )
                    to_check.append((check[0], check[1] + dir[1] * 2))

                elif ((check[0], check[1] + dir[1]), check) in boxes:
                    # print("\tFound box, adding to list")
                    to_move.append(
                        boxes.pop(boxes.index(((check[0], check[1] + dir[1]), check)))
                    )
                    to_check.append((check[0], check[1] + dir[1] * 2))

            elif move in "v^":
                if (check, (check[0], check[1] + 1)) in boxes:
                    # print("\tFound box, adding to list")
                    to_move.append(
                        boxes.pop(boxes.index((check, (check[0], check[1] + 1))))
                    )
                    to_check.append((check[0] + dir[0], check[1]))
                    to_check.append((check[0] + dir[0], check[1] + 1))
                elif ((check[0], check[1] - 1), check) in boxes:
                    # print("\tFound box, adding to list")
                    to_move.append(
                        boxes.pop(boxes.index(((check[0], check[1] - 1), check)))
                    )
                    to_check.append((check[0] + dir[0], check[1] - 1))
                    to_check.append((check[0] + dir[0], check[1]))

        # print(f"\tto move: {to_move}")
        if move_boxes:
            loc = new_loc
            for box_1, box_2 in to_move:
                boxes.append(
                    (
                        (box_1[0] + dir[0], box_1[1] + dir[1]),
                        (box_2[0] + dir[0], box_2[1] + dir[1]),
                    )
                )
        else:
            boxes += to_move

        # print(f"\tboxes: {boxes}")
        # print(f"\tloc: {loc}")

    tot = 0
    for (i, j), _ in boxes:
        tot += i * 100 + j
    return tot


moves, start, walls, boxes = parse(puzzle)
print("part 1: ", part_1(moves, start, walls, boxes))
moves, start, walls, boxes = parse_2(puzzle)
print("part 2: ", part_2(moves, start, walls, boxes))
