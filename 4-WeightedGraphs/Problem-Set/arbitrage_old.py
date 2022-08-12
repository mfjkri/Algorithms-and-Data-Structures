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


def bellmanFord(logGraph: GRAPH) -> Dict[str, str]:
    """
    bellmanFord:
        - This function will take in the logGraph (output of convertToLogGraph function), and returns the shortest path tree
        - The shortest path tree is essentially an adjacent list made up of the edges involved in the edgeTo list.
    """

    dist_to: Dict[str, float] = {}
    edge_to: Dict[str, str] = {}

    # Populate dist_to and edge_to with starting values for each vertices
    vertex: str
    for vertex in logGraph.keys():

        edge_to.update({vertex: ""})
        dist_to.update({vertex: INF})

    # Set starting vertex
    dist_to.update(
        {list(dist_to.keys())[0]: 0}
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
                    edge_to.update({adj_vertex: vertex})

    return edge_to


def checkForCycle(
        current_vertex: str,
        current_stack: List[str],
        shortest_path: Dict[str, str],
        cyclic_edges: List[EDGE_WTIHOUT_WEIGHT]) -> None:

    prev_vertex: str = shortest_path.get(current_vertex)

    # Check to see whether there is a connecting vertex
    if prev_vertex:

        # If previous vertex is already in stack
        # Means we have completed a cycle
        if prev_vertex in current_stack:
            # We add the edge as (prev_vertex, current_vertex)
            # This is because an edge is determined by:
            #       edge: (src, dest)
            new_cyclic_edge: EDGE_WTIHOUT_WEIGHT = (
                prev_vertex, current_vertex)

            # Check whether we have found this cyclic edge before
            # Only append unique edges (ignore repeats)
            if new_cyclic_edge not in cyclic_edges:
                cyclic_edges.append(new_cyclic_edge)
        else:
            # If no cycle
            # We continue traversing to check further
            current_stack.append(prev_vertex)
            checkForCycle(
                current_vertex=prev_vertex,
                current_stack=current_stack,
                shortest_path=shortest_path,
                cyclic_edges=cyclic_edges
            )


def searchForCycle(shortestPathTree: Dict[str, str]) -> List[EDGE_WTIHOUT_WEIGHT]:
    """
    searchForCycle:
        - This function takes in the shortest path tree (output of bellmanFord), and returns a list containing edges (excluding the weights) involved in the negative cycle.
        - For instance, for exchange rates 1, it should return: [('SGD', 'GBP'), ('GBP', 'USD'), ('USD', 'SGD')]

    """

    cyclic_edges: List[EDGE_WTIHOUT_WEIGHT] = []

    vertex: str
    for vertex in shortestPathTree.keys():

        checkForCycle(
            current_vertex=vertex,
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
