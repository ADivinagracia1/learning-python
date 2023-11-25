def quickSort(nums):

    # Base case
    if nums == []: return []
    
    index = 0           # define first element as pivot 
    pivot = nums[index] # remember, list is unsorted
    small = []
    large = []

    # loop through list with the index element removed
    for n in nums[index+1:]:
        if pivot > n:
            small.append(n) # smaller than pivot go to the smaller list
        else:
            large.append(n) # larger than pivot go to the larger list
    
    # recursively repeat until list is sorted
    return quickSort(small) + [pivot] + quickSort(large)


def threeSum(nums):

    res = []

    for i in range(len(nums)):
    # i = 1 #debugging, manually assigning i
        l = i + 1
        r = len(nums)-1

        # window
        while l < r:

            sum = nums[i] + nums[l] + nums[r]
            # solution did not code it this way, try starting with sum == 0 condition
            # print(f"{i}, {l}, {r} --> sum = {sum}")
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                # print("^ Good set")
                win = [nums[i], nums[l], nums[r]]
                if win not in res:
                    res.append(win)
                l += 1
                r -= 1
    
    return res

        

nums = [-1,0,1,2,-1,-4]
sNums = quickSort(nums)
# print(sNums)
val = threeSum(sNums)
print(val)