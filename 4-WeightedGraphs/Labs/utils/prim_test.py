import sys
import pathlib

scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from prim import LazyPrimMST
from utils.helpers import WeightedEdge, WeightedGraph


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
    str = "[ "
    for i, edge in enumerate(edges):

        if (isinstance(edge, WeightedEdge)):
            # str += "{}: {} - {}, {} | ".format(i + 1, edge.src, edge.dest, edge.weight)
            str += "WEdge({}, {}, {})".format(edge.src, edge.dest, edge.weight)
        else:
            str += "{}".format(i + 1, edge)

        if i != len(edges) - 1:
            str += ", "
        else:
            str += " ]"
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


def testPrim(graph, solution):

    try:
        studentAnswer = LazyPrimMST(graph)
        assert isinstance(studentAnswer, list), yellowText(
            "PrimMST should return a list, instead got type {}".format(type(studentAnswer)))

        isSame = True
        for i in solution:

            found = False

            for j in studentAnswer:
                if edgesAreEqual(i, j):
                    found = True
                    break

            if not found:
                isSame = False
                break

        errMessage = "Expected: {}\nGot:      {}".format(
            printSolution(solution), printSolution(studentAnswer))

        if not isSame:
            print(yellowText(errMessage))
            return False
        else:
            return True

    except Exception as e:
        print(e)
        return False


def main():

    print()
    print(boldText("TESTING LAZY PRIM"))
    print()

    V = [5, 6, 7]

    edges = [
        [(0, 1, 5), (0, 4, 2), (0, 3, 12), (2, 3, 4), (2, 0, 7), (3, 1, 10)],
        [(0, 1, 22), (0, 5, 16), (0, 3, 11),
         (1, 4, 2), (1, 3, 13), (2, 5, 6), (5, 4, 3)],
        [(0, 1, 20), (0, 2, 10), (0, 3, 25), (1, 2, 5), (1, 4, 12),
         (2, 5, 14), (3, 5, 30), (4, 5, 6), (4, 6, 11)]
    ]

    solutions = [
        [WeightedEdge(0, 4, 2), WeightedEdge(0, 1, 5),
         WeightedEdge(2, 0, 7), WeightedEdge(2, 3, 4)],
        [WeightedEdge(0, 3, 11), WeightedEdge(1, 3, 13), WeightedEdge(
            1, 4, 2), WeightedEdge(4, 5, 3), WeightedEdge(2, 5, 6)],
        [WeightedEdge(0, 2, 10), WeightedEdge(1, 2, 5), WeightedEdge(1, 4, 12), WeightedEdge(4, 5, 6),
         WeightedEdge(4, 6, 11), WeightedEdge(0, 3, 25)],
    ]

    for i in range(3):

        print("TEST {}".format(i + 1))
        print("-" * 30)

        graph = WeightedGraph(V[i])
        for edge in edges[i]:
            src, dest, weight = edge
            graph.addEdge(src, dest, weight)

        print(color.CYAN + "Initialising graph with {} vertices, adjacency list: ".format(i + 5))
        graph.printGraph()
        print(color.END)

        if not testPrim(graph, solutions[i]):
            return
        print(greenText("Passed\n"))

    print(color.BOLD + "\nALL TESTS SUCCESSFULLY PASSED" + color.END)


if __name__ == "__main__":
    main()
