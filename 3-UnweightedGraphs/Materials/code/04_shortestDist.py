def shortestDist(graph, start):
    '''
        enqueue: queue.append()
        dequeue: queue.pop(0)
    '''

    visited = [False] * len(graph.adjList)
    distTo = [0] * len(graph.adjList)
    queue = []
    queue.append(start)
    visited[start] = True

    while len(queue) != 0:
        v = queue.pop(0)

        for dest in graph.adjList[v]:
            if not visited[dest]:
                visited[dest] = True
                distTo[dest] = distTo[v] + 1
                queue.append(dest)

    return distTo

def main():
    g = __import__('01_graph')
    V = 7
    graph = g.Graph(V)

    edges = [(0, 1), (0, 3), (0, 5), (1, 4), (1, 3), (3, 2), (5, 6)]
    for edge in edges:
        graph.addEdge(edge)

    print("dist to vertices:", shortestDist(graph, 0))

if __name__ == "__main__":
    main()
