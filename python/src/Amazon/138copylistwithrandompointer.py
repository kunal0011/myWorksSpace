"""
LeetCode 138. Copy List with Random Pointer

Problem Statement:
A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied
list such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random is null or pointing to a node in the linked list
"""

from typing import Optional, List, Dict, Set


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        O(1) space solution using interweaving technique.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not head:
            return None

        # Step 1: Create interweaved list
        curr = head
        while curr:
            # Create copy node
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # Step 2: Set random pointers for copy nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate original and copy lists
        dummy = Node(0)
        copy_curr = dummy
        curr = head

        while curr:
            # Extract copy node
            copy_curr.next = curr.next
            copy_curr = copy_curr.next

            # Restore original list
            curr.next = curr.next.next
            curr = curr.next

        return dummy.next

    def copyRandomListWithMap(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Hash map solution for clarity.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not head:
            return None

        # Step 1: Create copy nodes with hash map
        node_map = {}
        curr = head

        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Set next and random pointers
        curr = head
        while curr:
            if curr.next:
                node_map[curr].next = node_map[curr.next]
            if curr.random:
                node_map[curr].random = node_map[curr.random]
            curr = curr.next

        return node_map[head]


def create_linked_list(values: List[List[int]]) -> Optional[Node]:
    """Helper function to create linked list from list of [value, random_index]."""
    if not values:
        return None

    # Create nodes
    nodes = []
    for val, _ in values:
        nodes.append(Node(val))

    # Set next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Set random pointers
    for i, (_, random_idx) in enumerate(values):
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]

    return nodes[0]


def get_list_representation(head: Optional[Node]) -> List[List[int]]:
    """Helper function to convert linked list to list representation."""
    if not head:
        return []

    # Create node to index mapping
    node_to_index = {}
    curr = head
    index = 0

    while curr:
        node_to_index[curr] = index
        curr = curr.next
        index += 1

    # Create list representation
    result = []
    curr = head
    while curr:
        random_idx = node_to_index[curr.random] if curr.random else None
        result.append([curr.val, random_idx])
        curr = curr.next

    return result


def verify_deep_copy(original: Optional[Node], copy: Optional[Node]) -> bool:
    """Helper function to verify deep copy correctness."""
    if not original and not copy:
        return True
    if not original or not copy:
        return False

    # Track visited nodes to handle cycles
    visited_orig = set()
    visited_copy = set()

    curr_orig = original
    curr_copy = copy

    while curr_orig and curr_copy:
        # Check for cycles
        if curr_orig in visited_orig or curr_copy in visited_copy:
            return curr_orig in visited_orig and curr_copy in visited_copy

        # Check values
        if curr_orig.val != curr_copy.val:
            return False

        # Check random pointers
        if (curr_orig.random is None) != (curr_copy.random is None):
            return False
        if curr_orig.random and curr_orig.random.val != curr_copy.random.val:
            return False

        visited_orig.add(curr_orig)
        visited_copy.add(curr_copy)
        curr_orig = curr_orig.next
        curr_copy = curr_copy.next

    return curr_orig is None and curr_copy is None


def visualize_list(head: Optional[Node]) -> None:
    """Helper function to visualize linked list structure."""
    if not head:
        print("Empty list")
        return

    # Create node to index mapping
    node_to_index = {}
    curr = head
    index = 0

    while curr:
        node_to_index[curr] = index
        curr = curr.next
        index += 1

    # Print list structure
    print("\nList structure:")
    print("Index | Value | Random -> (Index, Value)")
    print("-" * 45)

    curr = head
    index = 0
    while curr:
        random_info = f"({node_to_index[curr.random]}, {curr.random.val})" if curr.random else "null"
        print(f"{index:5d} | {curr.val:5d} | -> {random_info}")
        curr = curr.next
        index += 1


def test_copy_random_list():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "values": [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            "description": "Standard case with various random pointers"
        },
        {
            "values": [[1, 1], [2, 1]],
            "description": "Circular random pointers"
        },
        {
            "values": [[3, None], [3, 0], [3, None]],
            "description": "Same values with different random pointers"
        },
        {
            "values": [],
            "description": "Empty list"
        },
        {
            "values": [[1, None]],
            "description": "Single node"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")

        # Create original list
        original = create_linked_list(test_case['values'])
        print("\nOriginal list:")
        visualize_list(original)

        # Test both implementations
        copy1 = solution.copyRandomList(original)
        copy2 = solution.copyRandomListWithMap(original)

        print("\nCopied list (O(1) space):")
        visualize_list(copy1)
        print("\nCopied list (Hash map):")
        visualize_list(copy2)

        # Verify deep copies
        is_valid1 = verify_deep_copy(original, copy1)
        is_valid2 = verify_deep_copy(original, copy2)

        # Convert to list representation for comparison
        result1 = get_list_representation(copy1)
        result2 = get_list_representation(copy2)

        assert is_valid1, "O(1) space solution failed deep copy verification"
        assert is_valid2, "Hash map solution failed deep copy verification"
        assert result1 == test_case['values'], \
            f"O(1) space solution failed. Expected {test_case['values']}, got {result1}"
        assert result2 == test_case['values'], \
            f"Hash map solution failed. Expected {test_case['values']}, got {result2}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_copy_random_list()
