import re
from itertools import combinations
from scipy.optimize import linprog
from aocd import get_data

YEAR, DAY = 2025, 10
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""


def parse(data: str):
    machines = []
    for machine in data.strip().splitlines():

        state = tuple(map(int, re.search(r"[\.#]+", machine).group().replace(".", "0").replace("#", "1")))

        buttons = []
        for i in re.findall(r"\(([\d,]+)", machine):
            buttons.append(tuple(map(int, i.split(","))))

        jolts = tuple(map(int, re.search(r"{([\d,]+)", machine).group()[1:].split(",")))

        machines.append([state, buttons, jolts])

    return machines


def part_1_pressing(buttons: list, end: tuple):
    for n, _ in enumerate(buttons):
        for comb in combinations(buttons, n + 1):
            state = (0,) * len(end)
            for button in comb:
                next_state = ()
                for i, _ in enumerate(state):
                    if i in button:
                        next_state += (int(not (state[i])),)
                    else:
                        next_state += (state[i],)

                state = next_state
                if state == end:
                    return len(comb)


def part_1(machines: list):
    count = 0
    for machine in machines:
        end = machine[0]
        buttons = machine[1]

        count += part_1_pressing(buttons, end)
    return count


def part_2(machines: list):
    tot = 0
    for machine in machines:
        buttons = machine[1]
        jolts = machine[2]

        c = [1] * len(buttons)

        A_eq = []
        for i, _ in enumerate(jolts):
            row = []
            for button in buttons:
                if i in button:
                    row.append(1)
                else:
                    row.append(0)
            A_eq.append(row)

        tot += linprog(c=c, A_eq=A_eq, b_eq=jolts, integrality=1).fun

    return int(tot)


machines = parse(puzzle)
print("part 1: ", part_1(machines))
print("part 2: ", part_2(machines))
