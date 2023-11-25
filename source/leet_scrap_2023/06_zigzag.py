s = "PAYPALISHIRING"
n = 4
i = 0   # cursor indexing through string
j = 0   # cursor indexing where to insert  
seq = 0 # tracks when to ascend/descend 
space = 0


print_list = []

while i < len(s):
    
    # print(f"{i}.{j}. {seq}")

    # insert the letters in zigzag order
    if i < n:   # make the list only to first sequence
        print_list.append(s[j]) 
        #print(f"{i}.")
    else:       # store the rest of the letters in that list
        print_list[j] += " "*space
        print_list[j] += s[i]
        if space < n-2: space += 1
        else:           space = 0
        #print(f"{j}. {print_list[j]}")

    # create the sequence to store the letters in the list
    if i - (n-1)*seq > n-2: seq+=1
    if seq % 2 == 0:        j+=1
    else:                   j-=1

    i+=1

res = ""
print(print_list)
for line in print_list:
    print(line)
    res += line

# res = ""
# for r in range(len(print_list)):
#     print(print_list[r])
#     res += print_list[r]

# print(res)