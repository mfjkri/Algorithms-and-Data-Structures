'''
    Boyer-Moore algorithm (using bad char heuristic) for substring match
    - Best time complexity: O(N/M) 
    - Worse time complexity: O(NK) 
'''

def badCharHeuristic(substring):
    lastAt = {}

    for i in range(len(substring)):
        lastAt[substring[i]] = i

    return lastAt


def BoyerMoore(text, substring):
    lastAt = badCharHeuristic(substring)

    M = len(substring)
    N = len(text)
    s = 0
    
    while (s <= N-M):
        j = M - 1

        while j >= 0 and text[s + j] == substring[j]:
            j -= 1

        if j < 0:
            print('pattern occured at index: {}'.format(s))
            s += 1
        else:
            s += max(1, j - lastAt[text[s + j]])


BoyerMoore("BANANA", "ANA")