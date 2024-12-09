from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 9
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "2333133121414131402"
TEST_2 = "12345"


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
        # print(file, space)
        disk += file_blocks[index : index + file]
        # print(disk)
        index += file

        for i in range(space):
            if len(disk) < num_files:
                disk.append(file_blocks.pop())
            else:
                break

        # print(disk)

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
    for r_file, r_space in zip(reversed(files), reversed(spaces)):
        print(file_blocks)
        print(f"Checking file {r_file}: {file_blocks[r_index-r_file+1:r_index+1]}")
        f_index = 0
        r_index -= r_file

        for i, (f_file, f_space) in enumerate(zip(files, spaces)):

            f_index += f_file
            print(f"Checking space {f_space}: {file_blocks[f_index:f_index + f_space]}")

            if r_file <= f_space:
                print("\tFile fits")
                spaces[i] = f_space - r_file
                for _ in range(r_file):
                    # print(f_index)
                    file_blocks[f_index] = file_blocks[r_index]
                    file_blocks[r_index] = "."
                    f_index += 1
                    r_index -= 1

                files[i] = f_file + r_file
                spaces[i] = f_space - r_file
                break
            else:
                f_index += f_space

                # print(r_index)
            # print(f"No space found")
        r_index -= r_space


files, spaces = parse(TEST_1)
# print("part 1: ", part_1(files, spaces))
part_2(files, spaces)
