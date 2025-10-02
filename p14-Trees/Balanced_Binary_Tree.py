# Difficulty: Intermediate–Advanced

# Description:
# A balanced binary tree is one in which the heights of the two subtrees of every node
# never differ by more than 1.
# Write a function that determines if a binary tree is height-balanced.



# Requirements:

# Use the same TreeNode structure from before.
# Implement is_balanced(root: TreeNode) -> bool.
# Must run in O(n) — check height and balance in one pass (avoid repeated recursion).

# Example Input/Output:

# Input:
#       3
#      / \
#     9  20
#        / \
#       15  7
# Output: True

# Input:
#       1
#      / \
#     2   2
#    / \
#   3   3
#  / \
# 4   4
# Output: False



### first solution using max_depth2 function defined in Maximum_Depth__Binary_Tree.py ###
from Maximum_Depth__Binary_Tree import max_depth2, TreeNode
from collections import deque

def is_balanced(root: TreeNode) -> bool:
    if not root:
        return True
    
    queue = deque([root])
    
    while queue:
        level_size = len(queue) # to do level-by-level traversal
        
        for _ in range(level_size):
            node = queue.popleft()
            
            # Get depths
            depth_left = max_depth2(node.left) if node.left else 0
            depth_right = max_depth2(node.right) if node.right else 0
            
            if abs(depth_left - depth_right) > 1:
                return False
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return True





### second solution using recursion ###
# I did not implement this solution. But I found it on the internet searching 
# for a better solution. I think it is a better solution because it is more efficient.
# However, what if an stack overflow error occurs? (recursion depth limit)

def is_balanced2(root: TreeNode) -> bool:
    # Helper function returns height if balanced, -1 if not
    def check(node):
        if not node:
            return 0  # height of empty tree = 0

        left_height = check(node.left)
        if left_height == -1:
            return -1  # left subtree unbalanced

        right_height = check(node.right)
        if right_height == -1:
            return -1  # right subtree unbalanced

        # If height difference > 1 → unbalanced
        if abs(left_height - right_height) > 1:
            return -1

        # Return height if balanced
        return 1 + max(left_height, right_height)

    # Start recursion
    return check(root) != -1










print("\n___________________________________________")
t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(5)


t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.left.left = TreeNode(3)



t3 = TreeNode(3)
t3.left = TreeNode(9)
t3.right = TreeNode(20)

## Solution 1: Test 
print("solution 1 :: Test 1")
print(is_balanced(t1))  # True
print("solution 1 :: Test 2")
print(is_balanced(t2))  # False
print("solution 1 :: Test 3")
print(is_balanced(t3))  # True


## Solution 2: Test 
print("\n___________________________________________")
print("solution 2 :: Test 1")
print(is_balanced2(t1))  # True
print("solution 2 :: Test 2")
print(is_balanced2(t2))  # False
print("solution 2 :: Test 3")
print(is_balanced2(t3))  # True
