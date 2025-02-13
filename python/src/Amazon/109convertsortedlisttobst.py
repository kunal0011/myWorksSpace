"""
LeetCode 109. Convert Sorted List to Binary Search Tree

Problem Statement:
Given the head of a singly linked list where elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-10,5,null,-3,null,9], which represents the shown height balanced BST.
    0
   / \
 -3   9
 /   /
-10  5

Example 2:
Input: head = []
Output: []

Constraints:
- The number of nodes in head is in the range [0, 2 * 10^4]
- -10^5 <= Node.val <= 10^5
"""

from collections import deque
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """Convert sorted linked list to balanced BST using slow/fast pointer approach"""
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        # Find the middle node using slow/fast pointers
        prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Cut the list into two parts
        if prev:
            prev.next = None

        # Create root node from middle value
        root = TreeNode(slow.val)

        # Recursively build left and right subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root

    def sortedListToBSTArray(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """Alternative solution using array conversion"""
        # Convert linked list to array
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        def arrayToBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(values[mid])

            root.left = arrayToBST(left, mid - 1)
            root.right = arrayToBST(mid + 1, right)

            return root

        return arrayToBST(0, len(values) - 1)


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Helper function to create linked list from list of values"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper function to convert linked list to array"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def tree_to_list(root: TreeNode) -> List[Optional[int]]:
    """Convert binary tree to level-order list representation"""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def visualize_tree(root: TreeNode, level: int = 0, prefix: str = "Root: ") -> None:
    """Helper function to visualize binary tree with balance indicators"""
    if not root:
        print("  " * level + prefix + "None")
        return

    def get_height(node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    left_height = get_height(root.left)
    right_height = get_height(root.right)
    balance = right_height - left_height

    print("  " * level + prefix + f"{root.val} (balance: {balance})")
    if root.left or root.right:
        visualize_tree(root.left, level + 1, "L--- ")
        visualize_tree(root.right, level + 1, "R--- ")


def is_balanced(root: TreeNode) -> bool:
    """Check if tree is height-balanced"""
    def check_height(node: TreeNode) -> int:
        if not node:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return check_height(root) != -1


def test_sorted_list_to_bst():
    solution = Solution()

    test_cases = [
        {
            "values": [-10, -3, 0, 5, 9],
            "description": "Standard case"
        },
        {
            "values": [1, 3],
            "description": "Two elements"
        },
        {
            "values": [1],
            "description": "Single element"
        },
        {
            "values": [],
            "description": "Empty list"
        },
        {
            "values": [1, 2, 3, 4, 5, 6, 7],
            "description": "Odd number of elements"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        values = test_case["values"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        head = create_linked_list(values)
        print(f"Input list: {linked_list_to_list(head)}")

        # Test both solutions
        root_pointer = solution.sortedListToBST(create_linked_list(values))
        root_array = solution.sortedListToBSTArray(create_linked_list(values))

        print("\nPointer approach tree:")
        visualize_tree(root_pointer)
        print("\nArray approach tree:")
        visualize_tree(root_array)

        # Verify both trees are height-balanced
        assert is_balanced(root_pointer), "Pointer solution is not balanced"
        assert is_balanced(root_array), "Array solution is not balanced"

        # Verify both trees contain all elements
        result_pointer = tree_to_list(root_pointer)
        result_array = tree_to_list(root_array)

        assert sorted(result_pointer) == sorted(values), \
            f"Pointer solution missing elements: {set(values) - set(result_pointer)}"
        assert sorted(result_array) == sorted(values), \
            f"Array solution missing elements: {set(values) - set(result_array)}"

        print("✓ Test case passed!")


if __name__ == "__main__":
    test_sorted_list_to_bst()
    print("\nAll test cases passed! 🎉")
