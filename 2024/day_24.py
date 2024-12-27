from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 24
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
"""

TEST_2 = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""

TEST_3 = """
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00
"""


def parse(data: str):
    starts, block = data.strip().split("\n\n")

    wires = {}
    for start in starts.splitlines():
        wires[start[:3]] = int(start[5])

    gates = {}
    gate_deps = {}
    for gate in block.splitlines():
        wire_1, opp, wire_2, _, wire_3 = gate.split()
        gates[wire_3] = ((wire_1, wire_2), opp)

        gate_deps[wire_3] = [wire_1, wire_2]

    for gate in gate_deps:
        # print(gate, gate_deps[gate])
        check = gate_deps[gate].copy()

        depth = 0
        while check and depth < 10:
            new = check.pop()
            if new in gate_deps:
                # print("\t", gate_deps[new])
                for to_add in gate_deps[new]:
                    if not to_add in gate_deps[gate]:
                        check.append(to_add)
                        gate_deps[gate].append(to_add)
            depth += 1

    # print(gates)

    return wires, gates, gate_deps


def run_program(wires: dict, gates: dict):

    to_process = list(gates.keys())
    # print(to_process)

    while to_process:
        gate = to_process.pop(0)
        (wire_1, wire_2), opp = gates[gate]

        if wire_1 in wires and wire_2 in wires:
            if opp == "AND":
                wires[gate] = wires[wire_1] and wires[wire_2]
            if opp == "OR":
                wires[gate] = wires[wire_1] or wires[wire_2]
            if opp == "XOR":
                wires[gate] = wires[wire_1] ^ wires[wire_2]

        else:
            to_process.append(gate)

    return wires


@timing
def part_1(wires: dict):
    out_wires = []
    for wire, value in wires.items():
        if wire[0] == "z":
            out_wires.append((wire, value))

    bin_out = 0
    for i, (wire, value) in enumerate(sorted(out_wires)):
        bin_out += value * 10**i

    return int(str(bin_out), 2)


def part_2(wires: dict, gates: list):

    safe_gates = set()

    # Found by manually parsing the input in 2024/day_24.txt
    gates["hdt"], gates["z05"] = gates["z05"], gates["hdt"]
    gates["gbf"], gates["z09"] = gates["z09"], gates["gbf"]
    gates["mht"], gates["jgt"] = gates["jgt"], gates["mht"]
    gates["nbf"], gates["z30"] = gates["z30"], gates["nbf"]

    swaps = ["hdt", "z05", "gbf", "z09", "mht", "jgt", "nbf", "z30"]

    for i in range(45):
        test_wires = {}
        for j in range(45):
            if j <= i:
                test_wires[f"x{j:02}"] = 1
                test_wires[f"y{j:02}"] = 1
            else:
                test_wires[f"x{j:02}"] = 0
                test_wires[f"y{j:02}"] = 0

        # print(test_wires)

        test_wires = run_program(test_wires, gates)

        # print(test_wires)

        x_wires = []
        y_wires = []
        z_wires = []
        for wire, value in test_wires.items():
            if wire[0] == "x":
                x_wires.append((wire, value))
            if wire[0] == "y":
                y_wires.append((wire, value))
            if wire[0] == "z":
                z_wires.append((wire, value))

        x_bin = 0
        for n, (wire, value) in enumerate(sorted(x_wires)):
            x_bin += value * 10**n
        y_bin = 0
        for n, (wire, value) in enumerate(sorted(y_wires)):
            y_bin += value * 10**n
        z_bin = 0
        for n, (wire, value) in enumerate(sorted(z_wires)):
            z_bin += value * 10**n

        x_val = int(str(x_bin), 2)
        y_val = int(str(y_bin), 2)
        z_val = int(str(z_bin), 2)

        # print(f"z{i:02}: {x_val} + {y_val} = {z_val}: {x_val+y_val==z_val}")

        if x_val + y_val == z_val:
            # print(f"z{i:02}")
            safe_gates.update(gate_deps[f"z{i:02}"])
        else:
            # print(f"z{i:02}")
            to_check = []
            for gate in gate_deps[f"z{i:02}"]:
                if gate not in safe_gates:
                    to_check.append(gate)
            # print(to_check)
    # print(safe_gates)

    return ",".join(sorted(swaps))


wires, gates, gate_deps = parse(puzzle)
print("part 1: ", part_1(run_program(wires, gates)))
print("part 2: ", part_2(wires, gates))
