# author: Svante Aretun
# date: March 17, 2023
# Vertex and Graph classes
from collections import deque


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.numVertices += 1
        self.vertList[key] = newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList.values()

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def breadth_first_search(self, s):
        for v in self:
            v.color = 'white'

        queue = deque()

        self.vertList[s].color = 'gray'
        queue.append(self.vertList[s])
        path = []

        while queue:
            u = queue.popleft()
            path.append(u.id)

            for v in u.getConnections():
                if v.color == 'white':
                    v.color = 'gray'
                    queue.append(v)

            u.color = 'black'

        return path

    def depth_first_search(self):
        for v in self:
            v.color = 'white'

        path = []

        for v in self:
            if v.color == 'white':
                self.DFS(v, path)

        return path

    def DFS(self, vid, path):
        vid.color = 'gray'
        path.append(vid.id)

        for v in vid.getConnections():
            if v.color == 'white':
                self.DFS(v, path)
        vid.color = 'black'


if __name__ == '__main__':

    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 0)
    g.addEdge(5, 4)
    g.addEdge(5, 2)

    for v in g:
        print(v)

    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False

    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'

    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'

    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]

    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]