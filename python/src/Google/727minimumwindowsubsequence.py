"""
LeetCode 727: Minimum Window Subsequence

Problem Statement:
Given strings S and T, find the minimum (contiguous) substring W of S, such that T is a subsequence of W.
If there is no such window in S that covers all characters in T, return the empty string "".
If there are multiple such minimum-length windows, return the one with the leftmost starting index.

Logic:
1. Use sliding window technique with two pointers (left and right)
2. Keep track of character frequencies using Counter and defaultdict
3. For each character in S:
   - Update frequency count in sliding window
   - If current char matches required count in T, increment formed count
   - While we have all required characters:
     * Update minimum window if current window is smaller
     * Try to minimize window from left
     * Update frequency counts
4. Return the minimum window found or empty string if none exists

Time Complexity: O(|S| * |T|) - where |S| and |T| are lengths of strings
Space Complexity: O(k) - where k is the number of unique characters in T
"""

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        # Step 1: Initialize the character counts
        t_count = Counter(T)
        s_count = defaultdict(int)

        # Step 2: Initialize pointers and variables
        min_len = float('inf')
        min_window = ""
        left = 0
        required = len(t_count)
        formed = 0

        # Step 3: Start sliding window
        for right in range(len(S)):
            char = S[right]
            s_count[char] += 1

            if char in t_count and s_count[char] == t_count[char]:
                formed += 1

            while left <= right and formed == required:
                char = S[left]

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = S[left:right + 1]

                s_count[char] -= 1
                if char in t_count and s_count[char] < t_count[char]:
                    formed -= 1

                left += 1

        return min_window if min_len != float('inf') else ""


def test_minimum_window():
    solution = Solution()

    # Test case 1: Basic case
    S1, T1 = "abcdebdde", "bde"
    result1 = solution.minWindow(S1, T1)
    assert result1 == "bcde", f"Test case 1 failed. Expected 'bcde', got {result1}"
    print(f"Test case 1 passed: S = {S1}, T = {T1}, Result = {result1}")

    # Test case 2: Multiple occurrences
    S2, T2 = "abdabca", "abc"
    result2 = solution.minWindow(S2, T2)
    assert result2 == "abc", f"Test case 2 failed. Expected 'abc', got {result2}"
    print(f"Test case 2 passed: S = {S2}, T = {T2}, Result = {result2}")

    # Test case 3: No valid window
    S3, T3 = "xyz", "abc"
    result3 = solution.minWindow(S3, T3)
    assert result3 == "", f"Test case 3 failed. Expected '', got {result3}"
    print(f"Test case 3 passed: S = {S3}, T = {T3}, Result = {result3}")

    # Test case 4: Single character
    S4, T4 = "a", "a"
    result4 = solution.minWindow(S4, T4)
    assert result4 == "a", f"Test case 4 failed. Expected 'a', got {result4}"
    print(f"Test case 4 passed: S = {S4}, T = {T4}, Result = {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_minimum_window()
