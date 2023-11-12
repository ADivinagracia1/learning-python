number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
note
for <int> in <list>:
   <DO STUFF>
'''

for row in number_grid: #row is now a list!
    #for col in number_grid[row]: WRONG, they are both ints
    for col in row:
        print(col)