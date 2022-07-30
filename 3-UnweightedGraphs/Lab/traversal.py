"""
    Problem #1: Implement depth-first search & breadth-first search
    - You are to implement the dfs & bfs functions below.
    - Each function comes with instructions on how to implement them. 
    (Don't change anything that is already written for you)

    - The Graph (Undirected) class has been implemented for you
    - It comes with the following attributes:
        -> adjList: 2D list representing adj list of undirected graph
    - It comes with the following methods:
        -> addEdge: Takes in an edge as a tuple (u, v) and adds an edge from u to v
        -> printGraph: prints the adj list of each vertex out

    - To test your implementation, run `python utils/traversal_test.py`
"""


from typing import Deque, List
from collections import deque

from utils.helpers import Graph


def dfsRecurse(v: int, graph: Graph, visited: List[bool], result: List[int]) -> None:
    visited[v] = True
    result.append(v)

    for adj_vertex in graph.adjList[v]:
        if visited[adj_vertex] is False:
            dfsRecurse(adj_vertex, graph, visited, result)


def dfs(graph: Graph, start: int) -> List[int]:
    """
    Depth-first search from source

    Arguments
    ----------
    graph: type `Graph`
        -> Adjacency list undirected graph to traverse
    start: type `int`
        -> Vertex to begin depth-first search

    Return: 
    - A list of vertices where the vertices are visited in order, 
    by depth first search, from left to right
    """

    result: List[int] = []

    # 1. Initialise visited array
    visited: List[bool] = [False] * len(graph.adjList)

    # 2. From the starting vertex, recursively visit all adjacent vertices if not already visited
    #    2a. Each time a vertex is visited, set visited[vertex] to True
    dfsRecurse(
        v=start,
        graph=graph,
        visited=visited,
        result=result
    )

    # 3. Return ordering of vertices visited in dfs
    return result


def norecurse_dfs(graph: Graph, start: int) -> List[int]:
    """Depth-first search from source

    Arguments
    ----------
    graph: type `Graph`
        -> Adjacency list undirected graph to traverse
    start: type `int`
        -> Vertex to begin depth-first search

    Return: 
    - A list of vertices where the vertices are visited in order, 
    by depth first search, from left to right
    """

    result: List[int] = []

    # 1. Initialise stack
    stack: List[int] = []

    # 2. Initialise visited array
    visited: List[bool] = [False] * len(graph.adjList)

    # 3. Push start into stack
    stack.append(start)

    while stack:
        current_vertex: int = stack.pop()

        # Only visit the vertex if not already visited
        if visited[current_vertex] is False:
            visited[current_vertex] = True

            # - Push all adjacent vertices into stack
            for adj_vertex in graph.adjList[current_vertex][::-1]:
                stack.append(adj_vertex)

            # Add visited vertex to result
            result.append(current_vertex)

    # 3. Return ordering of vertices visited in dfs
    return result


def bfs(graph: Graph, start: int) -> List[int]:
    """Breadth-first search from source

    Arguments
    ----------
    graph: type `Graph`
        -> Adjacency list undirected graph to traverse
    start: type `int`
        -> Vertex to begin breadth-first search

    Return: 
    - A list of vertices where the vertices are visited in order, 
    by breadth first search, from left to right
    """

    result: List[int] = []

    # 1. Initialise empty queue
    queue: Deque = deque()

    # 2. Initialise enqueued array
    enqueued: List[bool] = [False] * len(graph.adjList)

    # 3. Enqueue starting vertex
    queue.append(start)
    enqueued[start] = True

    # 4. While queue is not empty:
    while queue:

        # - Dequeue vertex
        current_vertex: int = queue.popleft()

        # - Enqueue all adjacent vertices not already queued
        for adj_vertex in graph.adjList[current_vertex]:
            if enqueued[adj_vertex] is False:
                queue.append(adj_vertex)
                enqueued[adj_vertex] = True

        # Add visited vertex to result
        result.append(current_vertex)

    # 5. Return ordering of vertices visited in bfs
    return result
