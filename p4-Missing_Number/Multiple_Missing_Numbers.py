# Description:
# Imagine you are analyzing sensor data or student roll numbers. 
# You are given a list of integers from 1 to n, but some numbers 
# are missing — not just one.
# but extend it so that you can find all missing numbers in the sequence.


# Requirements:

# Function should take a list of integers as input.

# Return a list of all missing numbers, sorted in ascending order.

# If no numbers are missing, return an empty list.

# Example Input/Output:

# Input: [1, 2, 4, 6, 7, 9]
# Output: [3, 5, 8]

# Input: [3, 5, 1]
# Output: [2, 4]

# Input: [1, 2, 3]
# Output: []


######   Start of Code   ######


def find_multiple_missing_numbers(numList):
    missing_numbers = []
    for i in range(1, len(numList)+1):
        if i not in numList:
            missing_numbers.append(i)
    return missing_numbers

input_list = [1, 2, 4, 6, 7, 9]
output = find_multiple_missing_numbers(input_list)
print(output)





