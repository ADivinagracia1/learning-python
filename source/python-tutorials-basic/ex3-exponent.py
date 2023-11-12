def to_pow_of(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num
    return result

base = int(input("Enter base: "))
power = int(input("Enter power: "))

print(base**power)              #operator
print(to_pow_of(base,power))    #self made function