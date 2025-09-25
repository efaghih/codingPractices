# Description:
# Write a function that checks whether two strings are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of another,
# ignoring spaces, capitalization, and punctuation.


# Requirements:

# Function should take two strings as input.

# Return True if they are anagrams, else False.

# Ignore case and spaces.


# Example Input/Output:

# Input: "listen", "silent"
# Output: True

# Input: "Hello", "Olelh"
# Output: True

# Input: "Hello", "World"
# Output: False

######   Start of Code   ######

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

s1_cleaned = ''.join(char.lower() for char in s1 if char.isalnum())
s2_cleaned = ''.join(char.lower() for char in s2 if char.isalnum())

def is_anagram(s1, s2):

    if len(s1_cleaned) != len(s2_cleaned):
        return False

    return sorted(s1_cleaned) == sorted(s2_cleaned) # it is something I learned googling it. 
    # there are other basic ways.
    # for instance writing an algorithm to check if the two strings have the same characters.
    # sorting() func has a time complexity of O(n log n)
    # however, we already know that the two strings have the same length.
    # so the time complexity is O(n)
    # this is a more efficient way to check if the two strings are anagrams.

output = is_anagram(s1_cleaned, s2_cleaned)
print(output)




