from graphs.graph import Graph

class ExtendedGraph(Graph):
    class ExtendedVertex(Graph.Vertex):
        __slots__ = '_predecessor', '_discovered'

        def __init__(self, x):
            super().__init__(x)
            self._predecessor = None
            self._discovered = False

        def set_predecessor(self, predecessor):
            self._predecessor = predecessor

        def get_predecessor(self):
            return self._predecessor

        @property
        def is_discovered(self):
            return self._discovered

        def set_discovered(self, discovered):
            self._discovered = discovered

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x."""
        v = self.ExtendedVertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}        # need distinct map for incoming edges
        return v

    def print_graph(self):
        print("****VERTEX*****")
        for v in self.vertices():
            print(v)
        print("****EDGE*****")
        for e in self.edges():
            print(e)
