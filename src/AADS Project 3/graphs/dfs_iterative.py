def DFS_iterative(g, u):
    while u is not None:
        if g.degree(u) > 0:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if not v.is_discovered:
                    v.set_discovered(True)
                    v.set_predecessor(u)
                    u = v
                    break
            else:
                u = u.get_predecessor()
        else:
            u = u.get_predecessor()


def DFS_complete_iterative(g):
    forest = {}
    for u in g.vertices():
        if not u.is_discovered:
            forest[u] = None  # u will be the root of a tree
            u.set_discovered(True)
            DFS_iterative(g, u)
    for v in g.vertices():
        if v.get_predecessor() is not None:
            forest[v] = g.get_edge(v, v.get_predecessor())
    return forest


def _DFS_iterative_with_discovered(g, u, discovered):
    while u is not None:
        if g.degree(u) > 0:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    v.set_predecessor(u)
                    u = v
                    break
            else:
              u = u.get_predecessor()
        else:
            u = u.get_predecessor()
