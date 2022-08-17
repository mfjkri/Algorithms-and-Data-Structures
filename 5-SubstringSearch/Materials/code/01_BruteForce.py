'''
    Brute-Force algorithm for substring match
    - Best time complexity: O(N) 
    - Worse time complexity: O(NK) 
'''

def BruteForceSubstringSearch(text, substring):
    N = len(text)
    M = len(substring)

    for i in range(N - M + 1):

        match = True
        for j in range(len(substring)):
            if text[i + j] != substring[j]:
                match = False

        if match:
            print("substring found at index {}".format(i))


def main():
    substring = input("substring: ")
    text = input("text: ")
    BruteForceSubstringSearch(text, substring)

if __name__ == "__main__":
    main()
