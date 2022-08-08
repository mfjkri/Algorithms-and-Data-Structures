import csv
from sys import argv
from typing import List, Dict, Counter, Deque
from collections import deque

INF = float("inf")


def shortestPaths(start: str, adjList: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    - This function takes in a user (vertex) and the adjacency list, and returns a dictionary for each shortest path that exists from that vertex to any other in the network. For instance, consider the following network:

    - For instance, for network5.csv, shortestPath("Ann", adjList) should return:
        {
                "Eve": [ "Kim" ],
                "Max": [ "Kim" ],
                "Luke": [ "Kim", "Eve" ]
        }
    - This dictionary should not include keys who the start has a direct edge to (e.g. "Kim") and keys who the start has no path to. 
    - When there are multiple shortest paths, always choose the one that has lower alphabetical order
    """

    # Create a queue
    queue: Deque = deque()

    # Keep track of which vertices have already been enqueued
    queue_history: List[str] = []

    # Keep track of the shortest path to each vertices
    shortest_paths: Dict[str, List[str]] = {}

    # Enqueue the start vertex and mark it as such
    queue.append(start)
    queue_history.append(start)

    # Keep going as long there the queue is not empty
    while queue:

        # Get the first guy on the queue (First In First Out)
        current_vertex: str = queue.popleft()

        # Sort all adjacent vertices of the current vertex by alphabetical order
        # This is to prioritize a path where the name is less in alphabetical order
        sorted_adj_vertices = sorted(adjList[current_vertex])

        for adj_vertex in sorted_adj_vertices:
            adj_vertex: str

            # If adjacent vertex has not been enqueued already
            if adj_vertex not in queue_history:

                # Enqueue adjacent vertex and mark is as such
                queue.append(adj_vertex)
                queue_history.append(adj_vertex)

                # Only create shortest path if its not start vertex
                if current_vertex != start:
                    # Shortest path to adjacent vertex is:
                    #   path to current vertex + current vertex
                    new_path = list(shortest_paths.get(current_vertex, list()))
                    new_path.append(current_vertex)
                    shortest_paths.update({adj_vertex: new_path})

    return shortest_paths


def betweennessCentrality(adjList: Dict[str, List[str]]) -> Dict[str, int]:
    """
    betweennessCentrality 

        - This function takes in the adjacency list and returns a dictionary where each vertex is a key and it's betweenness centrality is the value
        - It should make use of the shortestPaths function
        - For instance: betweennessCentrality(adjList) for the above network should return: {'Ann': 0, 'Kim': 3, 'Eve': 2, 'Max': 0, 'Luke': 0}
    """

    # Create a counter object
    centrality_counter = Counter()

    # Initialize each vertex count in the counter to 0
    for vertex in adjList.keys():
        centrality_counter[vertex] = 0

    for vertex in adjList.keys():

        # Get all the shortest paths from the vertex to all other connected vertices
        shortest_paths = shortestPaths(start=vertex, adjList=adjList)

        for _, path in shortest_paths.items():

            for vertex_path in path:
                vertex_path: str

                # Increment the count of the vertex by 1
                centrality_counter[vertex_path] += 1

    # Convert the counter object to a dictionary to match expected output
    return dict(centrality_counter)


'''
    - In main, we help you to read from the csv file, through a command line argument, and create the adjacency list for the edges. This is stored in a dictionary where each key is a vertex in the network and value is a list of edges for that vertex. 
    - To test, for instance, network5.csv, you may run `python centrality.py network5.csv`
'''


def main():

    if len(argv) < 2:
        print("Require network file to load edges")
        return

    adjList = {}
    with open("networks/" + argv[1], "r") as csv_file:
        myReader = csv.reader(csv_file)
        for row in myReader:
            u, v = row[0], row[1]
            if u not in adjList:
                adjList[u] = []
            if v not in adjList:
                adjList[v] = []
            adjList[u].append(v)

    print(betweennessCentrality(adjList))


if __name__ == "__main__":
    main()
