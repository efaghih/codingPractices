
from collections import deque

class node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def add(self, n):
        if self.left is None:
            self.left = n
            return
        elif self.right is None:
            self.right = n
            return
        else:
            # recursively try adding to left subtree first
            self.left.add(n)


    def add_node(self, val):
        """
        Insert a new node into the tree in BFS (level-order) fashion.
        This ensures that all nodes on a level are filled left-to-right
        before moving to the next level.
        """

        # create the new node object to insert
        new_node = node(val)

        #  Case 1: if current node has no left child, insert here
        if self.left is None:
            self.left = new_node
            return

        #  Case 2: if current node has no right child, insert here
        if self.right is None:
            self.right = new_node
            return

        #  Case 3: both children exist — need to find next available spot
        # we’ll perform a BFS traversal using a queue
        q = deque()         # create a double end queue
        q.append(self)      # start BFS from this node (usually root)



        # what we are doing here? > we are checking each node starting from the root. 
        # first, pop the under-check node from the queue. if the node has any child spot available
        # then we fill that spot with the new node starting from the left. Otherwise,
        # if the node has no available spot, we enqueue the childrens (left oriented) and do this for the next 
        # node in the queue q.
        
        # continue until we find a node with an empty child
        while q:
            # get (and remove) the first node in the queue
            current = q.popleft()

            #  check left child
            if current.left is None:
                # found empty left spot — insert and stop
                current.left = new_node
                return
            else:
                # otherwise, enqueue this left child to check later
                q.append(current.left)

            #  check right child
            if current.right is None:
                # found empty right spot — insert and stop
                current.right = new_node
                return
            else:
                # otherwise, enqueue this right child to check later
                q.append(current.right)






    def traverse_tree(self):
        result = [] 
        
        #pre-order
        result.append(self.val)
       
        if self.left:
            result.extend(self.left.traverse_tree())
        else:
            result.append(None)

        if self.right:
            result.extend(self.right.traverse_tree())
        else:
            result.append(None)
        
        return result

    # Print nicely
    def print_tree(self):
        values = self.traverse_tree()
        print("Tree (in-order):", values)
    




## This is the visual print_simple_tree that I find it by googling ##



def print_simple_tree(root, max_levels): # (root, number of the levels we want to see)
    if not root:
        print("Tree is empty")
        return

    # Queue for BFS: stores (node, level)
    q = deque([(root, 1)])  
    levels = []  # list of lists, each inner list = values at that level

    # BFS traversal
    while q:
        node, level = q.popleft()   # remove node from front of queue
        if level > max_levels:      # stop if we reached beyond requested depth
            break
        if len(levels) < level:     # ensure levels list has space for this level
            levels.append([])

        # Add current node's value (or None if node is missing)
        levels[level - 1].append(node.val if node else None)

        # Add children to queue (even None, to keep spacing correct)
        if node:
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))

    # Now pretty-print each collected level
    max_width = 2 ** max_levels  # baseline spacing for centering tree
    for i, lvl in enumerate(levels):
        # Calculate spacing before/around nodes at this level
        space = " " * (max_width // (2 ** (i + 1)))

        # Convert each node value into string (replace None with " ")
        line = space.join(str(v) if v is not None else " " for v in lvl)

        # Print the formatted line for this tree level
        print(space + line)


n = node(1)
n.add_node(2)
n.add_node(3)
n.add_node(4)
n.add_node(5)
n.add_node(6)
n.add_node(7)
n.add_node(8)


n.print_tree()
print_simple_tree(n,4)
