class DirectedEdge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


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

def main():

    V = 7
    digraph = Digraph(V)
    edges = [(0, 1), (1, 4), (1, 3), (2, 3), (0, 3), (0, 5), (5, 0), (5, 6)]
    for edge in edges:
        digraph.addEdge(edge)

    digraph.printGraph()


if __name__ == "__main__":
    main()
