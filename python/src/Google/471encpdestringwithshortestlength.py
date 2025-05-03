"""
LeetCode 471: Encode String with Shortest Length

Problem Statement:
Given a string s, encode the string such that its encoded length is the shortest.
The encoding rule is: k[encoded_string], where the encoded_string inside the square 
brackets is being repeated exactly k times.

Note:
- k will be a positive integer.
- If an encoding process does not make the string shorter, then do not encode it.
- If there are several solutions, return any of them.

Constraints:
- 1 <= s.length <= 150
- s consists of lowercase English letters.
"""


def encode(s: str) -> str:
    n = len(s)
    dp = [['' for _ in range(n)] for _ in range(n)]

    # Fill dp table for all substring lengths
    for length in range(1, n + 1):
        # For each start position
        for i in range(n - length + 1):
            j = i + length - 1

            # Get substring from i to j
            substr = s[i:i+length]

            # Base case: length 1
            if length == 1:
                dp[i][j] = substr
                continue

            # Initialize with original string
            dp[i][j] = substr

            # Check if string can be encoded with pattern
            for k in range(1, length):
                if length % k == 0:
                    pattern = substr[:k] * (length // k)
                    if pattern == substr:
                        encoded = str(length // k) + '[' + dp[i][i+k-1] + ']'
                        if len(encoded) < len(dp[i][j]):
                            dp[i][j] = encoded

            # Try breaking string into two parts
            for k in range(i, j):
                left = dp[i][k]
                right = dp[k+1][j]
                if len(left) + len(right) < len(dp[i][j]):
                    dp[i][j] = left + right

    return dp[0][n-1]

# Test driver


def run_tests():
    test_cases = [
        {
            "s": "aaa",
            "expected": "3[a]",
            "explanation": "Original string length is 3, encoded is also 3"
        },
        {
            "s": "aabaabaa",
            "expected": "2[aaba]",
            "explanation": "Original length 8, encoded length 7"
        },
        {
            "s": "abbbabbbcabbbabbbc",
            "expected": "2[2[abbb]c]",
            "explanation": "Multiple levels of encoding possible"
        },
        {
            "s": "abcd",
            "expected": "abcd",
            "explanation": "Cannot be shortened by encoding"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = encode(test["s"])
        # Compare lengths to verify if result is valid
        is_valid = len(result) <= len(test["s"])
        status = "PASSED" if is_valid and (result == test["expected"] or len(
            result) <= len(test["expected"])) else "FAILED"

        print(f"Test {i}: {status}")
        print(f"Input string: {test['s']}")
        print(
            f"Expected: {test['expected']} (length: {len(test['expected'])})")
        print(f"Got: {result} (length: {len(result)})")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Encode String with Shortest Length problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Dynamic Programming Approach:
   - Use 2D DP table where dp[i][j] stores shortest encoded string for s[i:j+1]
   - For each substring length and starting position:
     * Try encoding with pattern repetition
     * Try splitting into two parts and combine their solutions

2. Key Optimizations:
   - Only check patterns that evenly divide substring length
   - Store computed results in DP table to avoid recalculation
   - Compare lengths to choose shorter encoding

3. Time Complexity: O(n³) where n is string length
   - Two nested loops for substring selection: O(n²)
   - Inner loop for pattern checking and splitting: O(n)

4. Space Complexity: O(n²) for DP table
"""
