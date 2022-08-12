import math
from sys import argv
from time import time
from typing import Dict, List, Tuple

from exchangeRates import exchangeRates


INF = float("inf")
GRAPH = Dict[str, List[Tuple[str, str, float]]]
EDGE = Tuple[str, str, float]
EDGE_WTIHOUT_WEIGHT = Tuple[str, str]


def arbitrage(exchangeRates: GRAPH) -> List[EDGE_WTIHOUT_WEIGHT]:

    # CONVERT EXCHANGE RATES TO LOG GRAPH
    logGraph: GRAPH = convertToLogGraph(exchangeRates)

    # RETRIEVES SHORTEST PATH TREE / NONE THROUGH BELLMAN FORD ALGO
    shortestPathTree: Dict[str, str] = bellmanFord(logGraph)

    # RETRIEVES EDGES INVOLVED IN CYCLE IF THERE IS ONE
    return searchForCycle(shortestPathTree)


def convertToLogGraph(exchangeRates: GRAPH) -> GRAPH:
    """
    convertToLogGraph:
        - This function takes in a graph of exchange rates, and returns an adjacency list with the same edges, but with every weight having the negative log10 function applied
    """

    new_graph: GRAPH = {}

    vertex: str
    edges: List[EDGE]
    for vertex, edges in exchangeRates.items():

        new_edges: List[EDGE] = []

        edge: EDGE
        for edge in edges:

            src: str
            dest: str
            edge_weight: float

            src, dest, edge_weight = edge
            # Create new edge but apply -log10() to edge weight
            new_edges.append((src, dest, -math.log(edge_weight, 10)))

        new_graph.update({vertex: new_edges})

    return new_graph


def bellmanFord(logGraph: GRAPH) -> Dict[str, List[EDGE]]:
    """
    bellmanFord:
        - This function will take in the logGraph (output of convertToLogGraph function), and returns the shortest path tree
        - The shortest path tree is essentially an adjacent list made up of the edges involved in the edgeTo list.
    """

    dist_to: Dict[str, float] = {}
    edge_to: Dict[str, Tuple[str, float]] = {}

    # Populate dist_to and edge_to with starting values for each vertices
    for vertex in logGraph.keys():
        edge_to.update({vertex: None})
        dist_to.update({vertex: INF})

    # Set starting vertex
    dist_to.update(
        {list(dist_to.keys())[1]: 0}
    )

    # For every vertex
    for _, _ in logGraph.items():

        vertex: str
        edges: List[EDGE]
        for vertex, edges in logGraph.items():

            dist_to_vertex: float = dist_to.get(vertex)

            # For every edge
            edge: EDGE
            for edge in edges:

                adj_vertex: str
                edge_weight: float
                _, adj_vertex, edge_weight = edge

                new_dist: float = dist_to_vertex + edge_weight

                # Relax edge

                # Check whether new distance is better than current distance
                # If better then update to new distance and set new edge_to
                if new_dist < dist_to.get(adj_vertex):
                    dist_to.update({adj_vertex: new_dist})
                    edge_to.update({adj_vertex: (vertex, edge_weight)})

    shortest_tree_path: Dict[str, List[EDGE]] = {}

    vertex: str
    prev_vertex: str
    for vertex, prev_edge in edge_to.items():

        if prev_edge:

            prev_vertex: str
            edge_weight: float
            prev_vertex, edge_weight = prev_edge

            edge: EDGE = (prev_vertex, vertex, edge_weight)

            tree_path: List[EDGE] = shortest_tree_path.setdefault(
                prev_vertex, []
            )
            tree_path.append(edge)

    return shortest_tree_path


def checkForCycle(
        current_edge: EDGE,
        current_stack: List[str],
        shortest_path: Dict[str, EDGE],
        cyclic_edges: List[EDGE_WTIHOUT_WEIGHT]) -> None:

    current_vertex: str
    adj_vertex: str
    edge_weight: float
    current_vertex, adj_vertex, edge_weight = current_edge

    # If next vertex is already in stack
    # Means we have completed a cycle
    if adj_vertex in current_stack:
        # We add the edge as (prev_vertex, current_vertex)
        # This is because an edge is determined by:
        #       edge: (src, dest)
        new_cyclic_edge: EDGE_WTIHOUT_WEIGHT = (
            current_vertex, adj_vertex)

        # Check whether we have found this cyclic edge before
        # Only append unique edges (ignore repeats)
        if new_cyclic_edge not in cyclic_edges:
            cyclic_edges.append(new_cyclic_edge)
    else:
        # If no cycle
        # We continue traversing to check further
        current_stack.append(adj_vertex)

        # Process all connecting edges
        next_edges: List[EDGE] = shortest_path.get(adj_vertex)

        if next_edges:

            next_edge: EDGE
            for next_edge in next_edges:

                checkForCycle(
                    current_edge=next_edge,
                    current_stack=current_stack,
                    shortest_path=shortest_path,
                    cyclic_edges=cyclic_edges
                )


def searchForCycle(shortestPathTree: Dict[str, List[EDGE]]) -> List[EDGE_WTIHOUT_WEIGHT]:
    """
    searchForCycle:
        - This function takes in the shortest path tree (output of bellmanFord), and returns a list containing edges (excluding the weights) involved in the negative cycle.
        - For instance, for exchange rates 1, it should return: [('SGD', 'GBP'), ('GBP', 'USD'), ('USD', 'SGD')]

    """

    cyclic_edges: List[EDGE_WTIHOUT_WEIGHT] = []

    edge: EDGE
    for edges in shortestPathTree.values():

        for edge in edges:
            checkForCycle(
                current_edge=edge,
                current_stack=list(),
                shortest_path=shortestPathTree,
                cyclic_edges=cyclic_edges
            )

    return cyclic_edges


def main():
    try:
        n = int(argv[1]) - 1
    except:
        print("No CLA inputted, defaulting to exchangeRate 1")
        n = 0

    start = time()
    print("Arbitrage: {}".format(arbitrage(exchangeRates[n])))
    end = time()
    print("Time taken for arbitrage function: {}s".format(end - start))


if __name__ == "__main__":
    main()
