def fibTab(n):
    table = [None] * (n + 1)

    table[0] = 1
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    
    return table[n]

# MAIN
print(fibTab(2))
print(fibTab(3))
print(fibTab(5))
print(fibTab(7))
print(fibTab(50))
print(fibTab(100))


