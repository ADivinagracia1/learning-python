#map( <function>, <list> )

def cube(n):
    return n*n*n

numbers = (1, 2, 3, 4)
result = map(cube, numbers)
print(result) # iterator
print(list(result))