# Problem — Longest Subarray With Sum Divisible by k

# You’re given an integer array nums (can contain negatives) and an integer k (k != 0).
# Return the length of the longest contiguous subarray whose sum is divisible by k. If no such subarray exists, return 0.

# Examples:

# nums = [2, -2, 2, -4, 3], k = 3 → 4
# (subarray [2, -2, 2, -4] sums to -2, which is divisible by 3? No. Try [2, -2, 2, -4, 3] sum 1 no. The best is 
# [-2, 2, -4, 3] sum -1 no. Another is [2, -2, 2, -4] sum -2 not divisible by 3… 
# You’ll need to think. There is a length-4 answer — find it.)
# nums = [1, 2, 3, 4, 1], k = 5 → 5
# nums = [5, 0, 0, 0], k = 5 → 4
# nums = [1, 2, 3], k = 7 → 0

# Constraints
# 1 <= len(nums) <= 2 * 10^5
# -10^9 <= nums[i] <= 10^9
# -10^9 <= k <= 10^9, k != 0

# Edge Cases to handle (no excuses)
# Negative numbers (both in nums and possibly negative k; treat divisibility correctly).
# Very large arrays (your O(n²) toy won’t survive).
# All zeros.
# No valid subarray.

# I/O format (if you want to script quick tests)
# Input: nums array, integer k
# Output: integer length