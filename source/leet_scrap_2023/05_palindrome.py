s = "qaqbcbaaabbabcbabb"
s = "rbqaqbc"
s = "babad"


def longestPalindrome(s: str) -> str:

    l = 0       # left cursor
    subs1 = ""
    subs2 = ""
    res = s[0]

    for r in range(len(s)):
        # If the string is already a Palindrome, check and return the string
        if s == s[::-1]:
            return s

        # If current element exists in string --> Check if its a palindrome
        if s[r] in subs1:

            subs1+=s[r]
            subs2 = subs1   

            while l <= r:
                print(f"->{subs2}")
                subs2=subs2[1:]
                if subs2 == subs2[::-1]: 
                    # print(f"-----> {res}, {subs2}")
                    res = max(res, subs2, key = len)
                    # print(f"====>{res}")
                l+=1
            l = 0
        else:    
            subs1+=s[r]
        print(f">{subs1}")

    return res

print(longestPalindrome(s))














# print(f"Answer: {res}")
    # print(f"> {subs1}")
    
    # if s[r] in subs1:
    #     while l < r:
    #         subs2 = subs1
    #         if subs2 == subs2[::-1]:
    #             res = max(res, subs2)
    #         print(f"-> {subs2}")
    #         subs2 = subs2[1:]
    #         l+=1

    # subs1 += s[r]
    # print(f">{subs1}")


# subs1 = ""
# subs2 = ""
# res = ""
# s_list = []
# iter = 0

# for c in s:
#     iter +=1
#     subs1 += c
#     print(f"{iter}. {subs1},") 
#     if c in subs1:   
#         subs2 = subs1
#         while subs2 != subs2[::-1]:
#             print(f"--> {subs2}, {res}")
#             subs2 = subs2[1:]
#             if subs2 == subs2[::-1]:
#                 print("PALINDROME!")
#                 res = max(res, subs2)
    
    #{subs2}, {res}")
    

        
        # if subs1 == subs1[::-1]:
        #     res = max(res, subs1)
        

    

# 5. Longest Palindromic String 

# # ============== Window Method ===================
# l = 0
# r = len(s)
# subs = s
# res = ""
# i = 0
# j = 0
# iter = 0
# incr = 0 # debug
# while l <= r:

#     incr += 1 # debug
#     # if len(res) < r - l + 1:
#     # Check if palindrome
#     if subs == subs[::-1]:
#         res = max(res, subs, key = len)

#     subs = s[l:r]   # assign to string
#     r-=1            # decrement right cursor
#     if l == r:      # when cursors meet 
#         l+=1        # increment left cursor
#         r = len(s)  # reset right cursor
    
#     if len(res) > r - l: continue # if letters are too big
#     print(f"{incr}. {subs}\t\t result={res}, {len(res)}\t\t [r-l]={r-l}") # debug