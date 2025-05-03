"""
LeetCode 422: Valid Word Square

Problem Statement:
Given an array of strings words, return true if it forms a valid word square.
A sequence of strings forms a valid word square if the kth row and column read the 
exact same string, where 0 ≤ k < max(numRows, numCols).

Note:
- The number of words given is at least 1 and does not exceed 500.
- Word length will be at least 1 and does not exceed 500.
- Each word contains only lowercase English letters.

Examples:
Input: ["abcd","bnrt","crmy","dtye"]
Output: true
Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".
"""


def validWordSquare(words: list[str]) -> bool:
    if not words:
        return True

    # Get the number of rows
    rows = len(words)

    # Check each position (i,j) matches (j,i)
    for i in range(rows):
        for j in range(len(words[i])):
            # If j is beyond the number of rows, or
            # i is beyond the length of words[j], or
            # characters don't match
            if (j >= rows or                         # More columns than rows
                # Row longer than corresponding column
                i >= len(words[j]) or
                    words[i][j] != words[j][i]):        # Characters don't match
                return False

    # Check if any row is longer than the number of rows
    for i in range(rows):
        if len(words[i]) > rows:
            return False

    return True

# Test driver


def run_tests():
    test_cases = [
        {
            "words": ["abcd", "bnrt", "crmy", "dtye"],
            "expected": True,
            "explanation": "Perfect word square"
        },
        {
            "words": ["ball", "area", "lead", "lady"],
            "expected": False,
            "explanation": "Characters don't match symmetrically"
        },
        {
            "words": ["abc", "bde", "cef"],
            "expected": True,
            "explanation": "Valid 3x3 word square"
        },
        {
            "words": ["abcd", "bnrt", "crm", "dt"],
            "expected": True,
            "explanation": "Valid irregular word square"
        },
        {
            "words": ["ball", "asee", "let"],
            "expected": False,
            "explanation": "Invalid lengths"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = validWordSquare(test["words"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input words: {test['words']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Valid Word Square problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Key Approach:
   - Check if each position (i,j) matches with position (j,i)
   - Handle edge cases where lengths don't match

2. Main Algorithm Steps:
   - For each position (i,j):
     a) Check if j is within bounds (not more columns than rows)
     b) Check if i is within bounds of words[j] (symmetry check)
     c) Check if characters at (i,j) and (j,i) match
   - Also verify no row is longer than number of rows

3. Edge Cases Handled:
   - Empty input
   - Irregular lengths
   - Out of bounds access
   - Asymmetric matrices

Time Complexity: O(N*M) where N is number of words and M is max length of words
Space Complexity: O(1) as we only use constant extra space
"""
