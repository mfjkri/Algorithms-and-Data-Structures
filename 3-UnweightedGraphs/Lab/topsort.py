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

from enum import Enum, auto
from typing import List, Dict, Union
from utils.helpers import Digraph, DirectedEdge


class VisitStatus(Enum):
    IN_PROGRESS = auto()
    SAFE = auto()


def check_for_cycle(curr_vertex: int,
                    adjList: List[List[DirectedEdge]],
                    visited: Dict[int, Union[VisitStatus, None]]) -> bool:

    if curr_vertex in visited:
        # If the current vertex is already marked as in progress
        # then this means that we have a cycle
        if visited[curr_vertex] == VisitStatus.IN_PROGRESS:
            return True
        # Else if it already marked as safe,
        # no point checking this vertex again (and its edges)
        elif visited[curr_vertex] == VisitStatus.SAFE:
            return False

    # Mark the current vertex as in progress
    visited[curr_vertex] = VisitStatus.IN_PROGRESS

    # Process all its edges
    for adj_edge in adjList[curr_vertex]:
        adj_edge: DirectedEdge
        adj_vertex: int = adj_edge.dest

        # Check each adj vertex for a cycle
        # If a cycle is detected for an adj vertex
        # Then propagate it upwards (to the parent function call)
        if check_for_cycle(
            curr_vertex=adj_vertex,
            adjList=adjList,
            visited=visited
        ):
            return True

    # After all its edges has been processed
    # (we won't reach this point if a cycle is detected in itself or its connected edges)
    # We can then mark this vertex as safe
    visited[curr_vertex] = VisitStatus.SAFE

    # Return false to propagate that this vertex contains no cycles
    return False


def dfs(curr_vertex: int,
        adjList: List[List[DirectedEdge]],
        visited: List[bool],
        topo_order: List[int]) -> None:

    if visited[curr_vertex] is False:
        visited[curr_vertex] = True

        for adj_edge in adjList[curr_vertex]:
            adj_edge: DirectedEdge
            adj_vertex: int = adj_edge.dest

            dfs(
                curr_vertex=adj_vertex,
                adjList=adjList,
                visited=visited,
                topo_order=topo_order
            )

        # post-order visiting
        topo_order.append(curr_vertex)


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

    for vertex, adj_edges in enumerate(digraph.adjList):
        adj_edges: List[DirectedEdge]

        if check_for_cycle(
            curr_vertex=vertex,
            adjList=digraph.adjList,
            visited={}
        ):
            return None

        dfs(
            curr_vertex=vertex,
            adjList=digraph.adjList,
            visited=visited,
            topo_order=topo_order
        )

    # 3. Return ordering of vertices visited in dfs reversed
    return topo_order[::-1]
