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
        [(int(seed), int(seed) + int(num) - 1), (int(soil), int(soil) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[1])
    ]
    soil_to_fertilizer = [
        [(int(seed), int(seed) + int(num) - 1), (int(soil), int(soil) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[2])
    ]
    fertilizer_to_water = [
        [(int(seed), int(seed) + int(num) - 1), (int(soil), int(soil) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[3])
    ]
    water_to_light = [
        [(int(seed), int(seed) + int(num) - 1), (int(soil), int(soil) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[4])
    ]
    light_to_temperature = [
        [(int(seed), int(seed) + int(num) - 1), (int(soil), int(soil) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[5])
    ]
    temperature_to_humidity = [
        [(int(seed), int(seed) + int(num) - 1), (int(soil), int(soil) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[6])
    ]
    humidity_to_location = [
        [(int(seed), int(seed) + int(num) - 1), (int(soil), int(soil) + int(num) - 1)]
        for seed, soil, num in re.findall(r"(\d+) (\d+) (\d+)", sections[7])
    ]

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


def part_1(seeds, mapping, sub: bool = False):
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


def part_2(seeds, mapping, sub: bool = False):
    scriptstart = datetime.now()
    min_loc = 999999999999999

    for i in range(0, len(seeds), 2):
        for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
            for step in mapping:
                for pair in step:
                    if pair[1][0] <= seed <= pair[1][1]:
                        seed = pair[0][0] + seed - pair[1][0]
                        break
                    else:
                        pass
            min_loc = seed if seed < min_loc else min_loc

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"\n{scriptend}: Part 2 complete in seconds: {elapsed_sec}")
    print("part 2: ", min_loc)


def part_2_rev(seeds, mapping, sub: bool = False):
    scriptstart = datetime.now()
    min_loc = 999999999999999

    for i in range(0, len(seeds), 2):
        for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
            for step in mapping:
                for pair in step:
                    if pair[1][0] <= seed <= pair[1][1]:
                        seed = pair[0][0] + seed - pair[1][0]
                        break
                    else:
                        pass
            min_loc = seed if seed < min_loc else min_loc

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"\n{scriptend}: Part 2 complete in seconds: {elapsed_sec}")
    print("part 2: ", min_loc)


seeds, mapping = parse(TEST_1)
part_1(seeds, mapping, sub=False)
# part_2(seeds, mapping, sub=False)
part_2_rev(seeds, mapping, sub=False)
