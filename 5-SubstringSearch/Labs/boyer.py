'''
    Problem #2: Implement Boyer-Moore's Substring Match Algorithm (only bad char heuristic) 
    - You are to implement both functions below
    - To test your implementation, run `python utils/bm_test.py`
'''

def badCharHeuristic(substring: str):
    """Builds bad char heuristic table for Boyer-Moore algorithm

    Arguments
    ----------
    substring: type `str`

    Return: 
    - lastAt: dictionary where 
    lastAt[char] is the latest index char is seen in substring
    """
    
    # PSEUDO CODE
    
    # 1. Initialise lastAt dictionary
    # 2. Iterate through substring
    # 3. For each char, update lastAt[char] to be latest index
        
    return {}

def BoyerMoore(text: str, substring: str):
    """BoyerMoore algorithm using bad char heuristic table

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
    
    # PSEUDO CODE
    
    # 1. Initialise lastAt table using badCharHeuristic function
    # 2. Initialise variable s to 0 (used to iterate through text and perform skips)
    # 3. While s < len(text) - len(substring):
        # a. Initialise j as length of substring - 1
        # b. While substring[j] & text[s + j] match, decrement j
        # c. If mismatch occurs, skip to last instance of text[s + j]
        # d. If j is less than 0, then substring match has occured

    return []