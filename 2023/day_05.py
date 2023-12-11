import re
from datetime import datetime
from aocd import get_data

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

    mapping = []
    for section in sections[1:]:
        mp = [
            [
                [int(start), int(start) + int(num)],
                [int(target), int(target) + int(num)],
            ]
            for target, start, num in re.findall(r"(\d+) (\d+) (\d+)", section)
        ]
        mp.sort()
        mapping.append(mp)

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
                if pair[0][0] <= seed <= pair[0][1]:
                    seed = pair[1][0] + seed - pair[0][0]
                    break
                else:
                    pass
        locs.append(seed)

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"\n{scriptend}: Part 1 complete in seconds: {elapsed_sec}")
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
    locations = []
    for i in range(0, len(seeds), 2):
        seed_range = [[seeds[i], seeds[i] + seeds[i + 1]]]
        new_ranges = []

        for step in mapping:
            while seed_range:
                start_range, end_range = seed_range.pop()
                for pair in step:
                    if pair[0][1] <= start_range or end_range <= pair[0][0]:
                        continue
                    if start_range < pair[0][0]:
                        seed_range.append([start_range, pair[0][0]])
                        start_range = pair[0][0]
                    if pair[0][1] < end_range:
                        seed_range.append([pair[0][1], end_range])
                        end_range = pair[0][1]
                    new_ranges.append(
                        [
                            pair[1][0] + start_range - pair[0][0],
                            pair[1][1] + end_range - pair[0][1],
                        ]
                    )
                    break
                else:
                    new_ranges.append([start_range, end_range])
            seed_range = new_ranges
            new_ranges = []
        locations += seed_range
    min_loc = min(loc[0] for loc in locations)

    scriptend = datetime.now()
    elapsed = scriptend - scriptstart
    elapsed_sec = elapsed.seconds
    print(f"\n{scriptend}: Part 2 complete in seconds: {elapsed_sec}")
    print("part 2: ", min_loc)


seeds, mapping = parse(puzzle)
part_1(seeds, mapping)
# part_2(seeds, mapping)
part_2_new(seeds, mapping)
