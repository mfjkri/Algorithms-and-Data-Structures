def dfsRecurse(graph, v, visited, stack):
    visited[v] = True
    stack[v] = True

    for dest in graph.adjList[v]:
        if stack[dest]:
            return True
        if not visited[dest]:
            hasCycle = dfsRecurse(graph, dest, visited, stack)
            if hasCycle:
                return True

    stack[v] = False
    return False


def hasCycle(graph, start):
    visited = [False] * len(graph.adjList)
    stack = [False] * len(graph.adjList)
    
    return dfsRecurse(graph, start, visited, stack)


def main():
    g = __import__('01_graph')
    V = 7
    graph = g.Graph(V)

    edges = [(0, 1), (1, 2), (2, 0), (2, 5), (3, 4)]
    for edge in edges:
        graph.addEdge(edge)
    
    print("Graph has cycle:", hasCycle(graph, 0))

if __name__ == "__main__":
    main()
