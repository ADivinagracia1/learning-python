
def binarySearch(nums, target, findFirst):
    l,r = 0, len(nums)-1
    result = -1
    while l <= r:
        mid = (l+r)//2
        print(l,mid,r,'\t',nums[l],nums[mid],nums[r])
        if target == nums[mid]:
            result = mid
            if findFirst:   r = mid - 1
            else:           l = mid + 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    
    return result


def searchRange(nums, target):
    first = binarySearch(nums, target, True)
    print(first)
    print("----")
    last = binarySearch(nums, target, False)
    print(last)

    return [first, last]

nums = [5,7,7,8,8,8,8,10]
target = 8
val = searchRange(nums,target)
print(val)