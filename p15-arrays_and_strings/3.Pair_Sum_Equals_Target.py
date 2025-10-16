# Pair Sum Equals Target (Two Pointers - Easy)

# Description:
# Given a sorted array of integers nums and an integer target, return indices (1-based) of the two numbers that add up to target.

# Requirements:
# Implement a function:

# def two_sum_sorted(nums: list[int], target: int) -> list[int]:


# Example:

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [1, 2]
# Explanation: 2 + 7 = 9



### Start of Code ###

# this is one of the soloutions iff the input list is sorted!
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # convert to 1-based index
        
        elif current_sum < target:
            left += 1  # sum too small, increase it
        
        else:
            right -= 1  # sum too large, decrease it
    
    return []  # no solution found



### Test ###
nums = [2, 7, 11, 15] 
target = 22

print (f"nums: {nums}, target: {target} -> two_sum_sorted: {two_sum_sorted(nums, target)}")

nums = [2, 7, 11, 15] 
target = 9

print (f"nums: {nums}, target: {target} -> two_sum_sorted: {two_sum_sorted(nums, target)}")

nums = [2, 7, 11, 15] 
target = 11

print (f"nums: {nums}, target: {target} -> two_sum_sorted: {two_sum_sorted(nums, target)}")

nums = [2, 7, 11, 15] 
target = 18

print (f"nums: {nums}, target: {target} -> two_sum_sorted: {two_sum_sorted(nums, target)}")

nums = [2, 7, 11, 15] 
target = 0

print (f"nums: {nums}, target: {target} -> two_sum_sorted: {two_sum_sorted(nums, target)}")

nums = [2, 7, 11, 15] 
target = 10

print (f"nums: {nums}, target: {target} -> two_sum_sorted: {two_sum_sorted(nums, target)}")

nums = [2, 7, 11, 15] 
target = 20

print (f"nums: {nums}, target: {target} -> two_sum_sorted: {two_sum_sorted(nums, target)}")