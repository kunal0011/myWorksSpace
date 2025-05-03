"""
LeetCode 531 - Lonely Pixel I

Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of black lonely pixels.
A black lonely pixel is a character 'B' that located at a specific position where the same row and same column 
don't have any other black pixels.

Logic:
1. Count 'B's in each row and column using arrays
2. For each black pixel:
   - Check if it's the only black pixel in its row (row count = 1)
   - Check if it's the only black pixel in its column (column count = 1)
3. Each such pixel contributes to the final count

Time Complexity: O(m*n) where m,n are dimensions of picture
Space Complexity: O(m+n) for row and column counters
"""

class Solution:
    def findLonelyPixel(self, picture: list[list[str]]) -> int:
        if not picture or not picture[0]:
            return 0
            
        m, n = len(picture), len(picture[0])
        row_count = [0] * m
        col_count = [0] * n
        
        # Count black pixels in each row and column
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Count lonely pixels
        lonely_count = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                    lonely_count += 1
                    
        return lonely_count

def run_test_cases():
    solution = Solution()
    test_cases = [
        # Test Case 1: Example with multiple lonely pixels
        {
            "picture": [
                ["W", "W", "B"],
                ["W", "B", "W"],
                ["B", "W", "W"]
            ],
            "expected": 3
        },
        # Test Case 2: No lonely pixels
        {
            "picture": [
                ["B", "B"],
                ["B", "B"]
            ],
            "expected": 0
        },
        # Test Case 3: Single pixel
        {
            "picture": [["B"]],
            "expected": 1
        },
        # Test Case 4: Empty picture
        {
            "picture": [],
            "expected": 0
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = solution.findLonelyPixel(test["picture"])
        print(f"\nTest Case {i}:")
        print("Picture:")
        for row in test["picture"]:
            print(row)
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == test['expected'] else '✗ Failed'}")

if __name__ == "__main__":
    run_test_cases()
