def reverse(x):
    
    strx = str(x)
    isNeg = False
    MIN = -2**31
    MAX = 2**31-1

    # print(strx)
    if strx[0] == "-": 
        isNeg = True
        strx = strx[1:]
    # print(strx)

    # perform reversal
    strx = strx[::-1]
    # print(strx)

    res = int(strx)*-1 if isNeg else int(strx) 
    # print(res)

    if res not in range(MIN, MAX):
        return 0
    else:
        return res



x = -123
print(reverse(x))