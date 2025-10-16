# Description:
# Given an integer array nums and an integer k, find the maximum sum of any contiguous subarray 
# of size k.

# Requirements:
# Implement a function:

# def max_sum_subarray(nums: list[int], k: int) -> int:


# Example:

# Input: nums = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9
# Explanation: Subarray [5, 1, 3] has the maximum sum = 9


# Expected Time: O(n) using a sliding window
# Hint: Move the window one step at a time, subtract the element 
# that goes out and add the one that comes in.


### Start of Code ###
## Sol1: (O(n × k))

def max_sum_subarray1(nums: list[int], k: int) -> int:
    start = 0
    max_sub = 0
    tmp_sum = 0
    for i in nums:
        for j in range (start,start+k, 1):
            if(j < len(nums)):
                tmp_sum += nums[j]
        max_sub = max(max_sub, tmp_sum)
        tmp_sum = 0
        start = i+1
    return max_sub


k = 3
nums = [2, 1, 5, 1, 3, 2]
print("max_sum_subarray1: ", max_sum_subarray1(nums, k))
nums = []
print("max_sum_subarray1: ", max_sum_subarray1(nums, k))
nums = [2]
print("max_sum_subarray1: ", max_sum_subarray1(nums, k))


print("__________________________________SOL2: ")


## Sol2: (O(n))
def max_sum_subarray2(nums: list[int], k: int) -> int:
    window_sum = sum(nums[:k])
    max_sub = window_sum
    
    for i in range (k, len(nums)): # i is like the end point of the window!
        window_sum = window_sum - nums[i-k] + nums[i] # update the window sum by the next window
        max_sub = max(max_sub , window_sum)

    return max_sub


k = 3
nums = [2, 1, 5, 1, 3, 2]
print("max_sum_subarray2: ", max_sum_subarray2(nums, k))
nums = []
print("max_sum_subarray2: ", max_sum_subarray2(nums, k))
nums = [2]
print("max_sum_subarray2: ", max_sum_subarray2(nums, k))


