def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # In case k is greater than n
    return nums[-k:] + nums[:-k]

nums = [1,2,3,4,5,6,7]
k = 3

rotated = rotate_array(nums, k)
print(rotated)
