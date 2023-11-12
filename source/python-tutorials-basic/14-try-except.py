try:
    value = 10 / 0      #div by zero check
    num = int(input("Enter a number: "))   #Wrong input check
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")