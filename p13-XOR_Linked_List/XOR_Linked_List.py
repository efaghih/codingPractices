

# This problem was asked by Google.

# An XOR linked list is a more memory efficient doubly linked list. Instead of 
# each node holding next and prev fields, it holds a field named both, which is 
# an XOR of the next node and the previous node. Implement an XOR linked list; 
# it has an add(element) which adds the element to the end, and a get(index) which
#  returns the node at index.

# If using a language that has no pointers (such as Python), 
# you can assume you have access to get_pointer and dereference_pointer functions 
# that converts between nodes and memory addresses.



### Start of code ###

def get_pointer(node):
    return id(node) if node else 0 # id is a built-in function that 
                                   # returns the memory address of the object

def dereference_pointer(address):
    return memory.get(address) if address else None
    # get is a built-in function that returns the value of the key 
    # if it exists, otherwise None


class Node:
    def __init__(self, value):
        self.value = value
        self.both = 0   # XOR of prev and next



# We’ll store all nodes in a dictionary to simulate memory:

memory = {}


class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        new_node = Node(element)
        memory[get_pointer(new_node)] = new_node # add the new node to the memory

        if self.head is None: # if the list is empty
            # First node
            self.head = self.tail = new_node # set the head and tail to the new node    
        else:
            """ 
            new_node.both = get_pointer(self.tail):
            set the both of the new node to the current 
            tail is the current tail node because xor of 0 (next node)
            with any number is the number itself
            """
            # Link current tail with new node
            new_node.both = get_pointer(self.tail) 

            self.tail.both ^= get_pointer(new_node) # XOR the current tail with the new node
            self.tail = new_node # set the tail to the new node


    def get(self, index):
        prev_addr = 0                                # start from the head
        current = self.head                          # start from the head
        for i in range(index):                       # iterate through the list   
            next_addr = prev_addr ^ current.both     # get the next address
            prev_addr = get_pointer(current)         # get the current address
            current = dereference_pointer(next_addr) # get the current node
        return current.value if current else None 



# Example usage:
xor_list = XORLinkedList()
xor_list.add(10)
xor_list.add(20)
xor_list.add(30)
xor_list.add(40)

print(xor_list.get(0))  # 10
print(xor_list.get(2))  # 30
