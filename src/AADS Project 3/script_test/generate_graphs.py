import random
from graphs.extendend_graph import ExtendedGraph

def generate_graph(number=100, directed=False):
    g = ExtendedGraph(directed)
    vertexes = _generate_vertexes(g, number)
    for i in range(number):
        start = 0 if directed else i
        for j in range(start, number):
            if (i != j and random.getrandbits(1)):
                g.insert_edge(vertexes[i], vertexes[j])
    return g


def _generate_vertexes(g, number):
    vertexes = []
    for i in range(number):
        vertexes.append(g.insert_vertex(i))
    return vertexes
