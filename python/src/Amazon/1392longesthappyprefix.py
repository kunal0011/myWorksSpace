class Solution:
    def longestPrefix(self, s: str) -> str:
        # KMP algorithm to find the longest prefix which is also suffix
        n = len(s)
        lps = [0] * n  # Longest Prefix Suffix array
        length = 0     # Length of the previous longest prefix suffix
        i = 1

        # Build the LPS array
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return s[:lps[-1]]


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test 1
    s1 = "level"
    assert sol.longestPrefix(
        s1) == "l", f"Test case 1 failed, got {sol.longestPrefix(s1)}"

    # Test 2
    s2 = "ababab"
    assert sol.longestPrefix(
        s2) == "abab", f"Test case 2 failed, got {sol.longestPrefix(s2)}"

    # Test 3
    s3 = "leetcodeleet"
    assert sol.longestPrefix(
        s3) == "leet", f"Test case 3 failed, got {sol.longestPrefix(s3)}"

    print("All test cases passed!")
