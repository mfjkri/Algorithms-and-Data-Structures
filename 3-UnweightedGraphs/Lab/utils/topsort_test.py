import sys
import pathlib


scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from topsort import topsort
from utils.helpers import Digraph


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


def testTopSort(graph):

    try:
        title = "Test 1: Top sort on graph 1 | "

        answers = [
            [0, 3, 5, 2, 1, 4, 6],
            [5, 0, 6, 3, 2, 1, 4],
            [0, 5, 6, 3, 2, 1, 4],
            [0, 3, 5, 2, 1, 6, 4],
            [5, 0, 3, 2, 1, 4, 6]
        ]
        studentAnswer = topsort(graph)
        errMessage = "Expected: one of the following:"
        for i in answers:
            errMessage += '\n     ' + str(i)
        errMessage += '\nGot: ' + str(studentAnswer)

        success = False
        for i in answers:
            if studentAnswer == i:
                success = True
        assert success, title + yellowText(errMessage)

        print(title + greenText('Passed'))
        return True

    except Exception as e:
        print(e)
        return False


def testCycle(digraph):
    try:
        title = "Test 2: Top sort on graph 2 | "
        studentAnswer = topsort(digraph)
        errMessage = "Expected None (Cycle detected), Got: {}".format(
            studentAnswer)
        assert studentAnswer == None, title + yellowText(errMessage)
        print(title + greenText('Passed'))

        return True

    except Exception as e:
        print(e)
        return False


def main():
    print(boldText("TESTING TOP SORT"))
    V = 7
    digraph = Digraph(V)
    edges = [(0, 3), (0, 6), (5, 6), (5, 2), (5, 4), (3, 2), (2, 1), (1, 4)]

    for edge in edges:
        digraph.addEdge(edge)

    print(color.CYAN + color.BOLD + '''
Initialising Directed Graph 1:

0 ------> 3         
|         |
⌄         ⌄   
6 <- 5 -> 2 -> 1
     |         |
     |         ⌄   
     --------> 4   
              
''' + color.END)

    if not testTopSort(digraph):
        return

    # --------
    print(color.CYAN + color.BOLD + '''
Initialising Directed Graph 2 (With Cycle):

0 ------> 3         
⌃         |
|         ⌄   
6 <------ 2 ------> 1
          |         |
          |         ⌄   
          --------> 4   
              
''' + color.END)
    V = 7
    digraph = Digraph(V)
    edges = [(0, 3), (3, 2), (2, 6), (6, 0), (2, 1), (1, 4), (2, 4)]

    for edge in edges:
        digraph.addEdge(edge)

    if not testCycle(digraph):
        return

    print(color.BOLD + "\nALL TESTS SUCCESSFULLY PASSED" + color.END)


if __name__ == "__main__":
    main()
