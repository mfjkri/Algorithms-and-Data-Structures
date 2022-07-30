"""
    Problem #2: Implement the topological sort algorithm 
    - You are to implement the topological sort algorithm
    - Each function comes with instructions on how to implement them. 
    (Don't change anything that is already written for you)


    - The DirectedEdge class has been implemented for you and contains the following attributes:
        -> src: edge from
        -> dest: edge to

    - The Digraph class has been implemented for you and comes with the following:
        -> adjList: 2D list representing adj list of undirected graph.
        Each vertex points to a list of it's adjacent DirectedEdges

        -> addEdge: Takes in an edge as a tuple (src, dest) and adds it as a DirectedEdge to the adjList
        -> printGraph: prints the adj list of each vertex out

    - To test your implementation, run `python utils/topsort_test.py`
"""

from typing import List, Union
from utils.helpers import Digraph, DirectedEdge


class CyclicDirectedGraph(Exception):
    pass


def dfs(current_vertex_index: int,
        graph: Digraph,
        adjList: List[DirectedEdge],
        stack_vertex_order: List[int],
        visited: List[bool],
        topo_order: List[int]) -> None:

    if visited[current_vertex_index] is False:
        visited[current_vertex_index] = True
        stack_vertex_order.append(current_vertex_index)

        for adj_vertex in adjList:
            adj_vertex: DirectedEdge
            adj_vertex_index: int = adj_vertex.dest

            # If we have already passed this vertex earlier in the same stack calls
            # this means that we have completed a cycle
            # hence the directed graph is cylic.
            # Raise an exception here so we can catch it below
            if adj_vertex_index in stack_vertex_order:
                raise CyclicDirectedGraph()

            # Else, we can just traverse further
            # No need to check if we already visited this vertex
            # as we already have a check at the start of this function
            # (maybe can still have one to reduce number of function calls made)
            dfs(
                current_vertex_index=adj_vertex_index,
                graph=graph,
                adjList=graph.adjList[adj_vertex_index],
                stack_vertex_order=stack_vertex_order,
                visited=visited,
                topo_order=topo_order
            )

        # post-order visiting
        topo_order.append(current_vertex_index)


def topsort(digraph: Digraph) -> Union[List[int], None]:
    """Topological sort algorithm

    Arguments
    ----------
    digraph: type `Digraph`
        -> Adjacency list undirected graph to sort
        -> Each vertex in adjList points to a list of DirectedEdges

    Return: 
    - None if digraph contains a cycle
    - A list of vertices where the vertices are sorted in topological order (starting from start) from left to right
    """

    # 1. Initialise visited array
    visited: List[bool] = [False] * len(digraph.adjList)

    topo_order: List[int] = []

    # 2. For each vertex not already visted, recursively visit all adjacent vertices if not already visited

    #    2a. Each time a vertex is visited, set visited[vertex] to True
    #    2b. Keep track of vertices currently on the recursive stack. If a vertex visited is on the
    #        recursive stack, a cycle is present

    for vertex_index, adjList in enumerate(digraph.adjList):
        adjList: List[DirectedEdge]
        try:
            dfs(
                current_vertex_index=vertex_index,
                graph=digraph,
                adjList=adjList,
                stack_vertex_order=list(),
                visited=visited,
                topo_order=topo_order
            )
        except CyclicDirectedGraph:
            return None

    # 3. Return ordering of vertices visited in dfs reversed
    return topo_order[::-1]
