"""
LeetCode 237 - Delete Node in a Linked List

Problem Statement:
Write a function to delete a node in a singly-linked list. You will not be given access to the 
head of the list, instead you will be given access to the node to be deleted directly. It is 
guaranteed that the node to be deleted is not a tail node in the list.

Solution Logic:
1. Since we don't have access to the head:
   - Copy the next node's value to current node
   - Skip the next node in the list
2. This effectively deletes the current node by making it a copy of the next node
3. Time: O(1), Space: O(1)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        # Copy next node's value and skip it
        node.val = node.next.val
        node.next = node.next.next

def create_linked_list(values):
    """Helper function to create linked list."""
    dummy = ListNode(0)
    curr = dummy
    nodes = []  # Store nodes for testing
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)
    return dummy.next, nodes

def print_list(head):
    """Helper function to print linked list."""
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    return "->".join(values)

def test_delete_node():
    # Test Case 1: Delete middle node
    head1, nodes1 = create_linked_list([4,5,1,9])
    print("Test 1: Delete middle node")
    print(f"Original list: {print_list(head1)}")
    solution = Solution()
    solution.deleteNode(nodes1[1])  # Delete node with value 5
    print(f"After deleting 5: {print_list(head1)}")  # Expected: 4->1->9
    
    # Test Case 2: Delete first node
    head2, nodes2 = create_linked_list([4,5,1,9])
    print("\nTest 2: Delete first node")
    print(f"Original list: {print_list(head2)}")
    solution.deleteNode(nodes2[0])  # Delete node with value 4
    print(f"After deleting 4: {print_list(head2)}")  # Expected: 5->1->9
    
    # Test Case 3: Delete second to last node
    head3, nodes3 = create_linked_list([1,2,3,4])
    print("\nTest 3: Delete second to last node")
    print(f"Original list: {print_list(head3)}")
    solution.deleteNode(nodes3[2])  # Delete node with value 3
    print(f"After deleting 3: {print_list(head3)}")  # Expected: 1->2->4

if __name__ == "__main__":
    test_delete_node()
