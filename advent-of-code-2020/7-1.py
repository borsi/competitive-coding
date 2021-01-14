import networkx as nx
from matplotlib import pyplot as plt
import re
from matplotlib.pyplot import figure
figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')


file = open("7-intest.txt", "r")
lines = file.read().splitlines()


def parse_graph_structure(line, graph):
    root = line.split('contain')[0]
    directions = line.split('contain')[1].split(',')
    regex = re.compile('[a-z]+ [a-z]+')
    bagno = re.compile('\d')
    root = regex.findall(root)
    for d in directions:
        e = regex.findall(d)
        n = bagno.findall(d)
        if (bool(n)):
            w = int(n[0])
        else:
            w = 0
        graph.add_edge(root[0], e[0], weight=w)
        # print(root, e, n)
        # edges.append((root[0], e[0], weight=n))
    # return edges


graph = nx.DiGraph()
for l in lines:
    # print(parse_graph_structure(l))
    # graph.add_edges_from(parse_graph_structure(l))
    parse_graph_structure(l, graph)


def collect_predecessors(startnode, graph):
    nodes = set()

    def find_all_predecessors(node, g):
        nodes.add(node)
        preds = g.predecessors(node)
        # print('%s -> %s' % (node, preds))
        # print(node)
        if (g.in_edges(node)):
            for pred in preds:
                # print(pred)
                find_all_predecessors(pred, g)
    find_all_predecessors(startnode, graph)
    return nodes


def calculate_bags_needed(startnode, graph):
    bags = 1

    def find_all_successors(node, g, bags):
        successors = g.successors(node)
        if (g.out_edges(node)):
            for succ in successors:
                # print(node, succ, g.get_edge_data(node, succ))
                w = g.get_edge_data(node, succ)['weight']
                find_all_successors(succ, g, bags * w)
        else:
            return 0
    find_all_successors(startnode, graph, bags)
    return bags


""" FIRST PART

oneshinybag = len(collect_predecessors('shiny gold', graph)) - 1
print(oneshinybag)

"""

""" SECOND PART """
print(calculate_bags_needed('shiny gold', graph))

""" FUN PRINT
# plt.tight_layout()
nx.draw_networkx(graph, arrows=True)
plt.savefig("g1.png", format="PNG")
plt.clf()
"""
