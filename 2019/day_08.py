from aocd import get_data

YEAR, DAY = 2019, 8
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "123456789012"
TEST_2 = "0222112222120000"


def part_1(data: str, l: int, h: int):

    layer_len = l * h
    layer_cnt = len(data) // layer_len
    least_0 = 100

    for layer_ind in range(layer_cnt):
        layer = data[layer_ind * layer_len : (layer_ind + 1) * layer_len]
        if layer.count("0") < least_0:
            least_0 = layer.count("0")
            least_layer = layer
    return least_layer.count("1") * least_layer.count("2")


def part_2(data: str, l: int, h: int):
    layer_len = l * h
    layer_cnt = len(data) // layer_len

    out = ""
    for pos in range(layer_len):
        for layer_ind in range(layer_cnt):
            layer = data[layer_ind * layer_len : (layer_ind + 1) * layer_len]

            if layer[pos] in "01":
                out += layer[pos]
                break

    for layer_ind in range(h):
        layer = out[layer_ind * l : (layer_ind + 1) * l]
        print("\t", layer.replace("0", " ").replace("1", "#"))


print("Part 1: ", part_1(puzzle, 25, 6))
print("Part 2: ")
part_2(puzzle, 25, 6)
