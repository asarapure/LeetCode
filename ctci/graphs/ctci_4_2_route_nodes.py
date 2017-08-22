from collections import deque

class Vertex :
    def __init__(self, key):
        self.name = key
        self.neighbours = []
        self.distance = 0
        self.color = ''

class Graph :
    vertices = {}

    def addVertex(self, v):
        if isinstance(v, Vertex) and v not in self.vertices :
            self.vertices[v.name] = v

    def addEdges(self, u, v):
        if u.name and v.name in self.vertices :
            self.vertices[u.name].neighbours.append(v.name)
            self.vertices[v.name].neighbours.append(u.name)

    def is_route_between(self, v1, v2 ) :
        if v1 is v2 :
            return True
        elif v1 is None or v2 is None :
            return False
        visited = set([v1.name, v2.name])
        print(visited)
        queue = deque([v1])
        while len(queue) > 0 :
            node = queue.popleft()
            print("here")
            for child in node.neighbours  :
                print(child)
                if self.vertices[child] is v2 :
                    print("we found a route.")
                    return  True

                elif child not in visited :
                    print("add")
                    visited.add(child)
                    queue.append(child)


v1 = Vertex('a')
v2 = Vertex('b')
v3 = Vertex('c')

g = Graph()
g.addVertex(v1)
g.addVertex(v2)
g.addVertex(v3)

g.addEdges(v1, v2)
g.addEdges(v2, v3)
g.is_route_between(v1, v3)