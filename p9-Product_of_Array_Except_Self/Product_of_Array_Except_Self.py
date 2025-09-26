# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element 
# at index i of the new array is the product of all the numbers 
# in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?


### My Solution ###

def product_of_array_except_self(nums: list[int]) -> list[int]:
    result = []
    product = 1
    for i in range(len(nums)):
        product *= nums[i]

    for i in range(len(nums)):
        result.append(product // nums[i])

    return result

print(product_of_array_except_self([1, 2, 3, 4, 5]))


# Follow-up: what if you can't use division?
# brute force solution:

def product_of_array_except_self_no_division(nums: list[int]) -> list[int]:
    result = []
    product = 1

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        result.append(product)
        product = 1

    return result

print(product_of_array_except_self_no_division([1, 2, 3, 4, 5]))



# Follow-up: what if you can't use division?
# Efficient solution: Two-Pass Product Algorithm

def product_of_array_except_self_efficient(nums):
    n = len(nums)
    result = [1] * n # result = [1, 1, 1, 1, 1] for this example
    
    # First pass: calculate left products
    # Start from index 1, not 0, since result[0] is already 1
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Second pass: multiply by right products
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] = result[i] * right_product
        right_product *= nums[i]
    
    return result

print(product_of_array_except_self_efficient([1, 2, 3, 4, 5]))


# time complexity: O(n)
# space complexity: O(1)

