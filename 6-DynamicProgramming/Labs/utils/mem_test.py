import sys
import pathlib


scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from memoization import fib, bestSum, longestCommonSubsequence
import signal


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


def redText(str):
    return color.RED + str + color.END


def boldText(str):
    return color.BOLD + str + color.END


class TimedOutExc(Exception):
    pass


def deadline(timeout, *args):
    def decorate(f):
        def handler(signum, frame):
            raise TimedOutExc()

        def new_f(*args):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(timeout)
            return f(*args)
            signal.alarm(0)

        new_f.__name__ = f.__name__
        return new_f
    return decorate


@deadline(4)
def testFib(solution, n):
    passed = True

    try:
        memo = {}
        studentAns = fib(n, memo)
        errMessage = "Error: expected {} , got {}".format(solution, studentAns)
        assert solution == studentAns, yellowText(errMessage)
        print(greenText("Passed"))

    except TimedOutExc:
        print(redText("Timeout"))
        print(yellowText("Error: Function took too long. Did you memoize your results?"))

    except Exception as e:
        print(redText("Failed"))
        print(e)
        passed = False

    return True


@deadline(4)
def testBestSum(solution, array, targetSum):
    try:
        studentAns = bestSum(array, targetSum, {})
        studentAns.sort()
        errMessage = "Error: expected {} (after sorting), got {} (after sorting)".format(
            solution, studentAns)
        assert solution == studentAns, yellowText(errMessage)
        print(greenText("Passed"))

    except TimedOutExc:
        print(redText("Timeout"))
        print(yellowText("Error: Function took too long. Did you memoize your results?"))
        return False

    except Exception as e:
        print(redText("Failed"))
        print(e)

    return True


@deadline(5)
def testLCS(solution, string1, string2):
    try:
        studentAns = longestCommonSubsequence(string1, string2, {})
        errMessage = "Error: expected {}, got {}".format(solution, studentAns)
        assert solution == studentAns, yellowText(errMessage)
        print(greenText("Passed"))

    except TimedOutExc:
        print(redText("Timeout"))
        print(yellowText("Error: Function took too long. Did you memoize your results?"))
        return False

    except Exception as e:
        print(redText("Failed"))
        print(e)

    return True


def main():

    print()
    print(boldText("TESTING FIB"))
    tests = [5, 10, 50]
    fibSolutions = [8, 89, 20365011074]

    for i, sol in enumerate(fibSolutions):
        print("Test {}: Fib {} | ".format(i + 1, tests[i]), end="")
        if not testFib(sol, tests[i]):
            break

    print()
    print(boldText("TESTING BEST SUM"))
    tests = [
        ([2, 4, 8], 10),
        ([4, 8, 9], 30),
        ([3, 4, 11, 8], 111),
        ([7, 3], 700),
    ]

    solutions = [
        [2, 8],
        [4, 8, 9, 9],
        [4, 8] + [11] * 9,
        [7] * 100,
    ]

    for i, sol in enumerate(solutions):
        print("Test {}: array {}, targetSum {} | ".format(
            i + 1, tests[i][0], tests[i][1]), end="")
        if not testBestSum(sol, tests[i][0], tests[i][1]):
            break

    print()
    print(boldText("TESTING LONGEST COMMON SUBSEQUENCE"))
    tests = [
        ("HELLO", "HOLLER"),
        ('jeffrey', 'refree'),
        ('8111111111111111142', '2222222228222222222222122222222433333333332'),
        ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
         'aaaaaaaaaaaaaaaaaa')
    ]

    solutions = [
        "HLL",
        "efre",
        "8142",
        "aaaaaaaaaaaaaaaaaa",
    ]
    for i, sol in enumerate(solutions):
        print("Test {}: string1 '{}', string2 '{}' | ".format(
            i + 1, tests[i][0], tests[i][1]), end="")
        if not testLCS(sol, tests[i][0], tests[i][1]):
            break

    # print(color.BOLD + "\nALL TESTS SUCCESSFULLY PASSED" + color.END)


if __name__ == "__main__":
    main()
