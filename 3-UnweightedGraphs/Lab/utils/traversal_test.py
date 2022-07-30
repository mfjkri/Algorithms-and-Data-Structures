import sys
import pathlib
from typing import Callable


scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from traversal import dfs, bfs, norecurse_dfs
from utils.helpers import Graph


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


def testDFS_with_function(graph, dfs_callback: Callable, dfs_implementation_type: str):
    print(boldText(f"TESTING DFS({dfs_implementation_type})"))

    try:
        title = f"Test 1: DFS starting from vertex 0 | "
        answer = [0, 1, 4, 2, 3, 5]
        studentAnswer = dfs_callback(graph, 0)
        errMessage = "Expected: {}, Got: {}".format(answer, studentAnswer)
        assert studentAnswer == answer, title + yellowText(errMessage)
        print(title + greenText('Passed'))

        title = f"Test 2: DFS starting from vertex 3 | "
        answer = [3, 0, 1, 4, 2, 5]
        studentAnswer = dfs_callback(graph, 3)
        errMessage = "Expected: {}, Got: {}".format(answer, studentAnswer)
        assert studentAnswer == answer, title + yellowText(errMessage)
        print(title + greenText('Passed'))

        title = f"Test 3: DFS starting from vertex 6 | "
        answer = [6]
        studentAnswer = dfs_callback(graph, 6)
        errMessage = "Expected: {}, Got: {}".format(answer, studentAnswer)
        assert studentAnswer == answer, title + yellowText(errMessage)
        print(title + greenText('Passed'))

        return True

    except Exception as e:
        print(e)
        return False


def testDFS(graph):
    successA = testDFS_with_function(graph, dfs_callback=dfs,
                                     dfs_implementation_type="recursive")

    print()

    successB = testDFS_with_function(graph, dfs_callback=norecurse_dfs,
                                     dfs_implementation_type="iterative")

    return successA and successB


def testBFS(graph):
    print()
    print(boldText("TESTING BFS"))

    try:
        title = "Test 1: BFS starting from vertex 0 | "
        answer = [0, 1, 3, 5, 4, 2]
        studentAnswer = bfs(graph, 0)
        errMessage = "Expected: {}, Got: {}".format(answer, studentAnswer)
        assert studentAnswer == answer, title + yellowText(errMessage)
        print(title + greenText('Passed'))

        title = "Test 2: BFS starting from vertex 3 | "
        answer = [3, 0, 1, 2, 5, 4]
        studentAnswer = bfs(graph, 3)
        errMessage = "Expected: {}, Got: {}".format(answer, studentAnswer)
        assert studentAnswer == answer, title + yellowText(errMessage)
        print(title + greenText('Passed'))

        title = "Test 3: BFS starting from vertex 6 | "
        answer = [6]
        studentAnswer = bfs(graph, 6)
        errMessage = "Expected: {}, Got: {}".format(answer, studentAnswer)
        assert studentAnswer == answer, title + yellowText(errMessage)
        print(title + greenText('Passed'))

        return True

    except Exception as e:
        print(e)
        return False


def main():

    V = 7
    graph = Graph(V)

    edges = [(0, 1), (0, 3), (0, 5), (1, 4), (4, 2), (1, 3), (3, 2)]
    for edge in edges:
        graph.addEdge(edge)

    print(color.CYAN + color.BOLD + '''
Initialising Undirected Graph:
0 ----- 1       |
| \   /   \     |
|  \ /     \    |
5   3 - 2 - 4   |
  6             |
''' + color.END)

    if not testDFS(graph):
        return

    if not testBFS(graph):
        return

    print(color.BOLD + "\nALL TESTS SUCCESSFULLY PASSED" + color.END)


if __name__ == "__main__":
    main()
