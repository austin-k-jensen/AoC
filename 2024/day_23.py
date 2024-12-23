import networkx as nx
from aocd import get_data
from utils import timing

YEAR, DAY = 2024, 23
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""


def create_graph(data: str):
    G = nx.Graph()
    for edge in data.strip().splitlines():
        n1, n2 = edge.split("-")
        G.add_edge(n1, n2)

    return G


@timing
def both(graph: nx.graph):
    best = 0
    threes = []
    for clq in nx.enumerate_all_cliques(graph):
        if len(clq) == 3:
            if clq[0][0] == "t" or clq[1][0] == "t" or clq[2][0] == "t":
                threes.append(clq)
        if len(clq) > best:
            out = clq
            best = len(clq)

    return len(threes), ",".join(sorted(out))


graph = create_graph(puzzle)
part_1, part_2 = both(graph)
print("part 1: ", part_1)
print("part 2: ", part_2)
