def dfsRecurse(digraph, v, result, visited):
    visited[v] = True

    for edge in digraph.adjList[v]:
        if not visited[edge.dest]:
            dfsRecurse(digraph, edge.dest, result, visited)

    result.append(v)


def topSort(digraph):
    visited = [False] * len(digraph.adjList)
    result = []

    for i in range(len(digraph.adjList)):
        if not visited[i]:
            dfsRecurse(digraph, i, result, visited)     
            
    result.reverse()
    return result


def main():
    digraph = __import__('05_digraph')
    V = 8
    digraph = digraph.Digraph(V)
    edges = [(0, 2), (0, 4), (0, 5), (4, 3), (4, 6),
             (4, 1), (6, 3), (1, 6), (5, 1)]
    for edge in edges:
        digraph.addEdge(edge)

    print(topSort(digraph, 0))


if __name__ == "__main__":
    main()
