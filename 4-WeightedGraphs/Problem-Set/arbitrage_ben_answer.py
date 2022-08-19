from time import time
from exchangeRates import exchangeRates
from sys import argv
import math

INF = 10000.0


def arbitrage(exchangeRates):

    # CONVERT EXCHANGE RATES TO LOG GRAPH
    logGraph = convertToLogGraph(exchangeRates)

    # RETRIEVES SHORTEST PATH TREE / NONE THROUGH BELLMAN FORD ALGO
    shortestPathTree = bellmanFord(logGraph)
    print(shortestPathTree)

    # RETRIEVES EDGES INVOLVED IN CYCLE IF THERE IS ONE
    return searchForCycle(shortestPathTree)


'''
convertToLogGraph:
    - This function takes in a graph of exchange rates, and returns an adjacency list with the same edges, but with every weight having the negative log10 function applied
'''


def convertToLogGraph(exchangeRates):
    exchangeRates = dict(exchangeRates)
    for from_rate, to_lists in exchangeRates.items():
        exchangeRates[from_rate] = [(x[0], x[1], -math.log(x[2], 10))
                                    for x in to_lists]
    return exchangeRates


'''
bellmanFord:
    - This function will take in the logGraph (output of convertToLogGraph function), and returns the shortest path tree
    - The shortest path tree is essentially an adjacent list made up of the edges involved in the edgeTo list.
'''


def bellmanFord(logGraph):
    start = list(logGraph.keys())[0]

    distTo = {k: 999999 for k in logGraph.keys()}
    edgeTo = {k: None for k in logGraph.keys()}
    distTo[start] = 0

    for start_node in logGraph:
        print("starting node", start_node)
        for src_key, dests in logGraph.items():
            print("edgeList", dests)
            for src, dest, weight in dests:
                dist = distTo[src] + weight
                if dist < distTo[dest]:
                    distTo[dest] = dist
                    edgeTo[dest] = (src, dest, weight)

    print("edgeTo", edgeTo)
    return_dict = {}
    for v in edgeTo:
        if edgeTo[v]:
            if edgeTo[v][0] not in return_dict:
                return_dict[edgeTo[v][0]] = []
            if edgeTo[v][1] not in return_dict:
                return_dict[edgeTo[v][1]] = []
            return_dict[edgeTo[v][0]].append(edgeTo[v])
    return return_dict


'''
searchForCycle:
    - This function takes in the shortest path tree (output of bellmanFord), and returns a list containing edges (excluding the weights) involved in the negative cycle.
    - For instance, for exchange rates 1, it should return: [('SGD', 'GBP'), ('GBP', 'USD'), ('USD', 'SGD')]

'''


def searchForCycle(shortestPathTree):
    for start_node in shortestPathTree:
        stack = []
        traversal = []
        dist = 0

        for edge in shortestPathTree[start_node]:
            stack.append(edge)

        while len(stack) > 0:
            last_edge = stack.pop()
            # print(last_edge)
            # print(stack)
            traversal.append((last_edge[0], last_edge[1]))
            dist += last_edge[2]
            if last_edge[1] in [x[0] for x in traversal] and dist < 0:
                return traversal

            add = False
            if last_edge[1] in shortestPathTree:
                for edge in shortestPathTree[last_edge[1]]:
                    add = True
                    stack.append(edge)
            # print(stack)
            # print('-' * 5)

            if not add:
                traversal.pop()
                dist -= last_edge[2]
    return []


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
