
def longestCommonPrefix(strs):

    # # NEW LINE OF CODE TO LEARN "all()" --> checks if everything inside is true
    # strs = ["flower","flow","flight"]
    # print( all("fl"  in a for a in strs) ) # True
    # print( all("flo" in a for a in strs) ) # False
    
    prefix = ""

    # loop the smallest string (wont have a shared prefix in other strings)
    for i in range(len(min(strs, key=len))): 
        
        c = strs[0][i]  # know that the 0th element exists + grab the char from there
        # check i-th position of all words, if same letter then all() returns True  
        if all(c == word[i]  for word in strs):
            prefix += c
        else: 
            break
            
    return prefix

    
    



strs1 = ["flower","flow","flight"]
# strs1 = ["dog","racecar","car"]
val = longestCommonPrefix(strs1)
print(f"==> {val}")

# Attempt 1 =======================================
    # temp = ""
    # res = ""
    # prev = ""
    # i, j = 0,0

    # for word in strs:
    #     # print(word)

    #     while i < len(prev) and j < len(word):
    #         print(prev[i], word[j])
    #         if prev[i] == word[j]:
    #             temp += word[j]
    #         i += 1 if i < len(prev) else 0
    #         j += 1 if i < len(word) else 0

        

    #     res = temp if len(temp)>len(res) else res
    #     print(f"-----{res}-----")
        
    #     i, j = 0,0
    #     prev = word
    #     temp = ""

    # print(res)
    # # return res
