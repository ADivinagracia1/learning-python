def jump(nums):
    
    # while i < len(nums):
    #     print(i, nums[i], len(nums))
    #     i += 1
    
    i = 0
    val = nums[i]
    jumps = []
    jumps.append(val)

    while i < len(nums) - 1:
        val -= 1
        i += 1
        if val < nums[i] or val == 0:
            val = nums[i]
            jumps.append(val)
        print(i, nums[i], len(nums), val, jumps)

    # if val > 0:
    #     jumps.append(val)

    return len(jumps) - 1

nums = [2,3,1,1,4]
val = jump(nums)
print(val)