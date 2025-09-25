# Problem Description:
# Description:
# Write a Python program that checks whether a given string is a palindrome. 
# A palindrome is a word, phrase, number, or sequence that reads the same backward 
# as forward (ignoring spaces, capitalization, and punctuation).


# Requirements:

# The function should take a string as input.

# It should return True if the string is a palindrome, otherwise False.

# Ignore capitalization, spaces, and punctuation.



# Example Input/Output:

# Input: "Racecar"
# Output: True

# Input: "Hello"
# Output: False

# Input: "A man, a plan, a canal: Panama"
# Output: True


######   Start of Code   ######

def is_palindrome(s):

    s_cleaned = ''.join(char.lower() for char in s if char.isalnum()) # this is something I leanred googling it.

    for i in range(len(s_cleaned) // 2):
        s_left = s_cleaned[i]
        s_right = s_cleaned[-i-1]


        print(s_left, s_right)
        print(f"this is i = {i}")

        if (s_left != s_right):
             return False

    return True

s = input("Enter something: ")

if is_palindrome(s):
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")