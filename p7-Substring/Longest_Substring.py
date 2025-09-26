# Description:
# Given a string s, find the length of the longest substring without repeating characters.


# Requirements:

# Implement length_of_longest_substring(s: str) -> int.

# Aim for O(n) time using a sliding window with a hash map (dictionary).

# Handle ASCII and Unicode safely (don’t assume only a–z).



# Examples:

# Input: "abcabcbb"   -> 3      # "abc"
# Input: "bbbbb"      -> 1      # "b"
# Input: "pwwkew"     -> 3      # "wke"
# Input: ""           -> 0
# Input: "dvdf"       -> 3      # "vdf"


### Start of the code ###

def length_of_longest_substring(s: str) -> int:

    char_map = {}
    max_length = 0
    start = 0
    i = 0
    while i < len(s):
        char = s[i]
        
        if char in char_map:
                start = char_map[char] + 1
                i = start 
                char_map = {}
                continue
                
        char_map[char] = i
        i += 1
        
        max_length = max(max_length, i - start)
    return max_length


print("abcabcbb: ", length_of_longest_substring("abcabcbb"))
print("bbbbb: ", length_of_longest_substring("bbbbb"))
print("pwwkew: ", length_of_longest_substring("pwwkew"))
print(" : ", length_of_longest_substring(""))
print("dvdf: ", length_of_longest_substring("dvdf"))
print("abcdebaflr: ", length_of_longest_substring("abcdebaflr"))



# time complexity: O(n^2) at worst case


# the real solution is to use a sliding window with a hash map

def length_of_longest_substring_sliding_window(s: str) -> int:
    char_map = {}
    max_length = 0
    start = 0

    # enumerate is a built-in function that returns a tuple 
    # containing the index and the value of the current character
    for i, char in enumerate(s): 
        if char in char_map :and char_map[char] >= start: # in short, means that the character is already in the map
            # Move start to the right of the first duplicate element
            start = char_map[char] + 1
        char_map[char] = i # update the index of the character
        max_length = max(max_length, i - start + 1)

    return max_length

# why the second condition? because we want to only consider elements that are 
# inside the current window (we only care about the longest substring)

print("--------------------------------")
print("Sliding Window algorithm: ")
print("abcabcbb: ", length_of_longest_substring_sliding_window("abcabcbb"))
print("bbbbb: ", length_of_longest_substring_sliding_window("bbbbb"))
print("pwwkew: ", length_of_longest_substring_sliding_window("pwwkew"))
print(" : ", length_of_longest_substring_sliding_window(""))
print("dvdf: ", length_of_longest_substring_sliding_window("dvdf"))
print("abcdebaflr: ", length_of_longest_substring_sliding_window("abcdebaflr"))



# time complexity: O(n)








    