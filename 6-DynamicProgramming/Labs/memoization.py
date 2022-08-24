'''
    Problem #1: Implement the following dynamic programming problems below, using memoization
    - To test your implementation, run `python utils/mem_test.py`
'''

from typing import Dict, List, Union


def fib(n: int, memo: Dict[int, int]) -> int:
    """Fibonacci Sequence
    - Given an int n, return the nth number in the fibonacci sequence
    - You should use recursion & memoization for this problem

    Arguments
    ----------
    n: type `int`
    memo: type `Dict`
        -> you may decide for yourself how you wish to use this memo
        -> It will be empty at the top recursive call

    Return:
    - Nth number in the fibonacci sequence

    Note: This function should run in O(N) time complexity
    """

    if n in memo:
        return memo[n]

    if n == 1 or n == 0:
        return 1

    result: int = fib(n - 1, memo) + fib(n - 2, memo)
    memo.update({n: result})

    return result


def bestSum(array: List[int],
            targetSum: int,
            memo: Dict[str, Union[List[int], None]]) -> List[int]:
    """
    - Given an array of numbers and a target sum, return:
        -> The shortest list of numbers in array that sum to the target sum
        -> None if there isn't any
    - e.g. bestSum([25, 5], 100) -> [25, 25, 25, 25]
    - You should use recursion and memoization for this problem

    Arguments
    ----------
    array: type `array<int>`
    targetSum: type `int`
    memo: type `Dict`
        -> you may decide for yourself how you wish to use this memo
        -> It will be empty at the top recursive call


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

    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return list()
    if targetSum < 0:
        return None

    best_result: Union[List[int], None] = None
    best_length: int = float("inf")

    for number in array:
        result: Union[List[int], None] = bestSum(
            array, targetSum - number, memo)

        if result is not None:
            result = result.copy()
            result.append(number)
            new_length: int = len(result)

            if new_length < best_length:
                best_result = result
                best_length = new_length

    memo.update({targetSum: best_result})
    return best_result


def longestCommonSubsequence(string1: str, string2: str, memo: Dict):
    """
    - Given two strings, find the longest
    common subsequence between them, using recursion and memoization
    - e.g. longestCommonSubsequence("HOLLER", "HELLO") -> "HLL"

    Arguments
    ----------
    string1: type `str`
    string2: type `str`
    memo: type `Dict`
        -> you may decide for yourself how you wish to use this memo
        -> It will be empty at the top recursive call

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
