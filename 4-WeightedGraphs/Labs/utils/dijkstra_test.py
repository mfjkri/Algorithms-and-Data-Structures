import sys
import pathlib


scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from dijkstra import DijkstraSP
from utils.helpers import WeightedDigraph, WeightedEdge


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def greenText(str):
    return color.GREEN + str + color.END


def cyanText(str):
    return color.CYAN + str + color.END


def yellowText(str):
    return color.YELLOW + str + color.END


def boldText(str):
    return color.BOLD + str + color.END


def printSolution(edges):
    str = "| "
    for i, edge in enumerate(edges):
        if (isinstance(edge, WeightedEdge)):
            # str += "{}: {} - {}, {} | ".format(i + 1, edge.src, edge.dest, edge.weight)
            str += "{}: WEdge({}, {}, {}) | ".format(i + 1,
                                                     edge.src, edge.dest, edge.weight)
        else:
            str += "{}: {} | ".format(i + 1, edge)
    return str


def edgesAreEqual(first, other):
    if not (
        hasattr(other, "src")
        and hasattr(other, "dest")
        and hasattr(other, "weight")
    ):
        return False

    return (
        ((first.src == other.src and first.dest == other.dest)
         or (first.src == other.dest and first.dest == other.src))
        and first.weight == other.weight
    )


def printDists(dists):
    str = ""
    for i, dist in enumerate(dists):
        if i != len(dists):
            str += "{}: {}, ".format(i + 1, dist)
        else:
            str += "{}: {}".format(i + 1, dist)
    return str


def testDijkstra(graph, solution):
    print(cyanText("Running dijkstra, starting from vertex 0"))

    try:

        studentAnswer = DijkstraSP(graph, 0)

        if solution == False:
            title = "Passing graph with negative weight edges into function | "
            assert studentAnswer == False, title + \
                yellowText(
                    "Function should return False, got {}".format(studentAnswer))
            return True

        if not isinstance(studentAnswer, tuple) or len(studentAnswer) != 2:
            print(yellowText("Error: should return two lists, edgeTo & distTo"))
            return False

        studentEdge, studentDist = studentAnswer

        title = "Checking if edgeTo & distTo are lists | "
        assert isinstance(studentEdge, list) and isinstance(
            studentDist, list), title + yellowText("edgeTo & distTo should be lists")
        print(title + greenText("Passed"))

        title = "Checking length of edgeTo & distTo | "
        assert (len(studentEdge) == len(solution[0])
                and len(studentDist) == len(solution[1])), title + yellowText("edgeTo & distTo should be length {}".format(len(solution[0])))
        print(title + greenText("Passed"))
        title = "Checking edgeTo list | "

        errMessage = (
            color.RED
            + 'Failed\n'
            + color.YELLOW
            + "Expected: {}\nGot:      {}".format(printSolution(solution[0][1:]), printSolution(studentEdge[1:])) + color.END)

        for i in range(1, len(solution[0])):

            if solution[0][i] == None and isinstance(studentEdge[i], WeightedEdge):
                print(title + errMessage)
                return False
            elif solution[0][i] == None:
                break
            if not edgesAreEqual(solution[0][i], studentEdge[i]):
                print(title + errMessage)
                return False

        print(title + greenText("Passed"))

        title = "Checking distTo list | "

        for i in range(1, len(solution[1])):
            if solution[1][i] == None:
                continue
            if studentDist[i] != solution[1][i]:
                errMessage = (
                    color.RED
                    + 'Failed\n'
                    + color.YELLOW
                    + "Expected {}\nGot      {}".format(printDists(solution[1][1:]), printDists(studentDist[1:])) + color.END)
                print(title + errMessage)
                return False

        print(title + greenText("Passed"))
        return True

    except Exception as e:
        print(e)
        return False


def main():

    print()
    print(boldText("TESTING DIJKSTRA"))
    print()

    V = [
        6,
        7,
        8
    ]

    edges = [
        [(0, 1, 22), (0, 5, 16), (0, 3, 11),
         (1, 4, 2), (1, 3, 13), (2, 5, 6), (5, 4, 3)],
        [(0, 1, 12), (0, 3, 16), (0, 6, -11), (6, 2, 20), (2, 3, 32),
         (3, 0, 8), (5, 2, 3), (4, 1, 13), (1, 5, 12), (3, 4, 5)],
        [(0, 1, 20), (0, 2, 10), (0, 3, 25), (2, 1, 5), (3, 2, 7), (5, 3, 30),
         (2, 5, 35), (4, 5, 6), (1, 4, 12), (5, 6, 3), (6, 7, 4), (5, 7, 8)]
    ]

    solution1 = (
        [-1, WeightedEdge(0, 1, 22), None, WeightedEdge(0, 3, 11),
         WeightedEdge(5, 4, 3), WeightedEdge(0, 5, 16)],
        [0, 22, None, 11, 19, 16]
    )

    solution2 = False

    solution3 = (
        [-1, WeightedEdge(2, 1, 5), WeightedEdge(0, 2, 10), WeightedEdge(0, 3, 25), WeightedEdge(
            1, 4, 12), WeightedEdge(4, 5, 6), WeightedEdge(5, 6, 3), WeightedEdge(6, 7, 4)],
        [0, 15, 10, 25, 27, 33, 36, 40]
    )

    solutions = [solution1, solution2, solution3]

    for i in range(len(solutions)):
        print()
        print("TEST {}".format(i + 1))
        print("-" * 30)

        graph = WeightedDigraph(V[i])
        for edge in edges[i]:
            src, dest, weight = edge
            graph.addEdge(src, dest, weight)

        print(color.CYAN + "Initialising graph with {} vertices, adjacency list: ".format(len(graph.adjList)))
        graph.printGraph()
        print(color.END)

        if not testDijkstra(graph, solutions[i]):
            return

    print(color.BOLD + "\nALL TESTS SUCCESSFULLY PASSED" + color.END)


if __name__ == "__main__":
    main()
