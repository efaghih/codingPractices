# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def serialize(root: Node) -> str:
    """Encodes a tree to a single string using preorder traversal."""
    vals = []  # list to collect values of nodes in traversal order

    def preorder(node):
        if not node:              # if node is None
            vals.append('#')      # add marker for null
            return
        vals.append(node.val)     # record current node's value
        preorder(node.left)       # recurse on left subtree
        preorder(node.right)      # recurse on right subtree

    preorder(root)                # start preorder traversal from root
    return ','.join(vals)         # join values into a single comma-separated string

def deserialize(data: str) -> Node:
    """Decodes your encoded data back into a tree."""
    vals = iter(data.split(','))  # split string into tokens, make it an iterator

    def build():
        val = next(vals)          # get the next value
        if val == '#':            # '#' means null node
            return None
        node = Node(val)          # create a new node
        node.left = build()       # recursively build left subtree
        node.right = build()      # recursively build right subtree
        return node               # return reconstructed node

    return build()                # build the tree starting from root


# ---- Test ----
if __name__ == "__main__":
    # Construct a test tree manually:
    #       root
    #      /    \
    #   left   right
    #   /
    # left.left
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    # Serialize the tree into a string
    s = serialize(node)
    print("Serialized:", s)

    # Deserialize the string back into a tree
    restored = deserialize(s)

    # Verify that the structure is preserved
    assert restored.left.left.val == 'left.left'
    print("✅ Test passed!")