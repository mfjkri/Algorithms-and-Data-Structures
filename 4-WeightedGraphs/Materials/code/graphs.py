
class WeightedEdge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __str__(self):
        return "({}, {}, {})".format(self.src, self.dest, self.weight)


class WeightedGraph:
    def __init__(self, V):
        self.adjList = [[] for i in range(V)]

    def addEdge(self, src, dest, weight):
        newEdge1 = WeightedEdge(src, dest, weight)
        self.adjList[src].append(newEdge1)

        newEdge2 = WeightedEdge(dest, src, weight)
        self.adjList[dest].append(newEdge2)

class WeightedDigraph:
    def __init__(self, V):
        self.adjList = [[] for i in range(V)]

    def addEdge(self, src, dest, weight):
        newEdge1 = WeightedEdge(src, dest, weight)
        self.adjList[src].append(newEdge1)
