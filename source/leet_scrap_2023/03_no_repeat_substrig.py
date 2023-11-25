def lengthOfLongestSubstring(s):
    
    l = 0
    my_set = set()
    my_str = ""
    res = 0

    for r in range(len(s)): # increment right cursor (left to right)
        # if found a copy, remove the first element
        # keep removing the first elemnt til you remove the copy
        while s[r] in my_str:
            l+=1
            my_str = my_str[1:]
            print(f"-->{my_str}")
            # my_set.remove(s[l])
        
        my_str += s[r]
        # my_set.add(s[r]) # add the new element in list 
        res = max(res, r - l + 1) # record the largest list size
        # print(f"s[{r}] = {s[r]} ===> {my_set}")
        print(my_str)
    
    return res


s = "pwwkew"
ans = lengthOfLongestSubstring(s)
print(ans)