class Vertex :
    def __init__(self, val):
        self.name = val

class Graph :
    edges = []
    edge_indices = {}
    vertices = {}

    def addVertex(self, v):
        if isinstance(v, Vertex) and v.name not in self.vertices :
            self.vertices[v.name] = v
            for row in self.edges :
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[v.name] = len(self.edge_indices)
            return True
        else :
            return False

    def add_edge(self, u, v, weight = 1):
        if u in self.vertices and v in self.vertices :
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else :
            return False


