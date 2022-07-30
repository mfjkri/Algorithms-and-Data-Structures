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


def main():
    V = 7
    graph = Graph(V)

    edges = [(0, 1), (0, 3), (0, 5), (1, 4), (1, 3), (3, 2), (2, 4)]
    for edge in edges:
        graph.addEdge(edge)

    graph.printGraph()


if __name__ == "__main__":
    main()
