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


def parse(data: str):
    graph = {}
    for edge in data.strip().splitlines():
        n1, n2 = edge.split("-")
        if n1 in graph:
            graph[n1].append(n2)
        else:
            graph[n1] = [n2]
        if n2 in graph:
            graph[n2].append(n1)
        else:
            graph[n2] = [n1]
    return graph


def create_graph(data: str):
    G = nx.Graph()
    for edge in data.strip().splitlines():
        n1, n2 = edge.split("-")
        G.add_edge(n1, n2)

    return G


@timing
def part_1(graph: dict):
    groups = set()
    for node1, nodes1 in graph.items():
        # print(node1, nodes1)
        for node2 in nodes1:
            # print("\t", node2, graph[node2])
            for node3 in graph[node2]:
                # print("\t\t", node3, graph[node3])
                if node1 in graph[node3] and node2 in graph[node3]:
                    # print("\t\t\tSet found:", node1, node2, node3)
                    if node1[0] == "t":
                        groups.add(frozenset([node1, node2, node3]))
    print(len(groups))


def part_2(graph: nx.graph):

    best = 0
    for clq in nx.clique.find_cliques(graph):
        if len(clq) > best:
            out = clq
            best = len(clq)
    return ",".join(sorted(out))


# graph = parse(puzzle)
# part_1(graph)
graph = create_graph(puzzle)
print(part_2(graph))
