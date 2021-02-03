import operator

def call_func(g):
    degrees = {}
    edges = g.edges()
    for v in g.vertices():
        degrees[v] = g.degree(v)

    return _func(g, degrees, edges)


def _func(g, degrees, edges):
    solution = []
    while len(edges) > 0:
        selected_vertex = max(degrees.items(), key=operator.itemgetter(1))[0]
        _delete_incident_edges(g, degrees, edges, selected_vertex)
        solution.append(selected_vertex)

    return solution


def _delete_incident_edges(g, degrees, edges, vertex):
    for e in g.incident_edges(vertex):
        if e in edges:
            edges.remove(e)
            u,v = e.endpoints()
            degrees[u] -= 1
            degrees[v] -= 1
