class WeightedEdge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __str__(self):
        return "({} - {} | {})".format(self.src, self.dest, self.weight)


class WeightedGraph:
    def __init__(self, V):
        self.adjList = [[] for i in range(V)]

    def addEdge(self, src, dest, weight):
        newEdge1 = WeightedEdge(src, dest, weight)
        self.adjList[src].append(newEdge1)

        newEdge2 = WeightedEdge(dest, src, weight)
        self.adjList[dest].append(newEdge2)

    def printGraph(self):
        for i in range(len(self.adjList)):
            print(i, end=": ")
            for j in range(len(self.adjList[i])):
                if j == len(self.adjList[i]) - 1:
                    print(self.adjList[i][j])
                else:
                    print(self.adjList[i][j], end=", ")


class WeightedDigraph:
    def __init__(self, V):
        self.adjList = [[] for i in range(V)]

    def addEdge(self, src, dest, weight):
        newEdge1 = WeightedEdge(src, dest, weight)
        self.adjList[src].append(newEdge1)

    def printGraph(self):
        for i in range(len(self.adjList)):
            print(i, end=": ")
            for j in range(len(self.adjList[i])):
                if j == len(self.adjList[i]) - 1:
                    print(self.adjList[i][j])
                else:
                    print(self.adjList[i][j], end=", ")
