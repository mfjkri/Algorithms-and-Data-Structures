def lcsMemoRecurse(string1, string2, i, j, memo):
    if (i, j) in memo:
        return memo[(i, j)]

    if i >= len(string1) or j >= len(string2):
        return ""
    
    if string1[i] == string2[j]:
        sub = lcsMemoRecurse(string1, string2, i + 1, j + 1, memo)
        memo[(i, j)] = string1[i] + sub
        return string1[i] + sub

    else:
        sub1 = lcsMemoRecurse(string1, string2, i + 1, j, memo)
        sub2 = lcsMemoRecurse(string1, string2, i, j + 1, memo)
        result = sub1 if len(sub1) > len(sub2) else sub2
        memo[(i, j)] = result
        return result

def longestCommonSubsequenceMemo(string1, string2):
    memo = {}
    return lcsMemoRecurse(string1, string2, 0, 0, memo)

# longestCommonSubsequence('HELLO', 'HOLLER')
print(longestCommonSubsequenceMemo('8111111111111111142', '222222222822222222222222222222433333333332'))