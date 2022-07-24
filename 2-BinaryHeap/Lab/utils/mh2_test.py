import sys
import pathlib

scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from min_heap2 import MinHeap
from utils.helpers import HeapItem


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


def testConstructor(minHeap):

    print()
    print(boldText("TESTING CONSTRUCTOR"))
    print(cyanText("Initialising MinHeap2 with maxsize of 5"))

    try:
        title = "Test 1: MinHeap2 has correct attributes | "
        errMessage = '''Error: MinHeap2 class has incorrect attributes. Does it have heap, size, maxsize & positions attributes? 
        (make sure to spell these correctly as autograder will detect spelling errors as errors)'''

        assert (hasattr(minHeap, "heap")
                and hasattr(minHeap, "size")
                and hasattr(minHeap, "maxsize")
                and hasattr(minHeap, "positions")
                ), title + yellowText(errMessage)
        print(title + greenText('Passed'))

        title = "Test 2: heap length is 6 (maxsize + 1) | "
        errMessage = '''Error: heap attribute is not a list or it's length is not 6
        (Note: heap length should be maxsize + 1 because items are inserted starting from index 1)'''
        assert isinstance(minHeap.heap, list) and len(
            minHeap.heap) == 6, title + yellowText(errMessage)
        print(title + greenText("Passed"))
        return True
    except Exception as e:
        print(e)
        return False


def testInsert(minHeap):

    print()
    print(boldText("TESTING INSERT"))
    print(color.CYAN + "\nInserting")
    print('''----------------
Key       | Value
Google    | 30
Facebook  | 62
Netflix   | 25
Amazon    | 42
Apple     | 15\n''' + color.END)

    try:

        title = "Test 1: Testing heap order is correct | "
        order = [
            None,
            HeapItem("Apple", 15),
            HeapItem("Netflix", 25),
            HeapItem("Google", 30),
            HeapItem("Facebook", 62),
            HeapItem("Amazon", 42),
        ]

        for i in range(1, 6):
            errMessage = "Error: Heap position {} should be {}, got {}".format(
                i, order[i], minHeap.heap[i])
            assert (
                isinstance(minHeap.heap[i], HeapItem)
                and order[i].key == minHeap.heap[i].key
                and order[i].key == minHeap.heap[i].key
            ), title + yellowText(errMessage)

        print(title + greenText("Passed"))

        title = "Test 2: Testing heap size | "
        errMessage = "Error: size attribute should be 5"
        assert minHeap.size == 5, title + yellowText(errMessage)
        print(title + greenText('Passed'))

        print(color.CYAN + "\nReplacing Keys")
        print('''----------------
Key       | Value
Google    | 50
Facebook  | 49
Apple     | 30\n''' + color.END)
        minHeap.insert("Google", 50)
        minHeap.insert("Facebook", 49)
        minHeap.insert("Apple", 30)

        title = "Test 3: Testing heap size remains at 5 | "
        errMessage = "Error: size attribute should be 5"
        assert minHeap.size == 5, title + yellowText(errMessage)
        print(title + greenText('Passed'))

        title = "Test 4: Testing keys changed correctly | "
        order = [
            None,
            HeapItem("Netflix", 25),
            HeapItem("Apple", 30),
            HeapItem("Google", 50),
            HeapItem("Facebook", 49),
            HeapItem("Amazon", 42),
        ]

        for i in range(1, 6):
            errMessage = "Error: Heap position {} should be {}, got {}".format(
                i, order[i], minHeap.heap[i])
            assert (
                isinstance(minHeap.heap[i], HeapItem)
                and order[i].key == minHeap.heap[i].key
                and order[i].key == minHeap.heap[i].key
            ), title + yellowText(errMessage)

        print(title + greenText("Passed"))
        return True

    except Exception as e:
        print(e)
        return False


def testGetMin(minHeap):
    print()
    print(boldText('TESTING REMOVE MIN'))

    try:
        order = [
            HeapItem("Netflix", 25),
            HeapItem("Apple", 30),
            HeapItem("Amazon", 42),
            HeapItem("Facebook", 49),
            HeapItem("Google", 50),
        ]

        title = "Test 1: Extracting min x5 | "
        for i in range(5):
            print(cyanText("Extracting min"))
            item = minHeap.removeMin()
            errMessage = "Min item should be {}, got {}".format(order[i], item)
            assert (
                isinstance(item, HeapItem)
                and item.key == order[i].key
                and item.value == order[i].value
            ), title + yellowText(errMessage)
        print(title + greenText("Passed"))

        print(cyanText("Extracting min"))
        item = minHeap.removeMin()
        title = "Test 2: Extracting min when heap is empty | "
        errMessage = "Error: Extracting min should return None and size attribute should be 0"
        assert item == None and minHeap.size == 0, title + \
            yellowText(errMessage)
        print(title + greenText("Passed"))

        return True
    except Exception as e:
        print(e)
        return False


def main():

    minHeap = MinHeap(5)

    if not testConstructor(minHeap):
        return

    minHeap.insert("Google", 30)
    minHeap.insert("Facebook", 62)
    minHeap.insert("Netflix", 25)
    minHeap.insert("Amazon", 42)
    minHeap.insert("Apple", 15)

    if not testInsert(minHeap):
        return

    if not testGetMin(minHeap):
        return

    print(color.BOLD + "\nALL TESTS SUCCESSFULLY PASSED" + color.END)


if __name__ == "__main__":
    main()
