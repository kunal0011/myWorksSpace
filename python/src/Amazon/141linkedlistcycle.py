"""
LeetCode 141. Linked List Cycle

Problem Statement:
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
- The number of nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list
"""

from typing import Optional, List, Set, Tuple


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd's Cycle-Finding Algorithm (Tortoise and Hare).
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

    def hasCycleWithDetails(self, head: Optional[ListNode]) -> Tuple[bool, List[int]]:
        """
        Returns both result and path taken by pointers.
        Time complexity: O(n)
        Space complexity: O(n) for tracking path
        """
        if not head or not head.next:
            return False, []

        # Track path for visualization
        path = []
        visited = set()
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False, path

            # Record positions
            path.append((slow.val, fast.val))
            visited.add(id(slow))
            visited.add(id(fast))

            slow = slow.next
            fast = fast.next.next

            if id(slow) in visited or (fast and id(fast) in visited):
                path.append((slow.val, fast.val if fast else None))
                return True, path

        path.append((slow.val, fast.val))
        return True, path


def create_linked_list(values: List[int], pos: int) -> Optional[ListNode]:
    """Helper function to create linked list with cycle."""
    if not values:
        return None

    # Create nodes
    nodes = []
    for val in values:
        nodes.append(ListNode(val))

    # Connect nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create cycle if pos is valid
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0]


def visualize_path(path: List[Tuple[int, int]]) -> None:
    """Helper function to visualize tortoise and hare movement."""
    print("\nPointer Movement:")
    print("Step | Tortoise | Hare")
    print("-" * 25)

    for i, (slow, fast) in enumerate(path):
        print(f"{i:4d} | {slow:8d} | {fast if fast is not None else 'None':4}")


def test_linked_list_cycle():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "values": [3, 2, 0, -4],
            "pos": 1,
            "expected": True,
            "description": "Standard cycle"
        },
        {
            "values": [1, 2],
            "pos": 0,
            "expected": True,
            "description": "Small cycle"
        },
        {
            "values": [1],
            "pos": -1,
            "expected": False,
            "description": "Single node"
        },
        {
            "values": [1, 2, 3, 4, 5],
            "pos": -1,
            "expected": False,
            "description": "No cycle"
        },
        {
            "values": [1, 2, 3, 4, 5],
            "pos": 4,
            "expected": True,
            "description": "Cycle at end"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Values: {test_case['values']}")
        print(f"Cycle position: {test_case['pos']}")

        # Create linked list
        head = create_linked_list(test_case['values'], test_case['pos'])

        # Test both implementations
        result1 = solution.hasCycle(head)
        result2, path = solution.hasCycleWithDetails(head)

        print(f"\nResults:")
        print(f"Has cycle: {result1}")

        if path:
            visualize_path(path)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Detailed approach failed. Expected {test_case['expected']}, got {result2}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_linked_list_cycle()
