'''
    Dijkstra's Shortest Path Algorithm: ElogV
'''

from heap import MinHeap
from graphs import WeightedDigraph


def Dijkstra(graph, s):
    V = len(graph.adjList)
    
    for v in range(len(graph.adjList)):
        for edge in graph.adjList[v]:
            if edge.weight < 0:
                print("Negative weight edge detected")
                return 

    edgeTo = [-1] * V
    distTo = [None] * V
    pq = MinHeap(V)

    distTo[s] = 0
    pq.insert(s, distTo[s])

    while (pq.size != 0):
        v = pq.getMin().key

        for edge in graph.adjList[v]:
            relax(edge, pq, distTo, edgeTo)

    return edgeTo, distTo


def relax(edge, pq, distTo, edgeTo):
    v = edge.src
    w = edge.dest

    if distTo[w] == None or distTo[v] + edge.weight < distTo[w]:
        distTo[w] = distTo[v] + edge.weight
        edgeTo[w] = edge
        if w in pq.positions:
            pq.decreaseKey(w, distTo[w])
        else:
            pq.insert(w, distTo[w])


def constructShortestPath(edgeTo, v):

    cur = edgeTo[v]
    path = [cur.dest]
    while (cur != -1):
        path.append(cur.src)
        cur = edgeTo[cur.src]

    path.reverse()
    
    return path

def main():
    V = 8
    edges = [(0, 1, 20), (0, 2, 10), (0, 3, 25), (2, 1, 5), (1, 4, 12), (2, 5, 35), (3, 5, 30),
            (3, 7, 30), (4, 5, 6), (5, 6, 3), (5, 7, 8), (6, 7, 4)
            ]

    graph = WeightedDigraph(V)
    for edge in edges:
        src, dest, weight = edge
        graph.addEdge(src, dest, weight)

    result = Dijkstra(graph, 0)
    if result is None:
        return
    edgeTo, distTo = result
    vertex = input("display shortest path from 0 to: ")
    print(constructShortestPath(edgeTo, int(vertex)))

if __name__ == "__main__":
    main()