"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them 
is that adjacent houses have security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
 """

def house_robber(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev1, prev2 = 0, 0
    
    for num in nums:
        temp = prev1
        prev1 = max(prev2 + num, prev1)
        prev2 = temp
    
    return prev1


nums = [2,7,9,3,1]
print(house_robber(nums))
