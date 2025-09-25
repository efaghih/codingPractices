# Description:
# Instead of just checking whether a string of parentheses is valid,
# now find the length of the longest valid (well-formed) parentheses substring.


# Requirements:

# Write a function longest_valid_parentheses(s: str) -> int.

# The function should return the maximum length of valid parentheses substring.

# Try solving with O(n) time complexity using a stack or dynamic programming.


# Example Input/Output:

# Input: "(()"
# Output: 2   # "()" is the longest valid substring

# Input: ")()())"
# Output: 4   # "()()" is the longest valid substring

# Input: ""
# Output: 0


    ######   Start of Code   ######
    
def longest_valid_parentheses(s: str) -> int:
    stack = []
    max_length = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if not stack:
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
                    # i - stack[-1] is the length of the valid parentheses substring

    return max_length


print(("(()    :\t"), longest_valid_parentheses("(()"))
print((")()()) :\t") , longest_valid_parentheses(")()())"))
print(("      :\t\t"), longest_valid_parentheses(""))
print(("(()(()) :\t"), longest_valid_parentheses("(()(())"))


