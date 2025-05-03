"""
LeetCode 482: License Key Formatting

Problem Statement:
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group,
which could be shorter than k but still must contain at least one character. Furthermore:
- All the letters in the string should be converted to uppercase.
- The reformed string should only contain alphanumeric characters and dashes.
- Each group should contain exactly k characters, except for the first group.
- The groups should be separated by dashes.

Return the reformatted license key.

Constraints:
- 1 <= s.length <= 10^5
- s consists of English letters, digits, and dashes '-'
- 1 <= k <= 10^4
"""


def licenseKeyFormatting(s: str, k: int) -> str:
    # Remove all dashes and convert to uppercase
    s = s.replace('-', '').upper()

    n = len(s)
    if n == 0:
        return ""

    # Calculate length of first group
    first_group_len = n % k if n % k != 0 else k

    # Build result string
    result = []

    # Add first group
    result.append(s[:first_group_len])

    # Add remaining groups
    for i in range(first_group_len, n, k):
        result.append(s[i:i+k])

    # Join groups with dashes
    return '-'.join(result)

# Test driver


def run_tests():
    test_cases = [
        {
            "s": "5F3Z-2e-9-w",
            "k": 4,
            "expected": "5F3Z-2E9W",
            "explanation": "The string is split into 2 groups of size 4"
        },
        {
            "s": "2-5g-3-J",
            "k": 2,
            "expected": "2-5G-3J",
            "explanation": "The string is split into 3 groups: '2', '5G', '3J'"
        },
        {
            "s": "---",
            "k": 3,
            "expected": "",
            "explanation": "Empty string after removing dashes"
        },
        {
            "s": "a-a-a-a-",
            "k": 1,
            "expected": "A-A-A-A",
            "explanation": "Each character in its own group"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = licenseKeyFormatting(test["s"], test["k"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input string: '{test['s']}'")
        print(f"k: {test['k']}")
        print(f"Expected: '{test['expected']}'")
        print(f"Got: '{result}'")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for License Key Formatting problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Key Approach:
   - Remove all dashes and convert to uppercase first
   - Calculate first group length based on total length and k
   - Split remaining characters into groups of k
   - Join groups with dashes

2. Optimizations:
   - Process string in one pass to remove dashes and convert case
   - Use list for building result (more efficient than string concatenation)
   - Handle empty string case early

3. Time Complexity: O(n) where n is length of input string
   - Single pass for preprocessing
   - Single pass for grouping

4. Space Complexity: O(n)
   - Need to store processed string and result
"""
