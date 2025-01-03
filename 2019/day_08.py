from aocd import get_data

YEAR, DAY = 2019, 8
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = "123456789012"


def part_1(data: str):

    # layer_len = 2 * 3
    layer_len = 25 * 6
    layer_cnt = len(data) // layer_len
    least_0 = 100

    for layer_ind in range(layer_cnt):
        layer = data[layer_ind * layer_len : (layer_ind + 1) * layer_len]
        if layer.count("0") < least_0:
            least_0 = layer.count("0")
            least_layer = layer
    print(least_layer.count("1") * least_layer.count("2"))


part_1(puzzle)
