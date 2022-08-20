def stringConstruct(array, string):
    if string == "":
        return []
    
    bestRes = None
    for str in array:
        i = string.find(str)

        if i != 0:
            continue

        res = stringConstruct(array, string[len(str):])
        if res != None:
            if bestRes == None or len(bestRes) > len(res):
                bestRes = res
                bestRes.insert(0, str)
    
    return bestRes

print(stringConstruct(["HO", "HOL", "L", "ER", "LER", "LLE"], "HOLLER"))

print(stringConstruct(["he", "llo", "world", " ", "wo", "orl", "d"], "hello world"))

print(stringConstruct(["E", "EE", "EEE", "EEEE", "EEEEE", "EEEEEE"], "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF"))