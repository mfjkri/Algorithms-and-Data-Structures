import sys
import pathlib


scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from boyer import BoyerMoore, badCharHeuristic
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


def testBM(solution, text, substring):
    passed = True
    studentBCH = badCharHeuristic(substring)
    studentBM = BoyerMoore(text, substring)
    bch, bm = solution
    try:
        title = "Checking if bad char heuristic is correct | "
        errMessage = "Error: expected {}, got {}".format(bch, studentBCH)
        assert bch == studentBCH, title + yellowText(errMessage)
        print(title + greenText("Passed"))

    except Exception as e:
        print(e)
        passed = False
    
    try:
        title = "Checking if BoyerMoore results are correct | "
        errMessage = "Error: expected {}, got {}".format(bm, studentBM)
        assert bm == studentBM, title + yellowText(errMessage)
        print(title + greenText("Passed"))
        
    except Exception as e:
        print(e)
        passed = False
        
    return passed
        

def main():

    print()
    print(boldText("TESTING KMP"))
    texts = [
            "BANANA", 
            "AAAABBBBAAAABBBBAAAaBAABBAABABDTTT",
            "ABBAACABBAACABBAACABBAACABBAAC",
            "TTTTTTTSTTSTTTTT",
        ]
    substrings = [
            'ANA', 
            'AABBAA',
            "ABBAAC",
            "TTT",
        ]    
    
    solutions = [
        (
            {"A": 2, "N": 1}, [1, 3]
        ),
        ({"A": 5, "B": 3}, [21]),
        ({'A': 4, 'B': 2, 'C': 5}, [0, 6, 12, 18, 24]),
        ({'T': 2}, [0, 1, 2, 3, 4, 11, 12, 13]),
    ]
    
    for i in range(len(substrings)):
        print()
        print(boldText("Test {} | text: {}, string: {}".format(i + 1, texts[i], substrings[i])))

        if not testBM(solutions[i], texts[i], substrings[i]):
            return

    print(color.BOLD + "\nALL TESTS SUCCESSFULLY PASSED" + color.END)

if __name__ == "__main__":
    main()