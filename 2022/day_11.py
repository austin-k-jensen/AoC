import re
from numexpr import evaluate
from math import lcm
from aocd import get_data

YEAR, DAY = 2022, 11
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
  If true: throw to monkey 2
  If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
  If true: throw to monkey 2
  If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
  If true: throw to monkey 1
  If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
  If true: throw to monkey 0
  If false: throw to monkey 1
"""


def part_1(data):
    monkeys = data.strip().split("\n\n")

    monkey_dict = {}
    for i, monkey in enumerate(monkeys):
        monkey_dict[i] = {}

        monkey_dict[i]["items"] = [
            int(item)
            for item in re.findall(r"items: (\d+(?:[, ]*\d+)+)", monkey)[0].split(", ")
        ]

        monkey_dict[i]["operation"] = re.findall(r"new = (.+)", monkey)[0]
        monkey_dict[i]["test"] = int(re.findall(r"by (\d+)", monkey)[0])
        monkey_dict[i]["true"] = int(re.findall(r"true: .+(\d+)", monkey)[0])
        monkey_dict[i]["false"] = int(re.findall(r"false: .+(\d+)", monkey)[0])
        monkey_dict[i]["count"] = 0

    for i in range(20):
        for monkey in monkey_dict:
            for i, item in enumerate(list(monkey_dict[monkey]["items"])):
                operation = monkey_dict[monkey]["operation"].replace("old", str(item))
                worry = evaluate(operation) // 3

                if worry % monkey_dict[monkey]["test"] == 0:
                    toss = monkey_dict[monkey]["true"]
                else:
                    toss = monkey_dict[monkey]["false"]
                monkey_dict[monkey]["items"].remove(item)
                monkey_dict[monkey]["count"] += 1
                monkey_dict[toss]["items"].append(worry)

    cnts = [monkey_dict[monkey]["count"] for monkey in monkey_dict]
    cnts_srt = sorted(cnts, reverse=True)
    print("part 1: ", cnts_srt[0] * cnts_srt[1])


def part_2(data):
    monkeys = data.strip().split("\n\n")

    monkey_dict = {}
    for i, monkey in enumerate(monkeys):
        monkey_dict[i] = {}

        monkey_dict[i]["items"] = [
            int(item)
            for item in re.findall(r"items: (\d+(?:[, ]*\d+)+)", monkey)[0].split(", ")
        ]

        monkey_dict[i]["operation"] = re.findall(r"new = (.+)", monkey)[0]
        monkey_dict[i]["test"] = int(re.findall(r"by (\d+)", monkey)[0])
        monkey_dict[i]["true"] = int(re.findall(r"true: .+(\d+)", monkey)[0])
        monkey_dict[i]["false"] = int(re.findall(r"false: .+(\d+)", monkey)[0])
        monkey_dict[i]["count"] = 0

    tests = [monkey_dict[monkey]["test"] for monkey in monkey_dict]
    worry_reduc = lcm(*tests)

    for i in range(10000):
        for monkey in monkey_dict:
            for i, item in enumerate(list(monkey_dict[monkey]["items"])):
                operation = monkey_dict[monkey]["operation"].replace("old", str(item))
                worry = evaluate(operation) % worry_reduc

                if worry % monkey_dict[monkey]["test"] == 0:
                    toss = monkey_dict[monkey]["true"]
                else:
                    toss = monkey_dict[monkey]["false"]
                monkey_dict[monkey]["items"].remove(item)
                monkey_dict[monkey]["count"] += 1
                monkey_dict[toss]["items"].append(worry)

    cnts = [monkey_dict[monkey]["count"] for monkey in monkey_dict]
    cnts_srt = sorted(cnts, reverse=True)
    print("part 2: ", cnts_srt[0] * cnts_srt[1])


part_1(puzzle)
part_2(puzzle)
