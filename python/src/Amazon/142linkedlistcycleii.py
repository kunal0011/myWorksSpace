"""
LeetCode 142. Linked List Cycle II

Problem Statement:
Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: -1
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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Floyd's Cycle-Finding Algorithm (Tortoise and Hare).
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not head or not head.next:
            return None

        # Phase 1: Detect cycle using two pointers
        slow = head
        fast = head
        has_cycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return None

        # Phase 2: Find cycle start
        # Move one pointer to head and advance both by one
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

    def detectCycleWithPath(self, head: Optional[ListNode]) -> Tuple[Optional[ListNode], List[Tuple[int, int]], List[int]]:
        """
        Returns cycle start node, path taken by pointers, and cycle path.
        Time complexity: O(n)
        Space complexity: O(n) for tracking paths
        """
        if not head or not head.next:
            return None, [], []

        # Track paths for visualization
        detection_path = []
        cycle_path = []

        # Phase 1: Detect cycle
        slow = head
        fast = head
        has_cycle = False

        while fast and fast.next:
            detection_path.append((slow.val, fast.val))
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                detection_path.append((slow.val, fast.val))
                break

        if not has_cycle:
            return None, detection_path, []

        # Phase 2: Find cycle start
        slow = head
        while slow != fast:
            cycle_path.append(slow.val)
            slow = slow.next
            fast = fast.next

        # Add cycle nodes
        cycle_path.append(slow.val)
        curr = slow.next
        while curr != slow:
            cycle_path.append(curr.val)
            curr = curr.next

        return slow, detection_path, cycle_path


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


def visualize_detection(path: List[Tuple[int, int]], cycle_path: List[int]) -> None:
    """Helper function to visualize cycle detection process."""
    print("\nCycle Detection Process:")
    print("Step | Tortoise | Hare")
    print("-" * 25)

    for i, (slow, fast) in enumerate(path):
        print(f"{i:4d} | {slow:8d} | {fast:4d}")

    if cycle_path:
        print("\nCycle Structure:")
        print("Cycle start value:", cycle_path[0])
        print("Cycle path:", " -> ".join(map(str, cycle_path)))
        print("Cycle length:", len(cycle_path))


def test_detect_cycle():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "values": [3, 2, 0, -4],
            "pos": 1,
            "expected_val": 2,
            "description": "Standard cycle"
        },
        {
            "values": [1, 2],
            "pos": 0,
            "expected_val": 1,
            "description": "Small cycle"
        },
        {
            "values": [1],
            "pos": -1,
            "expected_val": None,
            "description": "Single node"
        },
        {
            "values": [1, 2, 3, 4, 5],
            "pos": -1,
            "expected_val": None,
            "description": "No cycle"
        },
        {
            "values": [1, 2, 3, 4, 5],
            "pos": 2,
            "expected_val": 3,
            "description": "Cycle in middle"
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
        result1 = solution.detectCycle(head)
        result2, detection_path, cycle_path = solution.detectCycleWithPath(
            head)

        print(f"\nResults:")
        if result1:
            print(f"Cycle starts at node with value: {result1.val}")
        else:
            print("No cycle detected")

        visualize_detection(detection_path, cycle_path)

        # Verify results
        expected = test_case['expected_val']
        result1_val = result1.val if result1 else None
        result2_val = result2.val if result2 else None

        assert result1_val == expected, \
            f"Basic approach failed. Expected {expected}, got {result1_val}"
        assert result2_val == expected, \
            f"Path tracking failed. Expected {expected}, got {result2_val}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_detect_cycle()
