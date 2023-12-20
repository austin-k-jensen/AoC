import re
from numexpr import evaluate
from collections import defaultdict
from aocd import get_data

YEAR, DAY = 2023, 19
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""


def parse(data):
    workflows, items = data.strip().split("\n\n")

    workflow_dict = {}
    for workflow in workflows.splitlines():
        nm, steps = workflow.split("{")
        steps = [step.split(":") for step in steps.split(",")]
        steps[-1][0] = steps[-1][0][:-1]
        workflow_dict[nm] = steps

    item_dict = {}
    for i, item in enumerate(items.splitlines()):
        item_dict[i] = {}
        atrs = re.findall(r"(\d+)", item)
        item_dict[i]["state"] = "in"
        (
            item_dict[i]["x"],
            item_dict[i]["m"],
            item_dict[i]["a"],
            item_dict[i]["s"],
        ) = atrs
    return workflow_dict, item_dict


def part_1(workflow_dict, item_dict):
    total = 0
    for _, item in item_dict.items():
        while item["state"] not in "AR":
            for check in workflow_dict[item["state"]]:
                if len(check) == 1:
                    item["state"] = check[0]
                else:
                    if evaluate(item[check[0][0]] + check[0][1:]):
                        item["state"] = check[1]
                        break

        if item["state"] == "A":
            total += int(item["x"]) + int(item["m"]) + int(item["a"]) + int(item["s"])

    print("part 1: ", total)


def split_ranges(step, range_dict, workflow_dict):
    remain = range_dict[step]

    for check in workflow_dict[step]:
        if len(check) == 1:
            range_dict[check[0]] += remain
            if check[0] in "AR":
                pass
            else:
                split_ranges(check[0], range_dict, workflow_dict)
        else:
            match check[0][:2]:
                case "x<":
                    range_dict[check[1]] += [
                        [remain[0][0], int(check[0][2:])],
                        remain[1],
                        remain[2],
                        remain[3],
                    ]
                    remain = [
                        [int(check[0][2:]), remain[0][1]],
                        remain[1],
                        remain[2],
                        remain[3],
                    ]
                case "x>":
                    range_dict[check[1]] += [
                        [int(check[0][2:]) + 1, remain[0][1]],
                        remain[1],
                        remain[2],
                        remain[3],
                    ]
                    remain = [
                        [remain[0][0], int(check[0][2:]) + 1],
                        remain[1],
                        remain[2],
                        remain[3],
                    ]
                case "m<":
                    range_dict[check[1]] += [
                        remain[0],
                        [remain[1][0], int(check[0][2:])],
                        remain[2],
                        remain[3],
                    ]
                    remain = [
                        remain[0],
                        [int(check[0][2:]), remain[1][1]],
                        remain[2],
                        remain[3],
                    ]
                case "m>":
                    range_dict[check[1]] += [
                        remain[0],
                        [int(check[0][2:]) + 1, remain[1][1]],
                        remain[2],
                        remain[3],
                    ]
                    remain = [
                        remain[0],
                        [remain[1][0], int(check[0][2:]) + 1],
                        remain[2],
                        remain[3],
                    ]
                case "a<":
                    range_dict[check[1]] += [
                        remain[0],
                        remain[1],
                        [remain[2][0], int(check[0][2:])],
                        remain[3],
                    ]
                    remain = [
                        remain[0],
                        remain[1],
                        [int(check[0][2:]), remain[2][1]],
                        remain[3],
                    ]
                case "a>":
                    range_dict[check[1]] += [
                        remain[0],
                        remain[1],
                        [int(check[0][2:]) + 1, remain[2][1]],
                        remain[3],
                    ]
                    remain = [
                        remain[0],
                        remain[1],
                        [remain[2][0], int(check[0][2:]) + 1],
                        remain[3],
                    ]
                case "s<":
                    range_dict[check[1]] += [
                        remain[0],
                        remain[1],
                        remain[2],
                        [remain[3][0], int(check[0][2:])],
                    ]
                    remain = [
                        remain[0],
                        remain[1],
                        remain[2],
                        [int(check[0][2:]), remain[3][1]],
                    ]
                case "s>":
                    range_dict[check[1]] += [
                        remain[0],
                        remain[1],
                        remain[2],
                        [int(check[0][2:]) + 1, remain[3][1]],
                    ]
                    remain = [
                        remain[0],
                        remain[1],
                        remain[2],
                        [remain[3][0], int(check[0][2:]) + 1],
                    ]
            if check[1] in "AR":
                pass
            else:
                split_ranges(check[1], range_dict, workflow_dict)
    return range_dict


def part_2(workflow_dict):
    range_dict = defaultdict(list)
    range_dict["in"] = [[1, 4001], [1, 4001], [1, 4001], [1, 4001]]

    range_dict = split_ranges("in", range_dict, workflow_dict)

    accepted = 0
    while range_dict["A"]:
        add = 1
        for _ in range(4):
            pair = range_dict["A"].pop()
            mult = pair[1] - pair[0]
            add *= mult
        accepted += add
    print("part 2: ", accepted)


workflow_dict, item_dict = parse(puzzle)
part_1(workflow_dict, item_dict)
part_2(workflow_dict)
