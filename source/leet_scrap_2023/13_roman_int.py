def romanToInt(s: str) -> int:
    
    res = 0
    roman = {   "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000   }

    for i in range(len(s)):

        # check if next char exists
        # and that next char is greater than the current char
        if i + 1 < len(s) and roman[s[i+1]] > roman[s[i]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]

    return res

s = "MCMXCIV"
print(romanToInt(s))