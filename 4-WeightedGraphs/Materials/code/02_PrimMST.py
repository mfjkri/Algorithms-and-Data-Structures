'''
    Prim's MST algorithm: ElogV time
'''

from heap import MinHeap
from graphs import WeightedEdge

class WeightedGraph:
    def __init__(self, V):
        self.adjList = [[] for i in range(V)]

    def addEdge(self, src, dest, weight):
        newEdge1 = WeightedEdge(src, dest, weight)
        self.adjList[src].append(newEdge1)

        newEdge2 = WeightedEdge(dest, src, weight)
        self.adjList[dest].append(newEdge2)


def LazyPrimMST(graph: WeightedGraph):
    V = len(graph.adjList)

    edgeTo = [-1] * V
    distTo = [None] * V
    inMST = [False] * V

    pq = MinHeap(V)

    for v in range(V):
        if not inMST[v]:
            prim(graph, v, pq, distTo, edgeTo, inMST)

    return edgeTo


def prim(graph, s, pq: MinHeap, distTo, edgeTo, inMST):
    distTo[s] = 0
    pq.insert(s, distTo[s])
    while (pq.size != 0):
        v = pq.getMin().key
        inMST[v] = True

        for edge in graph.adjList[v]:
            if inMST[edge.dest]:
                continue

            if distTo[edge.dest] == None or edge.weight < distTo[edge.dest]:
                distTo[edge.dest] = edge.weight
                edgeTo[edge.dest] = edge

                if edge.dest in pq.positions:
                    pq.decreaseKey(edge.dest, edge.weight)
                else:
                    pq.insert(edge.dest, edge.weight)

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
        print(edge)

if __name__ == "__main__":
    main()
