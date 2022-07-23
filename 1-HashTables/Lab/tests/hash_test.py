import sys
sys.path.append("")

from hash_table import HashTable, hash


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


def testConstructor(table):
    print()
    print(color.BOLD + "TESTING CONSTRUCTOR" + color.END)
    try:
        title = "Test 1: Table attribute exists | "
        errMessage = "Error: HashTable class has no attribute table"

        assert hasattr(table, "table"), title + \
            color.YELLOW + errMessage + color.END
        print(title + color.GREEN + "Passed" + color.END)

        title = "Test 2: Table length is 26 | "
        errMessage = "Error: Table attribute is not a list or it's length is not 26"

        assert isinstance(table.table, list) and len(
            table.table) == 26, title + color.YELLOW + errMessage + color.END
        print(title + color.GREEN + "Passed" + color.END)
        return True
    except Exception as e:
        print(e)
        return False


def testInsert(table):
    print()
    print(color.BOLD + "TESTING INSERT" + color.END)
    print("\nInserting")
    print("----------------\nJeff    | 80\nAlice   | 98\nCharles | 72\nDaniel  | 81\nDarren  | 82\n%%      | 82 (error)\ná       | 82 (error)")
    try:
        table.insert("Jeff", 80)
        table.insert("Alice", 98)
        table.insert("Charles", 72)
        table.insert("Daniel", 81)
        table.insert("Darren", 82)
        table.insert("%%", None)
        table.insert("á (out of range)", None)

        title = "Test 1: Checking for Jeff | "
        errMessage = "Error: Indexing into Jeff does not return HashItem('Jeff', 80)"

        jeff = table.table[hash("Jeff")]
        assert hasattr(jeff, "key") and hasattr(
            jeff, "value"), title + color.YELLOW + errMessage + color.END
        assert jeff.key == "Jeff" and jeff.value == 80, title + \
            color.YELLOW + errMessage + color.END
        print(title + color.GREEN + "Passed" + color.END)

        title = "Test 2: Checking for Darren | "
        errMessage = title + color.YELLOW + \
            "Error: Indexing into Darren does not return HashItem('Darren', 82). Did you replace Daniel?" + color.END

        darren = table.table[hash("Darren")]
        assert hasattr(darren, "key"), errMessage
        assert darren.key == "Darren" and darren.value == 82, errMessage
        print(title + color.GREEN + "Passed" + color.END)
        return True
    except Exception as e:
        print(color.YELLOW + "Error: " + str(e) + color.END)
        return False


def testSearch(table):
    print()
    print(color.BOLD + "TESTING SEARCH" + color.END)

    try:

        title = "Test 1: Searching Charles | "
        errMessage = title + color.YELLOW + \
            "Error: Searching Charles does not return HashItem('Charles', 72)" + \
            color.END
        charles = table.search("Charles")
        assert hasattr(charles, "key") and hasattr(
            charles, "value") and charles.key == "Charles" and charles.value == 72, errMessage
        print(title + color.GREEN + "Passed" + color.END)

        title = "Test 2: Searching Daniel | "
        errMessage = title + color.YELLOW + \
            "Error: Searching Daniel does not return None" + color.END
        daniel = table.search("Daniel")
        assert daniel == None, errMessage
        print(title + color.GREEN + "Passed" + color.END)
        return True
    except Exception as e:
        print(e)
        return False


def main():

    table = HashTable()

    if not testConstructor(table):
        return

    if not testInsert(table):
        return

    if not testSearch(table):
        return

    print(color.BOLD + "\nALL TESTS SUCCESSFULLY PASSED" + color.END)


if __name__ == "__main__":
    main()
