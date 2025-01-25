"""
LeetCode 96. Unique Binary Search Trees

Problem Statement:
Given an integer n, return the number of structurally unique BST's (binary search trees) 
which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5
Explanation: Given n = 3, there are a total of 5 unique BST's:
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Example 2:
Input: n = 1
Output: 1

Constraints:
- 1 <= n <= 19
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] represents number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty tree
        dp[1] = 1  # Single node

        # Build up from smaller subproblems
        for nodes in range(2, n + 1):
            # Try each value as root
            for root in range(1, nodes + 1):
                left = root - 1        # Nodes in left subtree
                right = nodes - root   # Nodes in right subtree
                dp[nodes] += dp[left] * dp[right]

        return dp[n]


def visualize_catalan_numbers(n: int) -> None:
    """Helper function to visualize Catalan numbers and their relationship"""
    print("\nCatalan Numbers Sequence:")
    print("n  | Count | Formula")
    print("-" * 30)

    for i in range(n + 1):
        # Calculate Catalan number using dynamic programming
        dp = [0] * (i + 1)
        dp[0] = 1

        for j in range(1, i + 1):
            for k in range(j):
                dp[j] += dp[k] * dp[j - 1 - k]

        formula = f"C({i}) = {dp[i]}"
        if i > 0:
            terms = []
            for k in range(i):
                terms.append(f"C({k})*C({i-1-k})")
            formula += f" = " + " + ".join(terms)

        print(f"{i:2d} | {dp[i]:5d} | {formula}")


def test_num_trees():
    solution = Solution()

    test_cases = [
        {
            "n": 1,
            "expected": 1,
            "description": "Single node"
        },
        {
            "n": 2,
            "expected": 2,
            "description": "Two nodes"
        },
        {
            "n": 3,
            "expected": 5,
            "description": "Three nodes"
        },
        {
            "n": 4,
            "expected": 14,
            "description": "Four nodes"
        },
        {
            "n": 5,
            "expected": 42,
            "description": "Five nodes"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        n = test_case["n"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Input: n = {n}")

        # Visualize Catalan numbers up to n
        visualize_catalan_numbers(n)

        result = solution.numTrees(n)
        print(f"\nNumber of unique BSTs: {result}")

        assert result == expected, \
            f"Expected {expected}, but got {result}"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_num_trees()
    print("\nAll test cases passed! 🎉")
