class Vertex :
    def __init__(self, val):
        self.key = val
        self.connectedTo = {}

    def addNeighbours(self, newkey):
        self.connectedTo[newkey] = 1


class Graph :
    def __init__(self):
        self.numVertices = 0
        self.vertdict = {}

    def addVertex(self, key):
        if key not in self.vertdict :
            self.vertdict[key] = Vertex(key)

    def addEdge(self, a, b) :
        if a not in self.vertdict:
            self.vertdict[a] = Vertex(a)
        if b not in self.vertdict :
            self.vertdict[b] = Vertex(b)
        self.vertdict[a].addNeighbours(self.vertdict[b])

g = Graph()
for i in range(4) :
    g.addVertex(i)
print(g.vertdict[2].connectedTo)
g.addEdge(2,3)

print(g.vertdict)
print(g.vertdict[2].connectedTo)
g.addEdge(1,2)
print(g.vertdict)