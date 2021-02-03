def _func(g, u, tab, parent):
    #if the solution is not already calculated for the current vertex:
    if u not in tab:
        #list of vertices in which the current vertex is included
        incl_list = [u]
        #list of vertices in which the current vertex is excluded
        excl_list = []
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if parent is not v: #if v is not the parent of u
                _func(g, v, tab, u) #calling the function for the vertex v and adding it's solution to the incl_list
                sol_v = tab[v]
                incl_list += sol_v
                excl_list += sol_v
                if len(sol_v) == 0 or sol_v[0] is not v:
                    excl_list = excl_list + [v] #if v is not already included in the solution, include it

        if len(incl_list) <= len(excl_list): #if the incl_list solution has less vertex of the excl_list one
            tab[u] = incl_list  #save incl_list solution in tab[u]
        else: #else if the excl_list solution has less vertex of the incl_list one
            tab[u] = excl_list #save excl_list solution in tab[u]


#function to call.
#g is the graph
#u is the starting vertex
def call_func(g, u):

    if g.vertex_count() == 1:
        return [u]

    tab = {} #Key --> vertex
             #Value --> solution until that vertex (included)

    _func(g, u, tab, None)

    return tab[u]
