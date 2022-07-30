def dfsRecurse(graph, v, visited):
    visited[v] = True
    print("visiting vertex {}".format(v))

    for dest in graph.adjList[v]:
        if not visited[dest]:
            dfsRecurse(graph, dest, visited)
    return


def dfs(graph, start):
    visited = [False] * len(graph.adjList)
    dfsRecurse(graph, start, visited)


def bfs(graph, start):
    '''
        enqueue: queue.append()
        dequeue: queue.pop(0)
    '''

    visited = [False] * len(graph.adjList)
    queue = []
    queue.append(start)
    visited[start] = True

    while len(queue) != 0:
        v = queue.pop(0)
        print("visiting vertex {}".format(v))

        for dest in graph.adjList[v]:
            if not visited[dest]:
                visited[dest] = True
                queue.append(dest)


def main():
    g = __import__('01_graph')
    V = 7
    graph = g.Graph(V)

    edges = [(0, 1), (0, 3), (0, 5), (1, 4), (1, 3), (3, 2), (5, 6)]
    for edge in edges:
        graph.addEdge(edge)
    
    print("PERFORMING DFS")
    dfs(graph, 0)

    print("\nPERFORMING BFS")
    bfs(graph, 0)

if __name__ == "__main__":
    main()
