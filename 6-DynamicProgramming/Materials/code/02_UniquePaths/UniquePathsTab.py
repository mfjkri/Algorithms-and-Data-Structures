def uniquePathsTab(m, n):
    table = [[0 for j in range(m + 1)] for i in range(n + 1)]
    table[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            else:
                table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table[n][m]

print(uniquePathsTab(1, 1))
print(uniquePathsTab(3, 2))
print(uniquePathsTab(4, 3))
print(uniquePathsTab(55, 55))