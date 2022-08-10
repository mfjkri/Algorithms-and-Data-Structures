
'''
    Bellman-Ford algorithm: EV
'''
from graphs import WeightedDigraph

def BellmanFord(graph, s):
    INF = 10000
    V = len(graph.adjList)
    distTo = [INF] * V
    edgeTo = [None] * V

    distTo[s] = 0

    for v in range(V):
        for v in range(V):
            for edge in graph.adjList[v]:
                w = edge.dest
                if distTo[w] > distTo[v] + edge.weight:
                    distTo[w] = distTo[v] + edge.weight
                    edgeTo[w] = edge

    for v in range(V):
        for edge in graph.adjList[v]:
            w = edge.dest
            if distTo[w] > distTo[v] + edge.weight:
                distTo[w] = -INF

    return edgeTo, distTo


def main():
    V = 8
    edges = [(0, 1, 20), (0, 2, 10), (0, 3, 25), (2, 1, 5), (2, 5, 15), (3, 2, 7), (5, 1, -19),
            (5, 7, 8), (5, 6, 3), (1, 4, 12), (4, 5, 6),
            ]

    graph = WeightedDigraph(V)
    for edge in edges:
        src, dest, weight = edge
        graph.addEdge(src, dest, weight)

    edgeTo, distTo = BellmanFord(graph, 0)
    print("EDGE TO: ")
    for edge in edgeTo:
        print(edge)

    print()
    print("DIST TO: ")
    for dist in distTo:
        print(dist)

if __name__ == "__main__":
    main()