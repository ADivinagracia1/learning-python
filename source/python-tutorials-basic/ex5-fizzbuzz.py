

for i in range(20):
    word = ""

    if i % 3 == 0:
        word += "fizz"
    if i % 5 == 0:
        word += "buzz"

    if word == "":
        word = str(i)


    print(word)