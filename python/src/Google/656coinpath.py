"""
LeetCode 656 - Coin Path

Problem Statement:
You are given an array A of non-negative integers and an integer B. Starting at index 0, at each step, you can jump 
at most B steps forward. During each jump, you have to pay the cost A[i] where i is the index you land on.
If you land on an index i where A[i] = -1, you can't continue jumping and must stop there.
Find the path with minimum total cost from index 0 to the last index. If there are multiple paths with the same cost,
return the lexicographically smallest such path. If it's impossible to reach the last index, return an empty array.

Logic:
1. Use Dynamic Programming approach
2. For each position i, compute:
   - Minimum cost to reach the end from position i
   - Next jump position that leads to minimum cost path
3. Key optimizations:
   - Process array from right to left
   - Keep track of path using separate array
   - Early termination if last position is unreachable
   - Handle -1 positions as barriers

Time Complexity: O(n*B) where n is length of array
Space Complexity: O(n) for dp and path arrays
"""


class Solution:
    def cheapestJump(self, A: list[int], B: int) -> list[int]:
        n = len(A)
        if not A or A[-1] == -1:  # Handle edge cases
            return []

        # Initialize dp array for costs and path array for tracking jumps
        dp = [float('inf')] * n
        path = [-1] * n
        dp[-1] = A[-1]

        # Process from right to left
        for i in range(n - 2, -1, -1):
            if A[i] == -1:  # Can't jump from barrier
                continue
            # Try all possible jumps within range B
            for j in range(i + 1, min(n, i + B + 1)):
                # Update if we find cheaper path or same cost but lexicographically smaller
                if dp[j] != float('inf') and (dp[j] + A[i] < dp[i] or
                   (dp[j] + A[i] == dp[i] and j < path[i])):
                    dp[i] = dp[j] + A[i]
                    path[i] = j

        # Return empty array if no valid path exists
        if dp[0] == float('inf'):
            return []

        # Construct the path
        result = []
        pos = 0
        while pos != -1:
            result.append(pos + 1)  # Convert to 1-based indexing
            pos = path[pos]

        return result


def test_coin_path():
    solution = Solution()

    # Test cases
    test_cases = [
        {
            'A': [1, 2, 4, -1, 2],
            'B': 2,
            'expected': [1, 3, 5],
            'description': "Basic case with barrier"
        },
        {
            'A': [1, 2, 4, 1, 2],
            'B': 1,
            'expected': [1, 2, 3, 4, 5],
            'description': "Path with single step jumps"
        },
        {
            'A': [1, -1],
            'B': 1,
            'expected': [],
            'description': "Impossible path due to barrier"
        },
        {
            'A': [1, 2, 4, -1, 2, 3],
            'B': 3,
            'expected': [1, 3, 6],
            'description': "Path with varied jump lengths"
        }
    ]

    # Run tests
    for i, test in enumerate(test_cases, 1):
        result = solution.cheapestJump(test['A'], test['B'])
        print(f"\nTest Case {i} ({test['description']}):")
        print(f"Array: {test['A']}")
        print(f"Max Jump: {test['B']}")
        print(f"Expected Path: {test['expected']}")
        print(f"Actual Path: {result}")
        print(
            f"Status: {'PASSED' if result == test['expected'] else 'FAILED'}")


if __name__ == "__main__":
    test_coin_path()
