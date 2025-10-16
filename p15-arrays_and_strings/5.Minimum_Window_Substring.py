# Minimum Window Substring (Sliding Window - Hard)

# Description:
# Given two strings s and t, return the smallest substring of s that contains all characters of t.
# If no such substring exists, return an empty string.

# Requirements:
# Implement a function:

# def min_window(s: str, t: str) -> str:


# Example:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"


### Start of Code ###
from collections import Counter  # Counter helps count characters easily
# Counter is a built-in Python class from the collections module that counts how many times 
# each element appears in an iterable (like a string or list).
# It returns a dictionary-like object where:
    # keys = unique elements
    # values = counts of those elements



def min_window(s: str, t: str) -> str:
    # Edge case: if either string is empty, there's no valid window
    if not t or not s:
        return ""

    # Count how many of each character we need from t
    target_count = Counter(t)  
 
    # Dictionary to track how many of each character we currently have in the window
    window_count = {}

    # 'need' = total unique chars required, 'have' = how many we have matched so far
    have, need = 0, len(target_count)
    # 'res' stores the start and end indices of the best (smallest) window found
    # 'res_len' stores its length; start with infinity so the first valid window will replace it
    res, res_len = [-1, -1], float("inf")
    # Left pointer for the sliding window
    left = 0

    # Expand the right side of the window one character at a time
    for right, char in enumerate(s):
        # Add the current character to the window count
        window_count[char] = window_count.get(char, 0) + 1

        # If this character is needed and we now have the correct amount, increment 'have'
        if char in target_count and window_count[char] == target_count[char]:
            have += 1

        # While our window contains all needed characters
        while have == need:
            # If this window is smaller than any previous one, update our result
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # Before moving 'left', reduce the count of the char going out of the window
            window_count[s[left]] -= 1

            # If removing this char means we no longer satisfy the required count, reduce 'have'
            if s[left] in target_count and window_count[s[left]] < target_count[s[left]]:
                have -= 1

            # Shrink the window from the left
            left += 1

    # After the loop, unpack best window indices
    l, r = res
    # If we found a valid window, return that substring; otherwise, return empty string
    return s[l:r+1] if res_len != float("inf") else ""

s = "ADOBECODEBANC"
t = "ABC"
print(f"s: ({s}) and t: ({t}) :::  Min = {min_window(s, t)}")  # Output: "BANC"
s = "ABDACB"
t = "ABC"
print(f"s: ({s}) and t: ({t}) :::  Min = {min_window(s, t)}")  # Output: "ACB"
s = "aa"
t = "a"
print(f"s: ({s}) and t: ({t}) :::  Min = {min_window(s, t)}")  # Output: "a"
s = ""
t = "ABC"
print(f"s: ({s}) and t: ({t}) :::  Min = {min_window(s, t)}")  # Output: ""



#### Total Time Complexity:

# 𝑂(𝑛+𝑚)
# O(n+m)

# n = length of s

# m = length of t

# Since m ≤ n in most cases, we often write this as O(n).