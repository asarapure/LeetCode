class Vertex :
    def __init__(self, n):
        self.name = n
        self.neighbours = []

    def addNeighbours(self,v):
        if v not in self.neighbours :
            self.neighbours.append(v)

class Graph :
    vertices = {}

    def addVertex(self,vertex):
        if vertex.name not in self.vertices :
            self.vertices[vertex.name] = vertex
            return True
    def add_edge(self, a, b):
        if a in self.vertices and b in self.vertices :
            for k, v in self.vertices.items():
                if k == a :
                    v.addNeighbours(b)
                if k == b :
                    v.addNeighbours(a)
            return True
        else:
            return False

g = Graph()
v5 = Vertex(5)

g.addVertex(v5)
print(g.vertices)




print('vertex present')
return False

g.addVertex(v5)



g = Graph()
v7 = Vertex(7)
v8 = Vertex(8)
v9 = Vertex(9)

g.addVertex(v7)
g.addVertex(v8)
g.addVertex(v9)

g.addEdge(v7, v8)
g.addEdge(v7, v9)

g.printGraph()