'''
    Problem #2: Implement Dijkstra's Shortest Path algorithm (ElogV time complexity)
    - You are to implement the DijkstraSP function below

    - The WeightedEdge class has been implemented for you and contains the following attributes:
        -> src: edge from
        -> dest: edge to
        -> weight: weight of edge

    - The WeightedDigraph class has been implemented for you and comes with the following:
        -> adjList: 2D list representing adj list of weighted digraph.
        Each vertex points to a list of it's adjacent WeightedEdges
        -> addEdge: Takes in a weighted edge as a tuple (src, dest, weight) and adds it as a WeightedEdge to the adjList
        -> printGraph: prints the adj list of each vertex out

    - The MinHeap class from lesson 2 has been implmented for you and comes with the following:
        -> constructor: takes in maxsize
        -> insert(key, value): method to insert a key-value pair into heap
        -> getMin(): method to get minimum HeapItem from min heap
        -> decreaseKey(key, newValue): method to decrease the value of an existing key in heap

    - You may assume that all graphs only contain positive weights
    - To test your implementation, run `python utils/dijkstra_test.py`
'''

from typing import List, Union

from utils.heap import MinHeap
from utils.helpers import WeightedDigraph, WeightedEdge

INF = float("inf")


def DijkstraSP(graph: WeightedDigraph, start: int):
    """Dijkstra's shortest path algorithm

    Arguments
    ----------
    graph: type `WeightedDigraph`
        -> Weighted digraph (only positive weights) to perform Dijkstra's shortest path algorithm on
    start: type `int`
        -> The start vertex for which Dijkstra calculates the
        shortest path from to every other vertex

    Return:
    - edgeTo: A list of WeightedEdges where edgeTo[index] is the last edge to that index
    - distTo: A list of ints where distTo[index] = shortest path from start to that vertex
    in the shortest path from start to that vertex
    - edgeTo should be the first return value, followed by distTo
    - False if graph contains negative weight edges
    """

    # PSEUDO CODE

    # Let V be the number of vertices and E the number of edges
    # 1. Initialise a minimum priority queue

    V: int = len(graph.adjList)
    pq: MinHeap = MinHeap(V)

    # 2. Initialise edgeTo (length V array of ints `start at None`)
    edgeTo: List[Union[WeightedEdge, None]] = [None] * V

    # 3. Initialise distTo (length V array of ints `start at infinity or None`)
    distTo: List[int] = [INF] * V

    # 4. Set distTo[start] to be 0 and insert into minpq,
    # where key is the vertex and value is the distTo[vertex]
    distTo[start] = 0
    pq.insert(start, 0)

    # 5. While pq is not empty:
    while pq.size:

        # a. Get min vertex v from minpq. Note: MinHeap.GetMin() returns a HeapItem
        curr_vertex: int = pq.getMin().key
        edges: WeightedEdge = graph.adjList[curr_vertex]

        # b. For each adjacent edge of v, relax
        for adj_edge in edges:
            adj_edge: WeightedEdge
            adj_vertex: int = adj_edge.dest
            adj_edge_weight: int = adj_edge.weight

            if adj_edge_weight < 0:
                return False

            # Relaxing an edge:

            # If distTo[src] + edge.weight < distTo[dest]:
            new_dist: int = distTo[curr_vertex] + adj_edge_weight

            if new_dist < distTo[adj_vertex]:
                # distTo[dest] = distTo[src] + edge.weight
                distTo[adj_vertex] = new_dist

                # edgeTo[dest] = edge
                edgeTo[adj_vertex] = adj_edge

                # insert dest & edge into pq if dest not in pq, or decrease key if it is
                if adj_vertex not in pq.positions:
                    pq.insert(adj_vertex, new_dist)
                else:
                    pq.decreaseKey(
                        key=adj_vertex,
                        newValue=new_dist
                    )

    return edgeTo, distTo
