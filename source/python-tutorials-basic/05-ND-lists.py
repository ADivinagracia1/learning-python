#Can store lists within lists of any data type

a = "value"
stuff = [ [1, 2.7, "hello"], [2, 4, 4.5], [a,[[2,4], 1]] , "John"]
print(stuff[2])
print(stuff[2][1])
print(stuff[2][1][0])
print(stuff[2][1][0][1])


'''set1 = set()

for i in range(10):
    set1.add(i)

print(set1)
'''