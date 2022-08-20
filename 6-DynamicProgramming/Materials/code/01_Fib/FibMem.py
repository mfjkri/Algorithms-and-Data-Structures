
memo = {}
def fibMemo(n):
    if n in memo:
        return memo[n]

    elif n == 0 or n == 1:
        return 1

    else:
        memo[n] = fibMemo(n - 1) + fibMemo(n - 2)
        return memo[n]

# MAIN
print(fibMemo(2))
print(fibMemo(3))
print(fibMemo(5))
print(fibMemo(7))
print(fibMemo(50))
print(fibMemo(100))