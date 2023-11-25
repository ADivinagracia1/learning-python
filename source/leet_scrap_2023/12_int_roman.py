def intToRoman(num: int):
    
    res = ""
    # Bank of roman symbold (include 4, and 9s)
    symbol = {  1000:"M",
                900: "CM",
                500: "D",
                400: "CD",
                100: "C",
                90: "XC",
                50: "L",
                40: "XL",
                10: "X",
                9: "IX",
                5: "V",
                4: "IV",
                1: "I"
            }
    
    while num > 0:
        for place in symbol:
            if num >= place: # find a value in dict that goes into num   
                break        # stop looping at that value and use it
        num -= place
        res += symbol[place]
        # print(f"{num} --> {place} ==> {res}")
    return res

num = 1994
ans = intToRoman(num)
print(ans)