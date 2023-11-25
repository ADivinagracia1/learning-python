def binarySearch(nums, targ):

    l, r = 0, len(nums)-1

    # print(l, r)
    # print(nums[l], nums[r])

    while l <= r:
        mid = (l+r)//2
        print("ind: ",l,mid,r)
        print("val: ", nums[l],nums[mid],nums[r])
        print()
        if targ == nums[mid]:
            return mid
        elif targ > nums[mid]:
            l = mid+1
        else:
            r = mid-1

    return -1

nums = [1,3,5,7,8,9,12,15]
targ = 15
val = binarySearch(nums, targ)
print(val)