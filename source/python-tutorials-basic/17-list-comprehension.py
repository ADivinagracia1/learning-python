nums = [1,2,3,4,5,6,7,8,9]

# Basic for-loop (1)
my_list = []
for n in nums:
    my_list.append(n*2)
print(my_list)


# List comprehension equivalent of (1)
my_list = [n*2 for n in nums]
print(my_list)