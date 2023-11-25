def isMatch(s, p):
    
    lletters = "qwertyuiopasdfghjklzxcvbnm"
    state = 0
    p_prev = "x"
    i, j = 0, 0

    while i < len(s) or j < len(p):

        # if i >= len(s) or j >= len(p):
        #     print("here")
        #     return False

        print(i, j)

        # State Transition Handler
        if p[j] in lletters: state = 0
        elif p[j] == ".": state = 1
        elif p[j] == "*": state = 2
 
        # States 
        if state == 0:
        # char x char
            print(f"s0: s[{i}]='{s[i]}', p[{j}]='{p[j]}'")
            if s[i] == p[j]:
                i+=1
                j+=1
            else:
                if p[j+1] == "*":
                    i+=1
                    j+=1
                    continue
                else:
                    return False
        elif state == 1:
        # char x .
            print(f"s0: s[{i}]='{s[i]}', p[{j}]='{p[j]}'")
            i+=1
            j+=1
        elif state == 2:
        # char x *
            print(f"s0: s[{i}]='{s[i]}', p[{j}]='{p[j]}'")
            # print(p_prev)
            if s[i] == p_prev:
                j+=1
            else:
                j+=2
            i+=1

        p_prev = p[j-1]

    return True

    

s = "aa"
p = "c*"
val = isMatch(s, p)
print(val)