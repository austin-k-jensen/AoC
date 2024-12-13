import re
import numpy as np
from math import isclose
from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 13
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


@timing
def parse(data: str):
    systems = []

    for machine in data.strip().split("\n\n"):
        numbers = [int(x) for x in re.findall(r"\d+", machine)]

        systems.append(
            [
                np.array([[numbers[0], numbers[2]], [numbers[1], numbers[3]]]),
                np.array([numbers[4], numbers[5]]),
            ]
        )
    return systems


@timing
def both(systems, shift):

    tot = 0
    for system in systems:

        A, B = np.linalg.inv(system[0]).dot(system[1] + shift)
        int_A = int(round(A))
        int_B = int(round(B))

        if isclose(A, int_A, rel_tol=1e-13) and isclose(B, int_B, rel_tol=1e-13):
            tot += 3 * int_A + int_B
    return tot


systems = parse(puzzle)
print("part 1: ", both(systems, 0))
print("part 1: ", both(systems, 10000000000000))
