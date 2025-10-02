# Description:
# Given the root of a binary tree, return its maximum depth.
# The maximum depth is the number of nodes along the longest path 
# from the root down to the farthest leaf node.


# Requirements:

# Implement a class TreeNode with attributes val, left, and right.
# Write a function max_depth(root: TreeNode) -> int.
# You can solve this using recursion or BFS (level-order traversal).


# Example Input/Output:

# Input: [3,9,20,None,None,15,7]
# Output: 3
# # Explanation: Longest path is 3 -> 20 -> 15 or 3 -> 20 -> 7


### Start of code ###

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


### first solution ###

def max_depth(root: TreeNode) -> int:
    # Base case: if tree is empty
    if not root:
        return 0

    # Recursively get depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # Add 1 for the current node
    return 1 + max(left_depth, right_depth)




### second solution ###
from collections import deque

def max_depth2(root: TreeNode) -> int:
    if root == None:
        return 0
    
    depth = 0
    queue = deque([root])

    while queue:
        depth += 1

        for i in range (len(queue)):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth





# test the function (uncomment them)

   
# # Test 1: Skewed right tree
# root = TreeNode(0)
# node = root
# for i in range(1, 10):
#     node.left = TreeNode(i*2)
#     node = node.left




# #solution 1:
# print("solution 1 :: Test 1")
# print(max_depth(root))

# #solution 2:
# print("solution 1 :: Test 1")
# print(max_depth2(root))




# # Test 2: Skewed right tree
# print("\n___________________________________________")
# root = TreeNode(0)
# node = root
# for i in range(1, 10):
#     node.right = TreeNode(i*2)
#     node = node.right



# #solution 1:
# print("solution 1 :: Test 2")
# print(max_depth(root))

# #solution 2:
# print("solution 1 :: Test 2")
# print(max_depth2(root))



# # Test 3: 
# print("\n___________________________________________")
# root = TreeNode(0)
# node = root
# for i in range(1, 5):
#     node.right = TreeNode(i*2)
#     if i % 2 == 1:
#         node.left = TreeNode(i*2+1)
#     node = node.right

# #solution 1:
# print("solution 1 :: Test 3")
# print(max_depth(root))

# #solution 2:
# print("solution 1 :: Test 3")
# print(max_depth2(root))



print("\n___________________________________________")
t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)

# Add these lines:
print("Test 4:")
print("Solution 1:", max_depth(t1))
print("Solution 2:", max_depth2(t1))