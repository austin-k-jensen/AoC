from aocd import get_data

YEAR, DAY = 2024, 5
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def parse(data):
    _rules, _updates = data.strip().split("\n\n")

    rules = {}
    for row in _rules.splitlines():
        i, j = [int(x) for x in row.split("|")]
        if i in rules:
            rules[i].append(j)
        else:
            rules[i] = [j]

    updates = []
    for row in _updates.splitlines():
        dict = {}
        for i, x in enumerate(row.split(",")):
            dict[int(x)] = i
        updates.append(dict)

    return rules, updates


def is_valid(rules, update):
    valid = True
    for page in update:
        if page in rules:
            for rule in rules[page]:
                if rule in update:
                    if update[page] > update[rule]:
                        valid = False
                        break
    return valid


def part_1(rules, updates):

    invalid = []
    tot = 0
    for update in updates:
        valid = is_valid(rules, update)
        if valid:
            tot += list(update.keys())[
                list(update.values()).index(max(update.values()) / 2)
            ]
        else:
            invalid.append(update)

    return tot, invalid


def fix_update(rules, update):
    for page in update:
        if page in rules:
            for rule in rules[page]:
                if rule in update:
                    if update[page] > update[rule]:
                        new_page = update[rule]
                        new_rule = update[page]
                        update[page] = new_page
                        update[rule] = new_rule
    return update


def part_2(rules, updates):

    tot = 0
    for update in updates:
        valid = is_valid(rules, update)
        while not valid:
            update = fix_update(rules, update)
            valid = is_valid(rules, update)

        tot += list(update.keys())[
            list(update.values()).index(max(update.values()) / 2)
        ]
    return tot


rules, updates = parse(puzzle)
part_1_ans, invalid = part_1(rules, updates)
print("part 1: ", part_1_ans)
print("part 2: ", part_2(rules, invalid))
