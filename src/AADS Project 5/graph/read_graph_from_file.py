from graph.graph import Graph

def read_graph_from_file(filename):

    with open(filename) as f:
        array = []
        for line in f: # read rest of lines
            array.append([int(x) for x in line.split()])

    vertex = []
    g = Graph()
    for i in range(len(array)):
        vertex.append(g.insert_vertex(i+1))

    for i in range(len(array)):
        u = array[i][0]
        v = array[i][1]
        g.insert_edge(vertex[u], vertex[v])

    return g
