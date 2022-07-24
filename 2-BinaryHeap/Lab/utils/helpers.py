# HELPER FUNCTIONS
def parent(index):
    return index // 2


def left(index):
    return index * 2


def right(index):
    return index * 2 + 1


class HeapItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({}, {})".format(self.key, self.value)
