from typing import List, Dict, Set

NO_OF_CHARS = 256

"""
1: The number of unique characters is given in a constant variable. Do make use of this to initialise your 2D list!
2: To convert a character to it's ASCII number, you can use the ord() function in python, and to convert from it, you can use the chr() function

ord('A') # convert char to ascii number: 65
chr(65)  # convert ascii number to char: 'A'
"""


def printDFA(finite_automata: List[List[int]], chars: Set[int]) -> None:
    for index, row in enumerate(finite_automata):
        if index in chars:
            print(chr(index), row)


def buildDFA(substring) -> List[List[int]]:
    """
        - This function takes in a substring and builds the appropriate finite automata for the KMP string matching algorithm
        - It should return the DFA as a 2D list, with 256 rows (number of ASCII characters) and M (length of substring) + 1 columns, which is the number of states
        - All values in rows of chars not in the substring should be 0
    """

    substring_length: int = len(substring)

    chars_in_substring: Set[int] = set()
    dfa: List[List[int]] = [
        [0] * (substring_length + 1) for _ in range(NO_OF_CHARS)
    ]

    substring_states: Dict[str, int] = {}

    for index, ascii_char in enumerate(substring):
        char: int = ord(ascii_char)

        chars_in_substring.add(char)
        dfa[char][index] = index + 1

    for char in chars_in_substring:
        for j in range(1, substring_length + 1):
            # Only set those that aren't already set
            if dfa[char][j] == 0:
                sub_pattern: str = substring[1:j]
                current_state: int = 0

                if sub_pattern in substring_states:
                    current_state = substring_states.get(sub_pattern)
                else:
                    # Find the "current" state for the sub_pattern in substring
                    sub_char_ascii: str
                    for sub_char_ascii in sub_pattern:

                        sub_char: int = ord(sub_char_ascii)
                        current_state = dfa[sub_char][current_state]

                    substring_states.update({sub_pattern: current_state})

                # Transition current_state with current char
                new_state = dfa[char][current_state]
                dfa[char][j] = new_state

    # printDFA(finite_automata=finite_automata, chars=chars)
    return dfa


def KnuthMorrisPratt(text, substring):
    dfa = buildDFA(substring)
    i = 0
    j = 0
    M = len(substring)

    while (i < len(text)):
        charIndex = ord(text[i])
        j = dfa[charIndex][j]
        i += 1

        if j == M:
            print("substring found at index {}".format(i - M))


def main():
    substring = input('substring: ')
    text = input('text: ')

    KnuthMorrisPratt(text, substring)


if __name__ == '__main__':
    main()
