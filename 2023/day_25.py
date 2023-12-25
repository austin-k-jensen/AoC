import networkx
from aocd import get_data

YEAR, DAY = 2023, 25
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""


def part_1(data):
    G = networkx.Graph()

    for node in data.strip().splitlines():
        node, edges = node.split(": ")[0], node.split(": ")[1].split()
        for edge in edges:
            G.add_edge(node, edge)

    cuts = networkx.minimum_edge_cut(G)
    for node1, node2 in cuts:
        G.remove_edge(node1, node2)

    lens = [len(c) for c in networkx.connected_components(G)]
    print(lens[0] * lens[1])


part_1(puzzle)
