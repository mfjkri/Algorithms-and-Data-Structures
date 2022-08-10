'''
    Problem #1: Implement Lazy Prim's MST algorithm (ElogE time complexity)
    - You are to implement the LazyPrimMST function below

    - The WeightedEdge class has been implemented for you and contains the following attributes:
        -> src: edge from
        -> dest: edge to
        -> weight: weight of edge

    - The WeightedGraph class has been implemented for you and comes with the following:
        -> adjList: 2D list representing adj list of weighted undirected graph.
        Each vertex points to a list of it's adjacent WeightedEdges
        -> addEdge: Takes in a weighted edge as a tuple (src, dest, weight) and adds it as a WeightedEdge to the adjList
        -> printGraph: prints the adj list of each vertex out

    - The MinHeap class from lesson 2 has been implmented for you and comes with the following:
        -> constructor: takes in maxsize
        -> insert(key, value): method to insert a key-value pair into heap
        -> getMin(): method to get minimum HeapItem from min heap

    - To test your implementation, run `python utils/prim_test.py`
'''

from utils.heap import MinHeap
from utils.helpers import WeightedGraph


def LazyPrimMST(graph: WeightedGraph):
    """Prim's Minimum Spannning Tree Algorithm

    Arguments
    ----------
    graph: type `WeightedGraph`
        -> Weighted graph to perform Prim's algorithm on

    Return: 
    - A list of WeightedEdges part of the MST
    """

    # PSEUDO CODE

    # Let V be the number of vertices and E the number of edges
    # 1. Initialise a minimum priority queue

    V = len(graph.adjList)
    pq = MinHeap(V ** 2)

    # 2. Initialise inMST (size V array of boolean)

    # 3. Choose a starting vertex that is not already in the MST
    # 4. Set inMST[vertex] to be True, and then add all adjacent edges to the minpq
    # 5. While pq is not empty:
    # a. Get min edge from minpq
    # b. Add edge to result array
    # c. For each vertex part of the min edge, if not already in the MST,
    #    add all adjacent edges to minpq

    # 6. Repeat step 3 - 5 until all vertices are part of the MST

    return []
