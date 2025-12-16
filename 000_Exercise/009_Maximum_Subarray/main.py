def max_sub_array(nums):
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
            
    return max_global


nums = [5,4,-1,7,8]
result = max_sub_array(nums)
print("The maximum subarray sum is:", result)
