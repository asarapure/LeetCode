class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbours(self, val):
        self.connectedTo[val] = 1

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def __str__(self):
        return str(self.id) + 'connected to' + str([x.id for x in self.connectedTo])

class Graph :
    def __init__(self):
        self.vertdict = {}
        self.numVertices = 0

    def addVertex(self, key):
        if key not in vertdict :
            self.numVertices += 1
            newvertex = Vertex(key)
            self.vertdict[key] = newvertex
            return newvertex

    def addEdge(self, f, t, cost = 0 ):
        if f not in self.vertdict:
            self.vertdict[f] = Vertex(f)
        if t not in self.vertdict :
            self.vertdict[t] = Vertex[t]
        self.vertdict[f].addNeighbours(self.vertdict[t], cost)

g = Graph()
for i in range(6):
    g.addVertex(i)

print(g.vertdict)

g.addEdge(1,2, 4)
g.addEdge(3, 5, 3)
g.addEdge(4,0, 1)

for v in g:
    for w in v.getConnections():
        print("(%s, %s)") %(v.getId(), w.getId()))


v = Vertex(5)
v.addNeighbours(3)
v.addNeighbours(23)
print(v.getConnections())
print(v.getId())
for k,v in v.connectedTo :
    print(str(k) + ":" + str(v))
