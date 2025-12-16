def move_zeroes(nums):
    last_non_zero_found_at = 0

    for current in range(len(nums)):
        if nums[current] != 0:
            nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1

nums = [0,1,0,3,12]
move_zeroes(nums)
print(nums)
