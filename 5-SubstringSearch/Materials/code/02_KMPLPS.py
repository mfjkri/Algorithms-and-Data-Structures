'''
    Knuth Morris Pratt algorithm (using LPS) for substring match
    - Best time complexity: O(N) 
    - Worse time complexity: O(N) 
'''

def buildLPS(substring):
    lps = [0] * len(substring)
    j = 0
    
    for i in range(1, len(substring)):
        while j > 0 and substring[i] != substring[j]:
            j = lps[j - 1]

        if substring[j] == substring[i]:
            j += 1
            lps[i] = j

    return lps


def KnuthMorrisPratt(text, substring):
    lps = buildLPS(substring)

    i = 0
    j = 0

    for i in range(len(text)):
        while (j > 0 and text[i] != substring[j]):
            j = lps[j - 1]
        if text[i] == substring[j]:
            j += 1
        if j == len(substring):
            print("Found match at index {}".format(i - len(substring) + 1))
            j = lps[j - 1]


KnuthMorrisPratt("AEFOAEFCDAEFCDAED", "AEFCDAED")
KnuthMorrisPratt("ABABABABBABB", "ABBABB")
KnuthMorrisPratt("ADACADADB", "ADADB")
