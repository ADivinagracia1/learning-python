


def myAtoi(s):

    def inRange(num):
        if num > 2**31-1: return 2**31-1
        elif num < -2**31: return -2**31
        else: return num    

    state = 0
    sign = 1
    val = 0
    for c in s:

        if c == " ":
            state = 0
        elif c in "+-":
            state = 1
        elif c in "0123456789":
            state = 2
        else: # is letter
            state = 0

        if state == 1:
            sign = 1 if c == "+" else -1
        elif state == 2:
            val = val*10 + int(c)


    return inRange(sign*val)




# s = "   -42"
# s = "4193 with words"
s = "words and 987"
# s = "-42"
print(s)
val = myAtoi(s)
print(val)