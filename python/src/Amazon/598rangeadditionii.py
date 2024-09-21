from typing import List


class Solution:
    def maxCount(self, m: int, n: int, operations: List[List[int]]) -> int:
        if not operations:
            return m * n

        # Initialize min_a and min_b to maximum possible values
        min_a = m
        min_b = n

        for a, b in operations:
            min_a = min(min_a, a)
            min_b = min(min_b, b)

        return min_a * min_b


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    m1, n1, operations1 = 3, 3, [[2, 2], [3, 3]]
    print(sol.maxCount(m1, n1, operations1))  # Output: 4

    # Test case 2
    m2, n2, operations2 = 3, 3, [[2, 2], [3, 3], [1, 1]]
    print(sol.maxCount(m2, n2, operations2))  # Output: 1
