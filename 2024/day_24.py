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

    gates = []
    for gate in block.splitlines():
        wire_1, opp, wire_2, _, wire_3 = gate.split()
        gates.append(((wire_1, wire_2), opp, wire_3))

    return wires, gates


@timing
def part_1(wires: dict, gates: list):

    to_process = gates

    while to_process:
        gate = to_process.pop(0)
        (wire_1, wire_2), opp, out_wire = gate

        if wire_1 in wires and wire_2 in wires:
            if opp == "AND":
                wires[out_wire] = wires[wire_1] and wires[wire_2]
            if opp == "OR":
                wires[out_wire] = wires[wire_1] or wires[wire_2]
            if opp == "XOR":
                wires[out_wire] = wires[wire_1] ^ wires[wire_2]

        else:
            to_process.append(gate)

    out_wires = []
    for wire, value in wires.items():
        if wire[0] == "z":
            out_wires.append((wire, value))

    bin_out = 0
    for i, (wire, value) in enumerate(sorted(out_wires)):
        bin_out += value * 10**i

    return int(str(bin_out), 2)


# def part_2(wires: dict, gates: list)
#         out_wires = []
#     for wire, value in wires.items():
#         if wire[0] == "z":
#             out_wires.append((wire, value))


wires, gates = parse(puzzle)
print(part_1(wires, gates))
wires = {
    "x00": 1,
    "x01": 0,
    "x02": 0,
    "x03": 0,
    "x04": 0,
    "x05": 0,
    "x06": 0,
    "x07": 0,
    "x08": 0,
    "x09": 0,
    "x10": 0,
    "x11": 0,
    "x12": 0,
    "x13": 0,
    "x14": 0,
    "x15": 0,
    "x16": 0,
    "x17": 0,
    "x18": 0,
    "x19": 0,
    "x20": 0,
    "x21": 0,
    "x22": 0,
    "x23": 0,
    "x24": 0,
    "x25": 0,
    "x26": 0,
    "x27": 0,
    "x28": 0,
    "x29": 0,
    "x30": 0,
    "x31": 0,
    "x32": 0,
    "x33": 0,
    "x34": 0,
    "x35": 0,
    "x36": 0,
    "x37": 0,
    "x38": 0,
    "x39": 0,
    "x40": 0,
    "x41": 0,
    "x42": 0,
    "x43": 0,
    "x44": 0,
    "y00": 1,
    "y01": 0,
    "y02": 0,
    "y03": 0,
    "y04": 0,
    "y05": 0,
    "y06": 0,
    "y07": 0,
    "y08": 0,
    "y09": 0,
    "y10": 0,
    "y11": 0,
    "y12": 0,
    "y13": 0,
    "y14": 0,
    "y15": 0,
    "y16": 0,
    "y17": 0,
    "y18": 0,
    "y19": 0,
    "y20": 0,
    "y21": 0,
    "y22": 0,
    "y23": 0,
    "y24": 0,
    "y25": 0,
    "y26": 0,
    "y27": 0,
    "y28": 0,
    "y29": 0,
    "y30": 0,
    "y31": 0,
    "y32": 0,
    "y33": 0,
    "y34": 0,
    "y35": 0,
    "y36": 0,
    "y37": 0,
    "y38": 0,
    "y39": 0,
    "y40": 0,
    "y41": 0,
    "y42": 0,
    "y43": 0,
    "y44": 0,
}
