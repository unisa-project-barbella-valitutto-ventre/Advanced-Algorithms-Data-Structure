from graph.graph import Graph

def g1():
    g = Graph()
    vert = []
    for i in range(8):
        vert.append(g.insert_vertex(i))

    g.insert_edge(vert[0], vert[1])
    g.insert_edge(vert[0], vert[2])
    g.insert_edge(vert[1], vert[3])
    g.insert_edge(vert[1], vert[4])
    g.insert_edge(vert[4], vert[6])
    g.insert_edge(vert[4], vert[7])
    g.insert_edge(vert[2], vert[5])
    return g, vert[0]

def g2():
    g=Graph()
    vert=[]
    for i in range(12):
        vert.append(g.insert_vertex(i))

    g.insert_edge(vert[0], vert[1])
    g.insert_edge(vert[0], vert[2])
    g.insert_edge(vert[0], vert[3])
    g.insert_edge(vert[2], vert[4])
    g.insert_edge(vert[2], vert[5])
    g.insert_edge(vert[5], vert[6])
    g.insert_edge(vert[5], vert[7])
    g.insert_edge(vert[7], vert[8])
    g.insert_edge(vert[3], vert[9])
    g.insert_edge(vert[3], vert[10])
    g.insert_edge(vert[10], vert[11])

    return g, vert[0]

def g3():
    g=Graph()
    vert=[]
    for i in range(16):
        vert.append(g.insert_vertex(i))

    g.insert_edge(vert[0], vert[1])
    g.insert_edge(vert[0], vert[2])
    g.insert_edge(vert[0], vert[3])
    g.insert_edge(vert[2], vert[4])
    g.insert_edge(vert[2], vert[5])
    g.insert_edge(vert[4], vert[6])
    g.insert_edge(vert[4], vert[7])
    g.insert_edge(vert[5], vert[8])
    g.insert_edge(vert[8], vert[9])
    g.insert_edge(vert[3], vert[10])
    g.insert_edge(vert[3], vert[11])
    g.insert_edge(vert[10], vert[12])
    g.insert_edge(vert[10], vert[13])
    g.insert_edge(vert[11], vert[14])
    g.insert_edge(vert[14], vert[15])

    return g, vert[0]

def g4():
    g = Graph()
    vert = []
    for i in range(32):
        vert.append(g.insert_vertex(i))

    g.insert_edge(vert[0],vert[1])
    g.insert_edge(vert[1],vert[2])
    g.insert_edge(vert[1],vert[3])
    g.insert_edge(vert[3],vert[4])
    g.insert_edge(vert[3],vert[5])
    g.insert_edge(vert[4],vert[6])
    g.insert_edge(vert[4],vert[9])
    g.insert_edge(vert[6],vert[7])
    g.insert_edge(vert[6],vert[8])
    g.insert_edge(vert[9],vert[10])
    g.insert_edge(vert[9],vert[11])
    g.insert_edge(vert[1],vert[12])
    g.insert_edge(vert[12],vert[13])
    g.insert_edge(vert[12],vert[14])
    g.insert_edge(vert[13],vert[15])
    g.insert_edge(vert[13],vert[16])
    g.insert_edge(vert[14],vert[17])
    g.insert_edge(vert[17],vert[18])
    g.insert_edge(vert[17],vert[19])
    g.insert_edge(vert[14],vert[20])
    g.insert_edge(vert[2],vert[21])
    g.insert_edge(vert[21],vert[22])
    g.insert_edge(vert[22],vert[23])
    g.insert_edge(vert[22],vert[24])
    g.insert_edge(vert[21],vert[25])
    g.insert_edge(vert[25],vert[26])
    g.insert_edge(vert[25],vert[29])
    g.insert_edge(vert[26],vert[27])
    g.insert_edge(vert[26],vert[28])
    g.insert_edge(vert[29],vert[30])
    g.insert_edge(vert[29],vert[31])

    return g,vert[0]

def g5():
    g = Graph()
    vert = []
    for i in range(17):
        vert.append(g.insert_vertex(i))

    g.insert_edge(vert[0],vert[1])
    g.insert_edge(vert[0],vert[2])
    g.insert_edge(vert[0],vert[5])
    g.insert_edge(vert[0],vert[16])
    g.insert_edge(vert[1],vert[13])
    g.insert_edge(vert[2],vert[4])
    g.insert_edge(vert[2],vert[3])
    g.insert_edge(vert[3],vert[12])
    g.insert_edge(vert[3],vert[9])
    g.insert_edge(vert[4],vert[6])
    g.insert_edge(vert[5],vert[8])
    g.insert_edge(vert[5],vert[7])
    g.insert_edge(vert[7],vert[14])
    g.insert_edge(vert[9],vert[10])
    g.insert_edge(vert[10],vert[15])
    g.insert_edge(vert[9],vert[11])

    return g, vert[0]

def g6():
    g = Graph()
    vert = []
    for i in range(2):
        vert.append(g.insert_vertex(i))

    g.insert_edge(vert[0], vert[1])

    return g, vert[0]

def g7():
    g = Graph()
    vert = []
    for i in range(1):
        vert.append(g.insert_vertex(i))

    return g, vert[0]

def g8():
    g = Graph()
    vert = []
    for i in range(10):
        vert.append(g.insert_vertex(i))

    g.insert_edge(vert[0], vert[1])
    g.insert_edge(vert[0], vert[2])
    g.insert_edge(vert[1], vert[3])
    g.insert_edge(vert[1], vert[4])
    g.insert_edge(vert[1], vert[5])
    g.insert_edge(vert[3], vert[7])
    g.insert_edge(vert[4], vert[8])
    g.insert_edge(vert[4], vert[9])
    g.insert_edge(vert[2], vert[6])

    return g, vert[0]
