# Description:
# You are given a list of n-1 numbers in the range from 1 to n.
# The numbers are all distinct and exactly one number is missing.
# Write a function to find that missing number.


# Requirements:

# Function should take a list of integers as input.

# Return the missing number.

# The solution should work in O(n) time.

# Example Input/Output:

# Input: [1, 2, 4, 5, 6]
# Output: 3

# Input: [3, 7, 1, 2, 8, 4, 5]
# Output: 6

######   Start of Code   ######
input_list = [1, 2, 4, 5, 6]
def find_missing_number(numList):
    sum_numList = 0
    for i in range(len(numList)+1):
        sum_numList = sum_numList + i

    return sum(numList) - sum_numList  


f = find_missing_number(input_list)
print(f)



# ## another approach:

# def find_missing_number_2(numList):
#     return sum(range(len(numList)+1)) - sum(numList) 
#     # This method is more efficient because it:
#     # - Uses no extra space
#     # - Avoids extra loops
#     # - Does not rely on additional variables, functions, or libraries

# f2 = find_missing_number_2(input_list)
# print(f2)




