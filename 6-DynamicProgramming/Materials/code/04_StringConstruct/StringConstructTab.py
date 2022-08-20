def stringConstructTab(array, targetString):
    m = len(targetString)
    table = [None] * (m + 1)
    table[0] = []


    for i in range(m + 1):
        if table[i] != None:
            for str in array:
                j = targetString[i:].find(str)
                k = len(str)

                if j == 0 and (i + k) < m + 1:
                    newRes = table[i].copy()
                    newRes.append(str)
                    if table[i + k] == None or len(newRes) < len(table[i + k]):
                        table[i + k] = newRes
    
    return table[m]


print(stringConstructTab(["HO", "HOL", "L", "ER", "LER", "LLE"], "HOLLER"))
print(stringConstructTab(["he", "llo", "world", " ", "wo", "orl", "d"], "hello world"))
print(stringConstructTab(["E", "EE", "EEE", "EEEE", "EEEEE", "EEEEEE"], "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"))