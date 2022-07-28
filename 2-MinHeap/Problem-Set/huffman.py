from collections import Counter
from typing import Dict, Union

from heap import MinHeap


class TreeNode:
    def __init__(self, char: str, frequency: int, left=None, right=None):
        self.char: str = char
        self.frequency: int = frequency
        self.left: Union[TreeNode, None] = left
        self.right: Union[TreeNode, None] = right

    def __str__(self) -> str:
        return f"{self.char}, {self.frequency}, {self.left}, {self.right}"


def calculateFrequencies(data: str) -> Dict[str, int]:
    """
        calculateFrequencies:
            - This function takes in the data string and returns a dictionary which 
            contains each character in the string as keys and it's frequency as the value
    """

    return dict(Counter(data))


def createHuffmanTree(charFrequencies: Dict[str, int]) -> TreeNode:
    """
    createHuffmanTree:
        - This function takes in char frequencies and inserts each character as a TreeNode 
        into a MinPQ sorted according to character frequency
        - Then, while the PQ has more than one item:
            -> Extract the 2 min nodes and create a new tree node where its 
            left is the node with smallest frequency and right is the node with second smallest frequency
            -> Insert the new node back into the priority queue
        - Once the tree has been build, this function should return the root node of the tree as a TreeNode
    """

    min_priority_queue = MinHeap(maxsize=len(charFrequencies.values()))

    for char, frequency in charFrequencies.items():
        char: str
        frequency: int

        new_node = TreeNode(
            char=char,
            frequency=frequency
        )

        min_priority_queue.insert(
            newKey=new_node,
            newValue=frequency
        )

    while min_priority_queue.size > 1:

        left_node: TreeNode = min_priority_queue.getMin().key
        right_node: TreeNode = min_priority_queue.getMin().key

        new_node = TreeNode(
            char="",
            frequency=left_node.frequency + right_node.frequency,
            left=left_node,
            right=right_node
        )

        min_priority_queue.insert(
            newKey=new_node,
            newValue=new_node.frequency
        )

    root_node: TreeNode = min_priority_queue.getMin().key
    return root_node


def traverseTree(node: TreeNode, current_code: str, codes: Dict[str, str]) -> None:
    if node.char:
        codes.update({node.char: current_code})

    if node.left:
        traverseTree(
            node=node.left,
            current_code=current_code + '0',
            codes=codes
        )

    if node.right:
        traverseTree(
            node=node.right,
            current_code=current_code + '1',
            codes=codes
        )


def calculateCodes(huffmanRoot: TreeNode) -> Dict[str, str]:
    """
    calculateCodes:
        - This function takes in the root node from the Huffman tree
        - It should traverse the tree, and determine the code for each character in the string:
            -> A left path is considered '0'
            -> A right path is considered '1'
            -> Traverse a tree until you find a leaf node, and that character's code will be its path. 
            -> For instance, to get to C, we first go right, then left. Thus, C's code will be '10'
        - This function should should return a dictionary with each character as keys and it's code as the value
    """

    codes = {}

    traverseTree(
        node=huffmanRoot,
        # in the event our root node is not a wildcard node
        # this occurs when the input string only has 1 unique char
        current_code='' if not huffmanRoot.char else '0',
        codes=codes
    )

    return codes


def encodeString(data: str, codes: Dict[str, str]) -> str:
    """
    encodeString(data, codes):
        - This function takes in the original string (data) and the dictionary of codes for each char
        - It should return the string with each character replaced with its corresponding code
        - E.g. If we have:
            -> codes = {'A': '0', 'C': '10', 'B': '11'}
            -> message = "AAABBC"
            Our encoded string will be: "000111110"
    """

    return "".join([codes[char] for char in data])


def HuffmanEncoding(data):

    # 1. Determine frequencies of characters
    charFrequencies = calculateFrequencies(data)

    # 2. Build Huffman tree
    huffmanRoot = createHuffmanTree(charFrequencies)

    # 3. Traverse Huffman tree to determine code for each char
    codes = calculateCodes(huffmanRoot)
    print("codes:", codes)

    # 4. Build encoded string using codes
    encodedOutput = encodeString(data, codes)

    return encodedOutput, huffmanRoot


def main():

    data = input('input a string to encode via huffman: ')
    encoded_output, _ = HuffmanEncoding(data)

    print('encoded data:', encoded_output)
    print('space usage before compression:', len(data) * 8)
    print('space usage after compression:', len(encoded_output))


if __name__ == '__main__':
    main()
