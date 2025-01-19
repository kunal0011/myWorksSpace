"""
Problem 14: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Logic:
1. If the array is empty, return empty string
2. Take first string as initial prefix
3. For each character in this prefix:
   - Check if this character exists at same position in all other strings
   - If not, return prefix up to current position
4. Return the entire prefix if all characters match

Time Complexity: O(S) where S is sum of all characters in all strings
Space Complexity: O(1) as we only store the prefix

Alternative Approaches:
1. Horizontal scanning (current implementation)
2. Vertical scanning
3. Divide and conquer
4. Binary search
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: empty array
        if not strs:
            return ""

        # Take first string as initial prefix
        prefix = strs[0]

        # Check each character of prefix against all other strings
        for i in range(len(prefix)):
            for string in strs:
                # If current index is beyond string length or characters don't match
                if i >= len(string) or string[i] != prefix[i]:
                    return prefix[:i]

        return prefix


def test_longest_common_prefix():
    solution = Solution()

    # Test cases: (input_array, expected_result, description)
    test_cases = [
        (["flower", "flow", "flight"], "fl", "Basic case with common prefix"),
        (["dog", "racecar", "car"], "", "No common prefix"),
        (["interspecies", "interstellar", "interstate"],
         "inters", "Longer common prefix"),
        (["throne", "throne"], "throne", "Identical strings"),
        ([""], "", "Single empty string"),
        (["a"], "a", "Single character"),
        (["", "b"], "", "Empty string in array"),
        ([], "", "Empty array"),
        (["prefix", "prefix", "prefix"], "prefix", "All strings identical"),
        (["abc", "ab", "a"], "a", "Decreasing length strings")
    ]

    print("\nRunning Longest Common Prefix Tests:")
    print("=" * 50)

    passed = 0
    total = len(test_cases)

    for i, (strings, expected, desc) in enumerate(test_cases, 1):
        result = solution.longestCommonPrefix(strings)
        status = "PASS" if result == expected else "FAIL"
        color = "\033[92m" if status == "PASS" else "\033[91m"

        print(f"\nTest Case {i}: {desc}")
        print(f"Input Strings: {strings}")
        print(f"Expected: '{expected}'")
        print(f"Got: '{result}'")
        print(f"Status: {color}{status}\033[0m")

        if result == expected:
            passed += 1

    print("\n" + "=" * 50)
    print(f"\nTest Summary:")
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    success_rate = (passed / total) * 100
    print(f"Success Rate: {success_rate:.2f}%")


def visualize_algorithm():
    """
    Demonstrates how the algorithm works with a simple example
    """
    example = ["flower", "flow", "flight"]
    print("\nAlgorithm Visualization:")
    print("=" * 50)
    print(f"Input strings: {example}")
    print("\nStep-by-step process:")

    prefix = example[0]
    print(f"1. Take first string as prefix: '{prefix}'")

    for i in range(len(prefix)):
        print(f"\nChecking position {i} ('{prefix[i]}')")
        for j, string in enumerate(example):
            if i >= len(string) or string[i] != prefix[i]:
                print(f"  - Mismatch or end of string at position {i}")
                print(f"  - Final result: '{prefix[:i]}'")
                return
            print(f"  - Matches in string {j+1}: '{string}'")

    print(f"\nAll characters matched. Final result: '{prefix}'")


if __name__ == "__main__":
    test_longest_common_prefix()
    print("\n")
    visualize_algorithm()
