def maxArea(height):
    l, r = 0, len(height)-1
    area = 0

    width = r - l
    minH = min(height[l], height[r])
    area = width*minH
    # print(f"H[{l}] = {height[l]}, H[{r}] = {height[r]}, Area = {area}")

    while l < r:
        width = r - l
        minH = min(height[l], height[r])
        area = max(area, width*minH)
        print(f"H[{l}] = {height[l]}, H[{r}] = {height[r]}, Area = {area}")

        if height[l] > height[r]:
            r-=1
        elif height[l] < height[r]:
            l+=1
        else:
            if height[l+1] >= height[r-1]: l+=1
            else: r-=1

    return area

h = [1,8,6,2,5,4,8,3,7]
#h = h[::-1]
#h = [1,3,2,5,25,24,5]
h = [14,0,12,3,8,3,13,5,14,8]
print(f"input: {h}")
res = maxArea(h)
print(f"FINAL ANSWER: {res}")


# def maxAreaSol3(height):
#     l, r = 0, len(height)-1
#     area = 0

#     width = r - l
#     minH = min(height[l], height[r])
#     area = width*minH
#     print(f"H[{l}] = {height[l]}, H[{r}] = {height[r]}, Area = {area}")
    
#     # Check for initial size
#     if len(height) == 2:
#         return area
#     #otherwise, shift two cursors indepenantly
#     else:
#         while area < width*min(height[l+1], height[r]):
#             l+=1
#             width = r - l
#             minH = min(height[l], height[r])
#             area = max(area, width*minH)
#             print(f"H[{l}] = {height[l]}, H[{r}] = {height[r]}, Area = {area}")

#         while area < width*min(height[l], height[r-1]):
#             r-=1
#             width = r - l
#             minH = min(height[l], height[r])
#             area = max(area, width*minH)
#             print(f"H[{l}] = {height[l]}, H[{r}] = {height[r]}, Area = {area}")

#     return area

# def maxAreaSol2(height):
#     l, r = 0, len(height)-1
#     area = 0
#     # print(f"H[{l}] = {height[l]}")
#     # print(f"H[{r}] = {height[r]}")

#     while True:
#         print(f"H[{l}] = {height[l]}, H[{r}] = {height[r]}")
#         width = r - l
#         maxH = min(height[r],height[l])

#         area = max(area, width*maxH)
#         if area > width*min(height[r],height[l+1]): break
#         else: l+=1
#         print(f"Area: {area}")
    
#         area = max(area, width*maxH)
#         if area > width*min(height[r-1],height[l]): break
#         else: r-=1
#         print(f"Area: {area}")


#     # while height[l] <  height[l+1] or height[r] > height[r-1]:

#     # while True:

#     #     width = r - l
#     #     maxH = min(height[r],height[l])
        
#     #     if height[l] > height[l+1]:
#     #         area = max(area, width*maxH)
#     #         print(f"L: {area}, {l}")
#     #         l+=1

#     #     if height[r] < height[r-1]:
#     #         area = max(area, width*maxH)
#     #         print(f"R: {area}, {r}")
#     #         r-=1
        
#     return area


# def maxAreaNaive(height):
#     r, l = 0, len(height)-1
#     area = 0

#     for r in range(len(height)):
#         # print(r, height[r])
#         while l > r:
#             width = l - r
#             maxH = min(height[r],height[l])
#             area = max(area, width*maxH)
#             # print(f"-->{l}")
#             # print(f"====> {width}*{maxH} = {area}")
#             l-=1
#         l = len(height)-1
    
#     return area
