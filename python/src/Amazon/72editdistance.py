"""
LeetCode 72. Edit Distance

Problem Statement:
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Create DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize first row and column
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j],    # deletion
                        dp[i][j-1],    # insertion
                        dp[i-1][j-1]   # replacement
                    ) + 1

        return dp[m][n]


def print_dp_table(dp: list, word1: str, word2: str, highlight: tuple = None) -> None:
    """Helper function to print DP table with optional highlighting"""
    m, n = len(dp), len(dp[0])

    # Print header
    print("     ", end="")
    print("ε  ", end="")
    for char in word2:
        print(f"{char}  ", end="")
    print()

    # Print table with row headers
    for i in range(m):
        if i == 0:
            print("ε ", end=" ")
        else:
            print(f"{word1[i-1]} ", end=" ")

        for j in range(n):
            if highlight and (i, j) == highlight:
                print(f"\033[92m{dp[i][j]:2}\033[0m", end=" ")
            else:
                print(f"{dp[i][j]:2}", end=" ")
        print()


def explain_edit_distance(word1: str, word2: str) -> None:
    """
    Function to explain the edit distance calculation process step by step
    """
    print(f"\nCalculating edit distance between '{word1}' and '{word2}'")
    print("=" * 50)

    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    print("\nInitial DP table:")
    print_dp_table(dp, word1, word2)

    # Fill DP table with explanation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(f"\nComparing {word1[i-1]} with {word2[j-1]}:")

            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                print(f"Characters match, copying diagonal value: {dp[i][j]}")
            else:
                deletion = dp[i-1][j]
                insertion = dp[i][j-1]
                replacement = dp[i-1][j-1]
                dp[i][j] = min(deletion, insertion, replacement) + 1
                print(f"Characters don't match, taking minimum of:")
                print(f"- Deletion: {deletion}")
                print(f"- Insertion: {insertion}")
                print(f"- Replacement: {replacement}")
                print(f"Adding 1 to get: {dp[i][j]}")

            print("\nCurrent DP table:")
            print_dp_table(dp, word1, word2, (i, j))

    print(f"\nFinal edit distance: {dp[m][n]}")
    return dp[m][n]


def test_edit_distance():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "word1": "horse",
            "word2": "ros",
            "expected": 3,
            "description": "Basic case"
        },
        {
            "word1": "intention",
            "word2": "execution",
            "expected": 5,
            "description": "Longer strings"
        },
        {
            "word1": "",
            "word2": "a",
            "expected": 1,
            "description": "Empty string to single char"
        },
        {
            "word1": "abc",
            "word2": "abc",
            "expected": 0,
            "description": "Identical strings"
        },
        {
            "word1": "plasma",
            "word2": "altruism",
            "expected": 6,
            "description": "Different lengths"
        },
        {
            "word1": "",
            "word2": "",
            "expected": 0,
            "description": "Both empty"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        word1 = test_case["word1"]
        word2 = test_case["word2"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: word1 = '{word1}', word2 = '{word2}'")

        result = solution.minDistance(word1, word2)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_edit_distance()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_edit_distance("horse", "ros")
        explain_edit_distance("cat", "cut")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
