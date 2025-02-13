"""
LeetCode 173. Binary Search Tree Iterator

Problem Statement:
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. 
  The pointer should be initialized to a non-existent number smaller than any element in the BST.
- boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
- int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid, that is, there will be at least a next number in the in-order traversal when next() is called.

Example:
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 0 <= Node.val <= 10^6
- At most 10^5 calls will be made to hasNext, and next.
"""

from typing import Optional, List, Dict, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        """
        Initialize iterator.
        Time complexity: O(h) where h is height of tree
        Space complexity: O(h)
        """
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root: Optional[TreeNode]) -> None:
        """Helper function to push all leftmost nodes onto stack."""
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        Return next smallest number.
        Average time complexity: O(1)
        """
        topmost_node = self.stack.pop()

        # If right child exists, add all leftmost nodes of right subtree
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)

        return topmost_node.val

    def hasNext(self) -> bool:
        """
        Check if next number exists.
        Time complexity: O(1)
        """
        return len(self.stack) > 0


class BSTIteratorWithSteps:
    def __init__(self, root: Optional[TreeNode]):
        """Initialize iterator with step tracking."""
        self.stack = []
        self.steps = []
        self._leftmost_inorder(root)

        self.steps.append({
            "action": "Initialize",
            "stack_size": len(self.stack),
            "stack_values": [node.val for node in self.stack]
        })

    def _leftmost_inorder(self, root: Optional[TreeNode]) -> None:
        """Helper function with step tracking."""
        while root:
            self.stack.append(root)
            self.steps.append({
                "action": "Push to stack",
                "value": root.val,
                "stack_values": [node.val for node in self.stack]
            })
            root = root.left

    def next(self) -> Tuple[int, dict]:
        """Return next smallest number with step info."""
        topmost_node = self.stack.pop()
        step = {
            "action": "Next",
            "value": topmost_node.val,
            "stack_before": [node.val for node in self.stack + [topmost_node]],
            "stack_after": [node.val for node in self.stack]
        }

        if topmost_node.right:
            step["right_child"] = topmost_node.right.val
            self._leftmost_inorder(topmost_node.right)

        step["final_stack"] = [node.val for node in self.stack]
        self.steps.append(step)

        return topmost_node.val

    def hasNext(self) -> Tuple[bool, dict]:
        """Check for next number with step info."""
        result = len(self.stack) > 0
        step = {
            "action": "HasNext",
            "result": result,
            "stack_size": len(self.stack),
            "stack_values": [node.val for node in self.stack]
        }
        self.steps.append(step)
        return result

    def get_steps(self) -> List[dict]:
        """Return all recorded steps."""
        return self.steps


def create_tree(values: List[int], index: int = 0) -> Optional[TreeNode]:
    """Helper function to create a binary tree from list."""
    if not values or index >= len(values) or values[index] is None:
        return None

    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    return root


def visualize_steps(steps: List[dict]) -> None:
    """Helper function to visualize iterator steps."""
    print("\nIterator Steps:")
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}: {step['action']}")

        if step['action'] == "Initialize":
            print(f"Initial stack size: {step['stack_size']}")
            print(f"Stack values: {step['stack_values']}")

        elif step['action'] == "Push to stack":
            print(f"Pushed value: {step['value']}")
            print(f"Stack values: {step['stack_values']}")

        elif step['action'] == "Next":
            print(f"Returned value: {step['value']}")
            print(f"Stack before: {step['stack_before']}")
            print(f"Stack after: {step['stack_after']}")
            if "right_child" in step:
                print(f"Processing right child: {step['right_child']}")
            print(f"Final stack: {step['final_stack']}")

        elif step['action'] == "HasNext":
            print(f"Result: {step['result']}")
            print(f"Stack size: {step['stack_size']}")
            print(f"Stack values: {step['stack_values']}")


def test_bst_iterator():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "values": [7, 3, 15, None, None, 9, 20],
            "operations": ["next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
            "expected": [3, 7, True, 9, True, 15, True, 20, False],
            "description": "Basic case"
        },
        {
            "values": [1],
            "operations": ["next", "hasNext"],
            "expected": [1, False],
            "description": "Single node"
        },
        {
            "values": [3, 1, 4, None, 2],
            "operations": ["next", "next", "next", "next", "hasNext"],
            "expected": [1, 2, 3, 4, False],
            "description": "Balanced tree"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Tree values: {test_case['values']}")

        # Create tree
        root = create_tree(test_case['values'])

        # Test both implementations
        iterator1 = BSTIterator(root)
        iterator2 = BSTIteratorWithSteps(root)

        results1 = []
        results2 = []

        for op in test_case['operations']:
            if op == "next":
                results1.append(iterator1.next())
                results2.append(iterator2.next())
            else:  # hasNext
                results1.append(iterator1.hasNext())
                results2.append(iterator2.hasNext())

        print(f"\nResults:")
        print(f"Operations: {test_case['operations']}")
        print(f"Expected: {test_case['expected']}")
        print(f"Got: {results1}")

        visualize_steps(iterator2.get_steps())

        assert results1 == test_case['expected'], \
            f"Basic implementation failed. Expected {test_case['expected']}, got {results1}"
        assert results2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {results2}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_bst_iterator()
