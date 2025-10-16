# Longest Substring Without Repeating Characters (Sliding Window - Medium)

# Description:
# Given a string s, return the length of the longest substring without repeating characters.

# Requirements:
# Implement a function:

# def length_of_longest_substring(s: str) -> int:


# Example:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The longest substring without repeating characters is "abc".



### Start of Code ###
## Hint: I found out by practice that sliding window is useful for these kinds of problems!

def Longest_sub_SW(s: str) -> int:
    char_map = {}
    start = 0
    maxLen = 0

    for end in range(len(s)):
        char = s[end]
        char_map[char] = char_map.get(char, 0) + 1 #.get return 0 if char is not already in the map. Cool! :)

        # If duplicate found, shrink window until no duplicates remain
        while char_map[char] > 1:
            char_map[s[start]] -= 1
            start += 1

        # Update max length for the current valid window
        maxLen = max(maxLen, end - start + 1)

    return maxLen



print ("___________Sliding Window Practice____________")
s1 = "aaaa"
print(f"{s1}. MaxLen = ", {Longest_sub_SW(s1)})


s2 = "abcddbccc"
print(f"{s2}. MaxLen = ", {Longest_sub_SW(s2)})


s3 = "aaaa"
print(f"'{s3}'. MaxLen = ", {Longest_sub_SW(s3)})

s4 = "abcabcbb"
print(f"'{s4}'. MaxLen = ", {Longest_sub_SW(s4)})
      

s5 = "aavvbbccsdcfgtyu"
print(f"'{s5}'. MaxLen = ", {Longest_sub_SW(s5)})
      

s6 = ""
print(f"'{s6}'. MaxLen = ", {Longest_sub_SW(s6)})

s7 = "abcadfba"
print(f"'{s7}'. MaxLen = ", {Longest_sub_SW(s7)})
