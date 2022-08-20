def uniquePaths(m, n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)

print(uniquePaths(1, 1))
print(uniquePaths(3, 2))
print(uniquePaths(100, 100))