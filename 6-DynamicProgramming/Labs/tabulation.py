'''
    Problem #2: Implement the following dynamic programming problems below, using tabulation
    - To test your implementation, run `python utils/tab_test.py`
'''

from typing import List, Union


def fib(n: int) -> int:
    """Fibonacci Sequence
    - Given an int n, return the nth number in the fibonacci sequence
    - You should use tabulation for this problem

    Arguments
    ----------
    n: type `int`

    Return: 
    - Nth number in the fibonacci sequence

    Note: This function should run in O(N) time complexity
    """
    results: List[int] = [0] * (n + 1)
    results[0] = 1
    results[1] = 1

    for i in range(2, n + 1):
        results[i] = results[i - 1] + results[i - 2]

    return results[-1]


def bestSum(array: List, targetSum: int) -> Union[List[int], bool]:
    """
    - Given an array of numbers and a target sum, return: 
        -> The shortest list of numbers in array that sum to the target sum
        -> None if there isn't any
    - e.g. bestSum([25, 5], 100) -> [25, 25, 25, 25]
    - You should use tabulation for this problem

    Arguments
    ----------
    array: type `array<int>`
    targetSum: type `int`

    Return: 
    - array of any combination of integers included in the array, 
    with repeats allowed, which sum to the target
    - array should be the of the smallest size possible, or empty if there is no solution

    Note: Your function should run in O(NM) time complexity, 
    where N is the length of the array and M is the targetSum
    """

    # OPTIMAL SUBSTRUCTURE
    # From bestSum(array, targetSum),
    # recurse down into bestSum(array, targetSum - array[i])

    table: List[Union[List[int], bool]] = [True] * (targetSum + 1)

    for i in range(1, targetSum + 1):
        best_result: List[int] = []
        best_length: int = float("inf")

        toSubstrat: int
        for toSubstrat in array:

            if i - toSubstrat >= 0:
                if table[i - toSubstrat]:
                    curr_ans: Union[List[int], bool] = table[i - toSubstrat]
                    curr_ans = curr_ans.copy() if isinstance(curr_ans, List) else []
                    curr_ans.append(toSubstrat)

                    curr_ans_length: int = len(curr_ans)

                    if curr_ans_length < best_length:
                        best_result = curr_ans
                        best_length = curr_ans_length

        table[i] = best_result and best_result or False

    return table[targetSum]


def maxLengthString(prev, top, left):
    res = top if len(top) > len(left) else left
    res = res if len(res) > len(prev) else prev
    return res


def longestCommonSubsequence(string1: str, string2: str):
    """
    - Given two strings, find the longest 
    common subsequence between them, using tabulation
    - e.g. longestCommonSubsequence("HOLLER", "HELLO") -> "HLL"

    Arguments
    ----------
    string1: type `str`
    string2: type `str`

    Return: 
    - longest common subsequence between string1 & string2 as a string
    - Empty string if none exist

    Note: Your function should run in O(NM * max(N, M)) time complexity
    """

    # OPTIMAL SUBSTRUCTURE
    # For some char i of string1 & char j of string2,
    # if string1[i] & string2[j] match, then:
    # lcs(string1[:i], string2[:j]) = lcs(string1[:i - 1], string2[:j - 1]) + string1[i]
    # else:
    # lcs(string1[:i], string2[:j]) = max(
    # lcs(string1[:i - 1], string2[:j]),
    # lcs(string1[:i], string2[:j - 1])
    # )

    return ""
