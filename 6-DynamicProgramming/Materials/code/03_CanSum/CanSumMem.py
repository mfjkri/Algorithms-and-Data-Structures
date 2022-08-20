

def CanSum(array, target):
    if target in memo:
        return memo[target]

    if target == 0:
        return 1
    if target < 0:
        return 0

    for i in array:
        newTarget = target - i
        if (CanSum(array, newTarget)):
            memo[target] = True
            return True
    
    memo[target] = False
    return memo[target]

memo = {}
print(CanSum([3, 6, 7], 1000))
memo = {}
print(CanSum([7, 14], 300))