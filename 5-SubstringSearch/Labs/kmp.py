'''
    Problem #1: Implement Knuth-Morris Pratt's Substring Match Algorithm (using LPS) 
    - You are to implement both functions below
    - To test your implementation, run `python utils/kmp_test.py`
'''

from typing import List


def buildLPS(substring: str) -> List[int]:
    """Build longest prefix suffix table for KMP algorithm

    Arguments
    ----------
    substring: type `str`

    Return: 
    - lps: length M array, where M is the length of substring,
    representing longest prefix suffix table of substring
    """

    # 1. Initialise lps array of length M (set each index to 0)
    lps: List[int] = [0] * len(substring)

    # 2. Initialise variables j = 0, i = 1
    j: int = 0
    i: int = 1

    # 3. Iterate through substring:
    while i < len(substring):
        # If char at j and chat at i match, then lps[j] = lps[j - 1] + 1
        if substring[i] == substring[j]:
            j += 1
            lps[i] = j
            i += 1

        # While char at j and char at i don't match, move j back to lps[j - 1]
        else:
            if j == 0:
                lps[i] = j
                i += 1
            else:
                j = lps[j - 1]

    return lps


def KnuthMorrisPratt(text: str, substring: str) -> List[int]:
    """KMP algorithm using lps table

    Arguments
    ----------
    text: type `str`
    substring: type `str`

    Return: 
    Let M = len(substring)
    - found: array of ints, where for each i, text[i: i + M] = substring,
    aka. list of start indices for substring matches
    - Your array should be in ascending order
    """

    # 1. Initialise lps using buildLPS function
    lps: List[int] = buildLPS(substring)

    # 2. Initialise variable j to 0 (j keeps track of matched chars)
    j: int = 0
    i: int = 0

    result: List[int] = []

    # 3. Iterate through text:
    while i < len(text):
        # a. If encounter match, increment j
        if text[i] == substring[j]:
            i += 1
            j += 1

            # c. If j is length of substring, then substring match has occured,
            if j == len(substring):
                # add index of start of substring within text to result arr
                result.append(i - j)
                j = lps[j - 1]
        # b. If mismatch, j = lps[j - 1] until j = 0 or text[i] = substring[j]
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

    return result
