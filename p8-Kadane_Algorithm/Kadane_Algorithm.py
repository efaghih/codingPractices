# Maximum Subarray (Kadane’s Algorithm)

# Difficulty: Intermediate–Advanced

# Description:
# Given an integer array nums, find the contiguous subarray
#(containing at least one number) which has the largest sum, and return the sum.

# Requirements:
# Write a function max_subarray(nums: List[int]) -> int.
# Aim for O(n) time using Kadane’s algorithm.
# Handle negative numbers and mixed values correctly.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6


# Example Input/Output:



### Start of the code ###

def max_subarray(nums: list[int]) -> int:
    max_sum = nums[0]
    subsum = nums[0]
    i = 1
    while i < len(nums):
        if subsum < nums[i]:
            subsum = nums[i]
        else:
            subsum += nums[i]
        
        max_sum = max(max_sum, subsum)
        i += 1
    
    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray([1]))
print(max_subarray([5,4,-1,7,8]))

# time complexity: O(n): why? because we are iterating through the list once
# this was my first attempt at the problem, it was not exactly Kadane's Algorithm 
# So, I will now implement the real Kadane's Algorithm  
# I has better Space Complexity than my first attempt

# real Kadane's Algorithm:
# 1. Initialize max_sum to the first element of the array
# 2. Initialize subsum to 0
# 3. Iterate through the array
# 4. Add the current element to subsum
# 5. If subsum is greater than max_sum, update max_sum
# 6. If subsum is less than 0, reset subsum to 0

def max_subarray_kadane(nums: list[int]) -> int:
    max_sum = nums[0]
    subsum = 0
    for i in range(len(nums)):
        subsum = max(nums[i], subsum + nums[i])
        max_sum = max(max_sum, subsum)
    return max_sum



print("Kadane's Algorithm: ", max_subarray_kadane([-2,1,-3,4,-1,2,1,-5,4]))

# the time complexity of Kadane's Algorithm is O(n)


