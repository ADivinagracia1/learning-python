
def basic_if():
    is_male = False
    is_tall = True
    if is_male and is_tall:
        print("You a tall man")
    elif is_male and not(is_tall):
        print("You are a short man")
    elif not(is_male) and is_tall:
        print("You are a tall woman")
    else:
        print("You are not a man and not tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(4,2,8))
basic_if()