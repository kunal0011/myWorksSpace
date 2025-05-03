"""
LeetCode 331 - Verify Preorder Serialization of a Binary Tree

Problem Statement:
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, 
we record the node's value. If it is a null node, we record using a sentinel value '#'.

Given a string of comma-separated values preorder, return true if it is a correct preorder 
traversal serialization of a binary tree.

Example:
Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Explanation: This represents a valid binary tree with root value 9, left subtree [3,4,null,null,1,null,null], 
and right subtree [2,null,6,null,null].
"""

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Split the string by commas into nodes
        nodes = preorder.split(',')
        # Start with 1 available slot (for the root)
        slots = 1

        for node in nodes:
            # Every node consumes one slot
            slots -= 1

            # If at any point slots are negative, it's invalid
            if slots < 0:
                return False

            # Non-null nodes create two more slots (for their children)
            if node != '#':
                slots += 2

        # At the end, we should have used exactly all slots
        return slots == 0

def run_tests():
    solution = Solution()
    
    test_cases = [
        ("9,3,4,#,#,1,#,#,2,#,6,#,#", True),
        ("1,#", False),
        ("9,#,#,1", False),
        ("#", True),
        ("1,#,#", True),
        ("1,2,3,#,#,#,#", True),
        ("1,2,#,#,3,#,#", True)
    ]
    
    for i, (preorder, expected) in enumerate(test_cases, 1):
        result = solution.isValidSerialization(preorder)
        print(f"\nTest case {i}:")
        print(f"Input: {preorder}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")

if __name__ == "__main__":
    run_tests()
