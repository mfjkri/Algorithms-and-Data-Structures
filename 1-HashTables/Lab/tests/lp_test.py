
import sys
sys.path.append("")

from linear_probing import LPHashTable, hash


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


def getErrorColors(str):
    return color.YELLOW + str + color.END


def getSuccessColor(str):
    return color.GREEN + str + color.END


def testConstructor(table):
    print()
    print(color.BOLD + "TESTING CONSTRUCTOR" + color.END)
    print("Initialising LPHashTable, passing in argument of 5")

    try:
        table = LPHashTable(5)
        title = "Test 1: Table and size attribute exists | "
        errMessage = "Error: HashTable class has no attribute table or size"
        assert hasattr(table, "table") and hasattr(
            table, "size"), title + getErrorColors(errMessage)
        print(title + getSuccessColor("Passed"))

        title = "Test 2: Initial table capacity (array length) is 5 | "
        errMessage = "Error: Table attribute is not a list or it's length is not 5"
        assert isinstance(table.table, list) and len(
            table.table) == 5, title + color.YELLOW + errMessage + color.END
        print(title + color.GREEN + "Passed" + color.END)
        return True

    except Exception as e:
        print(e)
        return False


def testInsert(table):
    print()
    print(color.BOLD + "TESTING INSERT" + color.END)
    print(color.CYAN + "\nInserting")
    print('''----------------
Alice   | 98
Aaron   | 85
Brandon | 72
Ethan   | 81
Esther  | 82\n''' + color.END)

    try:
        title = "Test 1: Checking for Brandon | "
        errMessage = "Error: Indexing into Brandon (index 2) does not return HashItem('Brandon', 72)"

        brandon = table.table[2]
        assert hasattr(brandon, "key") and hasattr(
            brandon, "value"), title + color.YELLOW + errMessage + color.END
        assert brandon.key == "Brandon" and brandon.value == 72, title + \
            color.YELLOW + errMessage + color.END
        print(title + color.GREEN + "Passed" + color.END)

        title = "Test 2: Checking for Esther | "
        errMessage = title + color.YELLOW + \
            "Error: Indexing into Esther (index 3) does not return HashItem('Esther', 82)" + color.END

        esther = table.table[3]
        assert hasattr(esther, "key"), errMessage
        assert esther.key == "Esther" and esther.value == 82, errMessage
        print(title + color.GREEN + "Passed" + color.END)

        title = "Test 3: Checking that size attribute is 5 | "
        errMessage = title + color.YELLOW + "Error: Size attribute is not 5" + color.END
        assert table.size == 5, errMessage
        print(title + color.GREEN + "Passed" + color.END)

        print(color.CYAN + "\nInserting (Kevin, 92)\n" + color.END)
        table.insert("Kevin", 92)

        title = "Test 4: Checking that table length is now 10 due to resize (double the initial size)| "
        errMessage = title + color.YELLOW + \
            "Error: Table length (capacity) is not 10" + color.END
        assert len(table.table) == 10, errMessage
        print(title + color.GREEN + "Passed" + color.END)

        title = "Test 5: Checking for Kevin at index 3 (should have rehashed all items) | "
        errMessage = title + color.YELLOW + \
            "Error: Indexing into Kevin (index 3) does not return HashItem('Kevin', 92). Did you perform a rehash of items?" + color.END

        kevin = table.table[3]
        assert hasattr(kevin, "key"), errMessage
        assert kevin.key == "Kevin" and kevin.value == 92, errMessage
        print(title + color.GREEN + "Passed" + color.END)

        return True

    except Exception as e:
        print(e)
        return False


def testSearch(table):
    print()
    print(color.BOLD + "TESTING SEARCH" + color.END)

    try:

        title = "Test 1: Searching Esther | "
        errMessage = title + color.YELLOW + \
            "Error: Searching Esther does not return HashItem('Esther', 82)" + \
            color.END
        esther = table.search("Esther")

        assert hasattr(esther, "key") and hasattr(
            esther, "value") and esther.key == "Esther" and esther.value == 82, errMessage
        print(title + color.GREEN + "Passed" + color.END)

        title = "Test 2: Searching Jenn | "
        errMessage = title + color.YELLOW + \
            "Error: Searching Jenn does not return None" + color.END
        jenn = table.search("Jenn")
        assert jenn == None, errMessage
        print(title + color.GREEN + "Passed" + color.END)

        title = "Test 3: Searching Kevin | "
        errMessage = title + color.YELLOW + \
            "Error: Searching Kevin does not return HashItem('Kevin', 92)" + \
            color.END
        kevin = table.search("Kevin")
        assert hasattr(kevin, "key") and hasattr(
            kevin, "value") and kevin.key == "Kevin" and kevin.value == 92, errMessage
        print(title + color.GREEN + "Passed" + color.END)
        return True

    except Exception as e:
        print(e)
        return False


def testDelete(table):
    print()
    print(color.BOLD + "TESTING DELETE" + color.END)

    try:
        print(color.CYAN + 'Deleting Kevin' + color.END)
        table.delete("Kevin")
        title = "Test 1: Searching Kevin | "
        kevin = table.search("Kevin")
        errMessage = title + color.YELLOW + \
            "Error: Searching Kevin does not return None" + color.END
        assert kevin == None, errMessage

        errMessage = title + color.YELLOW + \
            f"Error: Table size should be 5, got {table.size}" + color.END
        assert table.size == 5, errMessage
        print(title + color.GREEN + "Passed" + color.END)

        print(color.CYAN + "Inserting ('Charlie', 91)" + color.END)
        table.insert("Charlie", 91)
        charlie = table.search("Charlie")

        title = "Test 2: Searching Charlie | "
        errMessage = title + color.YELLOW + \
            "Error: Searching Charlie does not return HashItem('Charlie', 91)" + \
            color.END
        charlie = table.search("Charlie")
        assert hasattr(charlie, "key") and hasattr(
            charlie, "value") and charlie.key == "Charlie" and charlie.value == 91, errMessage
        print(title + color.GREEN + "Passed" + color.END)
        return True

    except Exception as e:
        print(e)
        return False


def main():

    table = LPHashTable(5)

    if not testConstructor(table):
        return

    table.insert("Alice", 98)
    table.insert("Aaron", 85)
    table.insert("Brandon", 72)
    table.insert("Ethan", 81)
    table.insert("Esther", 82)

    if not testInsert(table):
        return

    if not testSearch(table):
        return

    if not testDelete(table):
        return

    print(color.BOLD + "\nALL TESTS SUCCESSFULLY PASSED" + color.END)


if __name__ == "__main__":
    main()
