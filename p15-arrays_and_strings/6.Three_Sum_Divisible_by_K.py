# Three Sum Divisible by K — Problem Description

# Problem:

# Given an array of integers nums and an integer k, return the number of triplets (i, j, l) 
# such that:

# 0 ≤ i < j < l < len(nums)

# The sum of the triplet is divisible by k:

# (nums[i]+nums[j]+nums[l])modk=0

# Example:

# Input:
# nums = [2, 3, 1, 6, 4]
# k = 3

# Output:
# 4




from collections import Counter
from math import comb

def threeSumDiv_k(nums: list, k: int) -> int:
    # Step 1: Count remainders
    remainders = [x % k for x in nums]
    freq = Counter(remainders)

    count = 0

    # Step 2: Iterate over remainder combinations a <= b <= c
    for a in range(k):
        for b in range(a, k):
            c = (k - (a + b) % k) % k  # the remainder needed to complete divisible-by-k

            if c < b:     # to keep order: a <= b <= c
                continue

            # counts of each remainder
            fa, fb, fc = freq[a], freq[b], freq[c]

            # Skip if any bucket is empty
            if fa == 0 or fb == 0 or fc == 0:
                continue

            # Case 1: all remainders same → a == b == c
            if a == b == c:
                if fa >= 3:
                    count += comb(fa, 3)

            # Case 2: a == b != c (two same, one different)
            elif a == b < c:
                if fa >= 2:
                    count += comb(fa, 2) * fc

            # Case 3: a < b == c
            elif a < b == c:
                if fb >= 2:
                    count += fa * comb(fb, 2)

            # Case 4: all different → a < b < c
            else: # a < b < c
                count += fa * fb * fc

    return count




nums = [2, 3, 1, 6, 4]
k = 3
#Output = 4
Output = threeSumDiv_k (nums, k)
print(Output)

nums = [1, 2, 3]
k = 3
#Output = 1
Output = threeSumDiv_k (nums, k)
print(Output)

nums = [3, 3, 3, 3]
k = 3
#Output = 4
Output = threeSumDiv_k (nums, k)
print(Output)