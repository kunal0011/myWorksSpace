"""
LeetCode 533 - Lonely Pixel II

Given an m x n picture consisting of black 'B' and white 'W' pixels and an integer N, return the number 
of black pixels located at some specific coordinate that satisfy the following conditions:
1. The row and column both contain exactly N black pixels.
2. For all rows that have a black pixel at the coordinate, they should be exactly the same as the row.

Logic:
1. Count black pixels ('B') in each row and column
2. For each black pixel:
   - Check if its row and column both contain exactly N black pixels
   - Check if all rows containing a black pixel in the same column are identical
3. Each such black pixel contributes to the final count

Time Complexity: O(m*n*(m+n)) where m,n are dimensions of picture
Space Complexity: O(m*n) for storing row strings
"""


class Solution:
    def findBlackPixel(self, picture: list[list[str]], N: int) -> int:
        m, n = len(picture), len(picture[0])

        # Count the number of black pixels in each row and column
        row_count = [0] * m
        col_count = [0] * n
        rows = ["".join(row) for row in picture]

        # Count black pixels in rows and columns
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1

        # Find valid rows and count lonely pixels
        count = 0
        for i in range(m):
            if row_count[i] == N:
                for j in range(n):
                    if picture[i][j] == 'B' and col_count[j] == N:
                        # Check if all rows with a 'B' in column j are the same as row i
                        if rows.count(rows[i]) == N:
                            count += 1

        return count


def run_test_cases():
    solution = Solution()

    # Test cases
    test_cases = [
        # Test Case 1: Example from LeetCode
        {
            "picture": [
                ["W", "B", "W", "B", "B", "W"],
                ["W", "B", "W", "B", "B", "W"],
                ["W", "B", "W", "B", "B", "W"],
                ["W", "W", "B", "W", "B", "W"]
            ],
            "N": 3,
            "expected": 6
        },
        # Test Case 2: No valid pixels
        {
            "picture": [
                ["W", "B", "W"],
                ["W", "B", "W"],
                ["W", "W", "B"]
            ],
            "N": 2,
            "expected": 0
        },
        # Test Case 3: Single pixel case
        {
            "picture": [["B"]],
            "N": 1,
            "expected": 1
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.findBlackPixel(test["picture"], test["N"])
        print(f"\nTest Case {i}:")
        print("Picture:")
        for row in test["picture"]:
            print(row)
        print(f"N = {test['N']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == test['expected'] else '✗ Failed'}")


if __name__ == "__main__":
    run_test_cases()
