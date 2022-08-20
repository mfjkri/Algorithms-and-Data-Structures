memo = {}

def uniquePathsMemo(m, n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    elif (m, n) in memo:
        return memo[(m, n)]

    else:
        cost = uniquePathsMemo(m - 1, n) + uniquePathsMemo(m, n - 1)
        memo[(m, n)] = cost
        memo[(n, m)] = cost
        return cost

print(uniquePathsMemo(1, 1))
print(uniquePathsMemo(3, 2))
print(uniquePathsMemo(55, 55))