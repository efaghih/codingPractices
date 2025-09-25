# Description:
# Given an array of integers and a target number, 
# return the indices of the two numbers that add up to the target. 
# Assume there is exactly one solution, and you may not use the same element twice.


# Requirements:

# Function should take a list of integers and a target integer.

# Return the indices of the two numbers as a tuple (i, j).

# Solve it in O(n) time using a dictionary (hash map).


# Example Input/Output:

# Input: nums = [2, 7, 11, 15], target = 9
# Output: (0, 1)   # because nums[0] + nums[1] = 2 + 7 = 9

# Input: nums = [3, 2, 4], target = 6
# Output: (1, 2)

# Input: nums = [3, 3], target = 6
# Output: (0, 1)

######   Start of Code   ######

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)


nums = [2, 7, 11, 15]
target = 9
output = two_sum(nums, target)
print("this is the output of two_sum: ", output)

nums = [3, 2, 4]
target = 6
output = two_sum(nums, target)
print("this is the output of two_sum: ", output)

# time complexity: O(n^2)



## another approach:
def two_sum_2(nums, target):
    num_map = {}
    
    for i in range(len(nums)):
        
        complement = target - nums[i]
        if complement in num_map:
            
            return (num_map[complement], i)
        num_map[nums[i]] = i


# time complexity: O(n)


print("_____________________")

nums = [2, 7, 11, 15]
target = 9
output = two_sum_2(nums, target)
print("this is the output of two_sum_2: ", output)

nums = [3, 2, 4]
target = 6
output = two_sum(nums, target)
print("this is the output of two_sum_2: ", output)




## another approach:
def two_sum_3(nums, target):

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums:
            return (i, nums.index(complement) )


print("_____________________")

nums = [2, 7, 11, 15]
target = 9
output = two_sum_3(nums, target)
print("this is the output of two_sum_3: ", output)

nums = [3, 2, 4]
target = 6
output = two_sum(nums, target)
print("this is the output of two_sum_3: ", output)

#time complexity: O(n^2)

