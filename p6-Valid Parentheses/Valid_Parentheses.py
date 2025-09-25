# Description:
# Given a string containing just the characters 
# '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

# A string is valid if:

# Open brackets are closed by the same type of brackets.

# Open brackets are closed in the correct order.



# Requirements:

# Write a function is_valid(s: str) -> bool.

# Use a stack to solve the problem efficiently.

# Return True if valid, otherwise False.



# Example Input/Output:

# Input: "()"
# Output: True

# Input: "()[]{}"
# Output: True

# Input: "(]"
# Output: False

# Input: "([)]"
# Output: False

# Input: "{[]}"
# Output: True


######   Start of Code   ######

def is_valid(s: str) -> bool:
    stack = []
    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack: # if the stack is empty
                return False
            top = stack.pop()
            if char == ')' and top != '(':
                return False
            if char == '}' and top != '{':
                return False
            if char == ']' and top != '[':
                return False
    return not stack # if the stack is empty, return True

print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([)]"))
print(is_valid("{[]}"))

