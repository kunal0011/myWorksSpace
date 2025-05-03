"""
LeetCode 430: Flatten a Multilevel Doubly Linked List

Problem Statement:
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer.
This child pointer may or may not point to a separate doubly linked list, also containing these special nodes.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list.
Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have ALL of their child pointers set to null.

Constraints:
- The number of nodes in the list is in the range [0, 2000]
- [1, 100] for Node.val
- Node.child can be null or pointing to a node in a different level
"""


class Node:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: 'Node') -> 'Node':
    if not head:
        return None

    # Use a stack to keep track of next pointers when we traverse down
    stack = []
    curr = head

    while curr or stack:
        if curr.child:
            # If there's a next node, push it to stack
            if curr.next:
                stack.append(curr.next)

            # Connect current node with child
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None  # Set child pointer to null

        elif not curr.next and stack:
            # If we've reached the end of current level and stack is not empty
            curr.next = stack.pop()
            curr.next.prev = curr

        curr = curr.next

    return head

# Helper function to create a linked list from a list of values and child references


def create_multilevel_list(values, child_refs=None):
    if not values:
        return None

    # Create nodes
    nodes = [Node(val) for val in values]

    # Connect nodes
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
        nodes[i+1].prev = nodes[i]

    # Add child references if provided
    if child_refs:
        for parent_idx, child_list in child_refs:
            nodes[parent_idx].child = create_multilevel_list(child_list)

    return nodes[0]

# Helper function to convert linked list to list for verification


def list_to_array(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

# Test driver


def run_tests():
    test_cases = [
        {
            "values": [1, 2, 3, 4, 5, 6],
            "child_refs": [(2, [7, 8, 9])],
            "expected": [1, 2, 3, 7, 8, 9, 4, 5, 6],
            "explanation": "Single child list at node 3"
        },
        {
            "values": [1, 2, 3, 4, 5],
            "child_refs": [(2, [6, 7, 8]), (6, [9, 10])],
            "expected": [1, 2, 3, 6, 9, 10, 7, 8, 4, 5],
            "explanation": "Nested child lists"
        },
        {
            "values": [1, 2],
            "child_refs": [],
            "expected": [1, 2],
            "explanation": "No child lists"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        # Create test input
        head = create_multilevel_list(test["values"], test["child_refs"])

        # Get result
        result = flatten(head)
        result_array = list_to_array(result)

        # Verify result
        status = "PASSED" if result_array == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(
            f"Input: {test['values']} with child references at {test['child_refs']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result_array}")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Flatten Multilevel Doubly Linked List problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Iterative Approach with Stack:
   - Use a stack to store next pointers when traversing down child lists
   - Process nodes one by one, handling three cases:
     a) Node has child: Connect current with child, store next in stack
     b) Node has no child but has next: Move to next node
     c) Node has no child and no next: Pop from stack if not empty

2. Key Points:
   - Maintain proper prev and next pointers
   - Set all child pointers to null
   - Handle transitions between levels using stack

3. Time and Space Complexity:
   - Time: O(N) where N is total number of nodes
   - Space: O(D) where D is maximum depth of child lists
   - Each node is visited exactly once
"""
