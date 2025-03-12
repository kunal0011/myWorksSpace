"""
LeetCode 430 - Flatten a Multilevel Doubly Linked List

Problem Statement:
-----------------
You are given a doubly linked list, which contains nodes that have a next pointer, 
a previous pointer, and an additional child pointer. This child pointer may or may 
not point to a separate doubly linked list, with its own next, previous, and child 
pointers. These child lists may have one or more children of their own, and so on, 
to produce a multilevel data structure.

Flatten the list so that all nodes appear in a single-level, doubly linked list. 
Let curr be a node with a child list. The nodes in the child list should appear 
after curr and before curr.next in the flattened list.

Key Points:
----------
1. The linked list is doubly linked (has both next and prev pointers)
2. Nodes may have child pointers to other doubly linked lists
3. Child lists should be flattened between current node and its next
4. All child pointers must be null in the final list
5. The relative order of nodes in each level should be preserved

Examples:
--------
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Input: head = [1,2,null,3]
Output: [1,2,3]

Constraints:
-----------
* The number of nodes in the list is in the range [0, 1000]
* 1 <= Node.val <= 10^5
"""

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        """
        Initialize a node in the multilevel doubly linked list
        
        Args:
            val: The value stored in the node
            prev: Reference to the previous node
            next: Reference to the next node
            child: Reference to the child list
        """
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        """
        Flatten a multilevel doubly linked list into a single-level doubly linked list.
        
        Algorithm:
        1. Use DFS to process each level
        2. When encountering a child, flatten it recursively
        3. Insert the flattened child list between current node and its next
        4. Update all necessary pointers (prev, next, child)
        
        Time Complexity: O(N) where N is total number of nodes
        Space Complexity: O(D) where D is maximum depth of child lists (recursion stack)
        """
        def flatten_dfs(node):
            """
            Helper function to flatten the list and return the tail of flattened list
            """
            curr = node
            last = None

            while curr:
                next_node = curr.next

                # Process child list if it exists
                if curr.child:
                    child_tail = flatten_dfs(curr.child)

                    # Connect current node with child
                    curr.next = curr.child
                    curr.child.prev = curr
                    curr.child = None

                    # Connect child tail with next node
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail

                    last = child_tail
                else:
                    last = curr

                curr = next_node

            return last

        flatten_dfs(head)
        return head


def create_test_list(values, child_indices=None):
    """
    Create a multilevel doubly linked list from values and child relationships
    
    Args:
        values: List of values for nodes
        child_indices: Dictionary mapping node indices to their child list indices
    Returns:
        Head of the created multilevel linked list
    """
    if not values:
        return None

    # Create all nodes
    nodes = [Node(val) for val in values]
    
    # Connect next and prev pointers
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
        nodes[i+1].prev = nodes[i]
    
    # Add child connections if specified
    if child_indices:
        for parent_idx, child_idx in child_indices.items():
            nodes[parent_idx].child = nodes[child_idx]
    
    return nodes[0]

def list_to_array(head):
    """Convert linked list to array for easy comparison"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_flatten_list():
    """
    Test driver for the flatten multilevel doubly linked list problem
    """
    test_cases = [
        # Test case 1: Basic multilevel list
        {
            'values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'child_indices': {2: 6, 7: 8},
            'expected': [1, 2, 3, 7, 8, 9, 10, 4, 5, 6]
        },
        # Test case 2: Single level list
        {
            'values': [1, 2, 3],
            'child_indices': {},
            'expected': [1, 2, 3]
        },
        # Test case 3: Multiple levels
        {
            'values': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'child_indices': {1: 4, 5: 7},
            'expected': [1, 2, 5, 6, 7, 8, 9, 3, 4]
        },
        # Test case 4: Single node with child
        {
            'values': [1, 2],
            'child_indices': {0: 1},
            'expected': [1, 2]
        }
    ]
    
    solution = Solution()
    
    for i, test_case in enumerate(test_cases, 1):
        # Create test list
        head = create_test_list(test_case['values'], test_case['child_indices'])
        
        # Flatten the list
        flattened = solution.flatten(head)
        
        # Convert to array for comparison
        result = list_to_array(flattened)
        expected = test_case['expected']
        
        # Check result
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input structure: {test_case['values']} with child connections: {test_case['child_indices']}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_flatten_list()
