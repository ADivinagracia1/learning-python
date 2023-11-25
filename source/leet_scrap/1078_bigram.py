def findOcurrences(text, first, second):

    state = 0
    ans = []
    text_list = text.split()

    for i in range(len(text_list)):
        if state == 0:
            print(text_list[i], "s0")
            if text_list[i] == first:
                state = 1
        elif state == 1:
            print(text_list[i], "s1")
            if text_list[i] == second:
                state = 2
                try:
                    ans.append(text_list[i+1])
                except:
                    pass
            elif text_list[i] == first:
                state = 1
            else:
                state = 0
        elif state == 2:
            print(text_list[i], "s2")
            if text_list[i] == first:
                state = 1
            else:
                state = 0

    return ans


text = "alice is a good girl she is a good student"
first = "a"
second = "good"

text = "we will we will rock you"
first = "we"
second = "will"

text = "we we we we will rock you"
first = "we"
second = "we"


val = findOcurrences(text, first, second)
print(val)