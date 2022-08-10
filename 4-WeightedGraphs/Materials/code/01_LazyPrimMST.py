'''
    Lazy Prim's MST algorithm: ElogE time
'''
from heap import MinHeap

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

    def printGraph(self):
        for i in range(len(self.adjList)):
            print(i, end= ": ")
            for j in range(len(self.adjList[i])):
                if j == len(self.adjList[i]):
                    print(j)
                else: 
                    print(j, end = ", ")

def LazyPrimMST(graph: WeightedGraph):
    V = len(graph.adjList)

    inMST = [False] * V
    mstEdges = []

    pq = MinHeap(100)

    for v in range(V):
        if not inMST[v]:
            prim(graph, v, pq, inMST, mstEdges)

    return mstEdges


def prim(graph, s, pq: MinHeap, inMST, mstEdges):

    addEdgesToPQ(graph, s, pq, inMST)

    while (pq.size != 0):
        edge = pq.getMin().key

        if inMST[edge.dest]:
            continue

        mstEdges.append(edge)
        addEdgesToPQ(graph, edge.dest, pq, inMST)

def addEdgesToPQ(graph, s, pq, inMST):
    inMST[s] = True
    for edge in graph.adjList[s]:
        pq.insert(edge, edge.weight)

def main():
    V = 8
    edges = [(0, 1, 20), (0, 2, 10), (0, 3, 25), (1, 2, 5), (1, 4, 12), (2, 5, 14), (3, 5, 30),
             (4, 5, 6), (5, 6, 11), (5, 7, 7), (6, 7, 16)
             ]
    
    graph = WeightedGraph(V)
    for edge in edges:
        src, dest, weight = edge
        graph.addEdge(src, dest, weight)
    
    mstEdges = LazyPrimMST(graph)
    for edge in mstEdges:
        print(edge.src, "-", edge.dest)

if __name__ == "__main__":
    main()