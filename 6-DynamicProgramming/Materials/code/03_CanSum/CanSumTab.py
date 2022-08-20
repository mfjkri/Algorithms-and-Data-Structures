def canSumTab(array, target):
    table = [False] * (target + 1)
    table[0] = True

    for i in range(target + 1):
        if table[i]:
            for number in array:
                if (i + number) < len(table):
                    table[i + number] = True
    
    return table[target]

print(canSumTab([3, 6, 7], 1000))
print(canSumTab([7, 14], 300))
        
