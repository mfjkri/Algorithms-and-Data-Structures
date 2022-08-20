def lcsRecurse(string1, string2, i, j):
    if i >= len(string1) or j >= len(string2):
        return ""
    
    if string1[i] == string2[j]:
        res = lcsRecurse(string1, string2, i + 1, j + 1)
        return string1[i] + res

    else:
        res1 = lcsRecurse(string1, string2, i + 1, j)
        res2 = lcsRecurse(string1, string2, i, j + 1)
        if len(res1) > len(res2):
            return res1
        else:
            return res2

def longestCommonSubsequence(string1, string2):
    print(lcsRecurse(string1, string2, 0, 0))

longestCommonSubsequence('HELLO', 'HOLLER')
longestCommonSubsequence('8111111111111111142', '222222222822222222222222222222433333333332')