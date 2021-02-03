import random
from graph.graph import Graph

def generate_graph(number=100, directed=False):
    g = Graph(directed)
    vertexes = _generate_vertexes(g, number)
    for i in range(number):
        start = 0 if directed else i
        for j in range(start, number):
            if (i != j and bool(random.getrandbits(1))):
                g.insert_edge(vertexes[i], vertexes[j])
    return g


def _generate_vertexes(g, number):
    vertices = []
    for i in range(number):
        vertices.append(g.insert_vertex(i))
    return vertices
