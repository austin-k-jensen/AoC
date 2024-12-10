from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 9
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "2333133121414131402"
TEST_2 = "12345"
TEST_3 = "14113"


@timing
def parse(data):
    numbers = data.strip().split()
    numbers = [int(x) for x in numbers[0]]
    files = numbers[::2]
    spaces = numbers[1::2]
    return files, spaces


@timing
def part_1(files, spaces):

    file_blocks = []
    for i, file in enumerate(files):
        file_blocks += [i] * file

    disk = []
    num_files = len(file_blocks)
    index = 0
    for file, space in zip(files, spaces):
        disk += file_blocks[index : index + file]
        index += file

        for i in range(space):
            if len(disk) < num_files:
                disk.append(file_blocks.pop())
            else:
                break

    tot = 0
    for i, file in enumerate(disk):
        tot += i * file
    return tot


@timing
def part_2(files, spaces):
    file_blocks = []
    for i, file in enumerate(files):
        file_blocks += [i] * file
        if i < len(spaces):
            file_blocks += ["."] * spaces[i]

    r_index = len(file_blocks) - 1
    check_id = len(files) - 1

    for r_file, r_space in zip(reversed(files), reversed(spaces)):

        f_index = 0
        fit = False

        files, spaces = [], []
        comp = 0
        cnt = 0
        for block in file_blocks:
            if block == comp:
                cnt += 1
            else:
                if comp == ".":
                    spaces.append(cnt)
                else:
                    if block != ".":
                        spaces.append(0)
                    files.append(cnt)
                if block == check_id:
                    break
                cnt = 1
            comp = block
        check_id -= 1

        for f_file, f_space in zip(files, spaces):

            f_index += f_file

            if r_file <= f_space:
                for _ in range(r_file):
                    file_blocks[f_index] = file_blocks[r_index]
                    file_blocks[r_index] = "."
                    f_index += 1
                    r_index -= 1

                r_index -= r_space
                fit = True
                break
            else:
                f_index += f_space

        if not fit:
            r_index -= r_file + r_space

    tot = 0
    for i, file in enumerate(file_blocks):
        if file == ".":
            pass
        else:
            tot += i * file
    return tot


files, spaces = parse(puzzle)
print("part 1: ", part_1(files, spaces))
print("part 2: ", part_2(files, spaces))
