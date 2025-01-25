"""
LeetCode 85. Maximal Rectangle

Problem Statement:
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle 
containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
- rows == matrix.length
- cols == matrix[i].length
- 1 <= row, cols <= 200
- matrix[i][j] is '0' or '1'
"""


class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        def largest_rectangle_area(heights: list[int]) -> int:
            """Helper function to find largest rectangle in histogram"""
            heights.append(0)
            stack = [-1]
            max_area = 0

            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

            heights.pop()
            return max_area

        # Convert matrix rows to histogram heights
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        # Process each row
        for row in range(rows):
            # Update heights
            for col in range(cols):
                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            # Find largest rectangle in current histogram
            max_area = max(max_area, largest_rectangle_area(heights))

        return max_area


def visualize_matrix(matrix: list[list[str]], highlight: tuple = None) -> None:
    """Helper function to visualize binary matrix with optional highlight"""
    if not matrix or not matrix[0]:
        print("Empty matrix")
        return

    rows, cols = len(matrix), len(matrix[0])

    # Print column numbers
    print("   ", end="")
    for j in range(cols):
        print(f"{j:2}", end=" ")
    print("\n   " + "---" * cols)

    # Print matrix with row numbers
    for i in range(rows):
        print(f"{i:2}|", end=" ")
        for j in range(cols):
            if highlight and i >= highlight[0] and i <= highlight[2] and \
               j >= highlight[1] and j <= highlight[3]:
                print("\033[92m" + matrix[i][j] + "\033[0m", end="  ")
            else:
                print(matrix[i][j], end="  ")
        print()


def test_maximal_rectangle():
    solution = Solution()

    test_cases = [
        {
            "matrix": [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]
            ],
            "expected": 6,
            "description": "Standard case"
        },
        {
            "matrix": [["0"]],
            "expected": 0,
            "description": "Single zero"
        },
        {
            "matrix": [["1"]],
            "expected": 1,
            "description": "Single one"
        },
        {
            "matrix": [
                ["1", "1", "1"],
                ["1", "1", "1"]
            ],
            "expected": 6,
            "description": "All ones"
        },
        {
            "matrix": [
                ["0", "0"],
                ["0", "0"]
            ],
            "expected": 0,
            "description": "All zeros"
        },
        {
            "matrix": [
                ["1", "0", "1"],
                ["1", "1", "1"],
                ["1", "1", "1"]
            ],
            "expected": 6,
            "description": "Complex pattern"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        matrix = test_case["matrix"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print("Matrix:")
        visualize_matrix(matrix)

        result = solution.maximalRectangle(matrix)

        assert result == expected, \
            f"Expected {expected}, but got {result}"
        print(f"✓ Test case passed! Maximum area: {result}")


if __name__ == "__main__":
    test_maximal_rectangle()
    print("\nAll test cases passed! 🎉")
