def CanSum(array, target):
    if target == 0:
        return 1
    if target < 0:
        return 0

    for i in array:
        newTarget = target - i
        if (CanSum(array, newTarget)):
            return True
    
    return False

print(CanSum([3, 6, 7], 1000))
print(CanSum([7, 14], 300))
        
