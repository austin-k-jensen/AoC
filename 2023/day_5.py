import re
from datetime import datetime
from aocd import get_data
from aocd import submit

YEAR, DAY = 2023, 5
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def parse(data):
    scriptstart = datetime.now()

    sections = data.split("\n\n")

    seeds = [int(seed) for seed in re.findall(r"(\d+)", sections[0])]

    seed_to_soil = [
        [(int(soil), int(soil) + int(num) - 1), (int(seed), int(seed) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[1])
    ]
    seed_to_soil.sort()
    soil_to_fertilizer = [
        [(int(soil), int(soil) + int(num) - 1), (int(seed), int(seed) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[2])
    ]
    soil_to_fertilizer.sort()
    fertilizer_to_water = [
        [(int(soil), int(soil) + int(num) - 1), (int(seed), int(seed) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[3])
    ]
    fertilizer_to_water.sort()
    water_to_light = [
        [(int(soil), int(soil) + int(num) - 1), (int(seed), int(seed) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[4])
    ]
    water_to_light.sort()
    light_to_temperature = [
        [(int(soil), int(soil) + int(num) - 1), (int(seed), int(seed) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[5])
    ]
    light_to_temperature.sort()
    temperature_to_humidity = [
        [(int(soil), int(soil) + int(num) - 1), (int(seed), int(seed) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[6])
    ]
    temperature_to_humidity.sort()
    humidity_to_location = [
        [(int(soil), int(soil) + int(num) - 1), (int(seed), int(seed) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[7])
    ]
    humidity_to_location.sort()

    mapping = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location,
    ]

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"{scriptend}: Parsing complete in seconds: {elapsed_sec}")

    return seeds, mapping


def part_1(seeds, mapping):
    scriptstart = datetime.now()
    locs = []
    for seed in seeds:
        for step in mapping:
            for pair in step:
                if pair[1][0] <= seed <= pair[1][1]:
                    seed = pair[0][0] + seed - pair[1][0]
                    break
                else:
                    pass
        locs.append(seed)

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"\n{scriptend}: Parsing complete in seconds: {elapsed_sec}")
    print("part 1: ", min(locs))


def part_2(seeds, mapping):
    scriptstart = datetime.now()
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append([seeds[i], seeds[i] + seeds[i + 1] - 1])

    found = False
    loc = 0

    while not found:
        test_loc = loc
        for step in reversed(mapping):
            for pair in step:
                if pair[0][0] <= test_loc <= pair[0][1]:
                    test_loc = pair[1][0] + test_loc - pair[0][0]
                    break

        for seed_range in seed_ranges:
            if seed_range[0] <= test_loc <= seed_range[1]:
                found = True

                scriptend = datetime.now()
                elapsed = scriptend - scriptstart
                elapsed_sec = elapsed.seconds
                print(f"\n{scriptend}: Part 2 complete in seconds: {elapsed_sec}")
                print("part 2: ", loc)

        loc += 1


def part_2_new(seeds, mapping):
    scriptstart = datetime.now()
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append([seeds[i], seeds[i] + seeds[i + 1] - 1])
    seed_ranges.sort()
    print(seed_ranges)

    for step in mapping[0:2]:
        print(step)
        new_ranges = []
        for seed_range in seed_ranges:
            for pair in step:
                print(pair, seed_range)
                if seed_range[1] < pair[0][0]:
                    pass
                elif seed_range[0] >= pair[0][0] and seed_range[1] <= pair[0][1]:
                    new_ranges.append(
                        [
                            pair[1][0] + seed_range[0] - pair[0][0],
                            pair[1][1] + seed_range[1] - pair[0][1],
                        ]
                    )
                elif seed_range[0] > pair[0][1]:
                    new_ranges.append(seed_range)
                    # seed_ranges.remove(seed_range)
            seed_ranges = new_ranges
        print(seed_ranges)

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"\n{scriptend}: Part 2 complete in seconds: {elapsed_sec}")
    # print("part 2: ", loc)


seeds, mapping = parse(TEST_1)
# part_1(seeds, mapping)
# part_2(seeds, mapping)
part_2_new(seeds, mapping)
