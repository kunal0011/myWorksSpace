class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Edge case for empty string
        if not s:
            return 0

        # Dictionary to store the count of each character in the window
        char_count = {}
        l = 0  # Left pointer
        max_len = 0

        # Expand the window with the right pointer
        for r in range(len(s)):
            # Add character at s[r] to the window
            char_count[s[r]] = char_count.get(s[r], 0) + 1

            # If there are more than two distinct characters, shrink the window
            while len(char_count) > 2:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    # Remove the character from the map if its count is 0
                    del char_count[s[l]]
                l += 1  # Move the left pointer to the right

            # Calculate the max length of the window
            max_len = max(max_len, r - l + 1)

        return max_len

# Test cases


def test_lengthOfLongestSubstringTwoDistinct():
    sol = Solution()

    # Test Case 1
    assert sol.lengthOfLongestSubstringTwoDistinct(
        "eceba") == 3, "Test Case 1 Failed"  # "ece"

    # Test Case 2
    assert sol.lengthOfLongestSubstringTwoDistinct(
        "ccaabbb") == 5, "Test Case 2 Failed"  # "aabbb"

    # Test Case 3
    assert sol.lengthOfLongestSubstringTwoDistinct(
        "abcabcabc") == 2, "Test Case 3 Failed"  # "ab"

    # Test Case 4
    assert sol.lengthOfLongestSubstringTwoDistinct(
        "a") == 1, "Test Case 4 Failed"  # "a"

    # Test Case 5
    assert sol.lengthOfLongestSubstringTwoDistinct(
        "ababffzzeee") == 5, "Test Case 5 Failed"  # "zzeee"

    print("All test cases passed!")


# Run the tests
test_lengthOfLongestSubstringTwoDistinct()
