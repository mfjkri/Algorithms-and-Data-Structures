def maxLengthString(prev, top, left):
    res = top if len(top) > len(left) else left
    res = res if len(res) > len(prev) else prev
    return res

def lcsTab(string1, string2):
    m = len(string1)
    n = len(string2)

    table = [["" for j in range(m + 1)] for i in range(n + 1)]

    for i in range(n+ 1):
        table[i][0] = ""
    for j in range(m + 1):
        table[0][j] = ""

    # N
    for i in range(1, n + 1):
        # M
        for j in range(1, m + 1):
            prev = table[i - 1][j - 1] 

            if string2[i - 1] == string1[j - 1]:
                # max(M, N)
                prev += string1[j - 1]
            
            top = table[i - 1][j]
            left = table[i][j - 1]

            table[i][j] = maxLengthString(prev, top, left)
    
    for row in table:
        print(row)
    return table[n][m]


print(lcsTab('HELLO', 'HOLLER'))
# print(lcsTab('clement', 'antoine'))
# print(lcsTab('8111111111111111142', '222222222822222222222222222222433333333332'))