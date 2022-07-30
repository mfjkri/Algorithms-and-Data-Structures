class Graph:
    def __init__(self, V):
        self.adjList = [[] for i in range(V)]

    def addEdge(self, edge):
        src, dest = edge

        self.adjList[src].append(dest)
        self.adjList[dest].append(src)

    def printGraph(self):
        for i in range(len(self.adjList)):
            print("vertex {}".format(i), end='')
            for dest in self.adjList[i]:
                print(" -> {}".format(dest), end="")

            print()


class DirectedEdge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def __str__(self) -> str:
        return f"({self.src}) -> ({self.dest})"

    def __repr__(self) -> str:
        return str(self)


class Digraph:
    def __init__(self, V):
        self.adjList = [[] for i in range(V)]

    def addEdge(self, edge):
        src, dest = edge
        self.adjList[src].append(DirectedEdge(src, dest))

    def printGraph(self):
        for v in range(len(self.adjList)):
            print("vertex {}: ".format(v), end="")
            for edge in self.adjList[v]:
                print("({}, {})".format(edge.src, edge.dest), end=" ")
            print()
