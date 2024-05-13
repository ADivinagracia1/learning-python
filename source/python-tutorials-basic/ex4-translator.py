#Yeet Language
#vowels turn into e

def translate(phrase):
    translation = ""
    for char in phrase:
        if char.lower() in "aeiou":
            if char.isupper():
                translation = translation + "E"
            else:
                translation = translation + "e"
        else:
            translation = translation + char
    return translation

ans = input("Enter a phrase: ")
print(translate(ans))