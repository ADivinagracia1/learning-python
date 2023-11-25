def findMin(arr):
    # Binary Search, but finding 
    l, r = 0, len(arr)-1

    if len(nums) == 1:  return 0
    if arr[l] < arr[r]: return 0

    while l < r: # note: not l <= r 
        mid = (l + r)//2 
        print(l,mid,r)
        if arr[mid] > arr[r]:
            l = mid + 1
        else:
            r = mid 
    
    print(l,mid,r)
    return l

def search(nums, target):
    # Binary Search 3 times: O(3log n)

    pivot = findMin(nums)
    # print(pivot)

    # Binary Search with range: [0, pivot]
    l, r = 0, pivot
    # print(l, r, "first")
    while l < r:
        mid = (l + r)//2
        # print(l,mid,r)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid
        else:
            l = mid + 1
    
    # Binary Search with range: [pivot, len(nums)-1]
    l, r = pivot, len(nums)-1
    print(l, r, "second")
    while l < r:
        mid = (l + r)//2
        print(l,mid,r)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1 
        else:
            l = mid + 1
    
    return -1
    


# nums = [4,5,0,1]
# target = 0
# nums = [4,5,6,7,0,1,2]
# target = 12
# nums = [1,3]
# target = 3
# val = search(nums, target)

nums = [9,0,1,2,4,5,6,7,8]
val = findMin(nums)
print(val)