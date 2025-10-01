# Difficulty: Intermediate

# Description:
# Given the head of a singly linked list, reverse the list and return the new head.

# Requirements:

# Implement a class ListNode with attributes val and next.

# Write a function reverse_list(head: ListNode) -> ListNode.

# Solve iteratively (optional: add a recursive version later).

# Example Input/Output:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
# Output: 5 -> 4 -> 3 -> 2 -> 1 -> None




### Start of Code ###


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head: ListNode) -> ListNode:
    current = head # start from the head
    numList = []
    while current is not None:
        numList.append(current.val)
        if (current.next is not None):
            current = current.next 
        else:
            break
        
    for i in range(len(numList)):
        print(f"->{numList[-i-1]}")


# test the function (Solution 1: uncomment to test)
#  # Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
#  # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
# values = [1, 2, 3, 4, 5]
# head = ListNode(values[0])
# current = head
# for i in range(1, len(values)): # create a linked list with the values to test the function
#     current.next = ListNode(values[i])
#     current = current.next

# reverse_list(head)
 



# Solution 2: Checked the internet and found this solution


def reverse_list2(head: ListNode) -> ListNode:
    """
    Reverse a linked list iteratively using three pointers.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    prev = None
    current = head
    
    while current is not None:
        next_temp = current.next  # Save the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev forward
        current = next_temp       # Move current forward
    
    return prev  # prev is now the new head


def print_list(head: ListNode):
    """Helper function to print the linked list."""
    current = head
    while current is not None:
        print(f"{current.val}", end="")
        if current.next is not None:
            print(" -> ", end="")
        current = current.next
    print(" -> None")




# test the function
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
# Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
values = [1, 2, 3, 4, 5]
head = ListNode(values[0])
current = head
for i in range(1, len(values)): # create a linked list with the values to test the function
    current.next = ListNode(values[i])
    current = current.next


print("\n____________________________________________")
print("Solution 2:")
print("Original list:")
print_list(head)

reversed_head = reverse_list2(head)

print("Reversed list:")
print_list(reversed_head)