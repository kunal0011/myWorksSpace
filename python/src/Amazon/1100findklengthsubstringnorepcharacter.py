class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):  # If k is larger than the string, return 0
            return 0

        char_set = set()
        count = 0
        left = 0

        # Sliding window approach
        for right in range(len(s)):
            # Slide the window until we remove repeated characters
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            # Check if the current window size is k
            if right - left + 1 == k:
                count += 1
                # Slide the window by removing the leftmost character
                char_set.remove(s[left])
                left += 1

        return count

# Testing the implementation


def test_num_k_len_substr_no_repeats():
    solution = Solution()

    # Test case 1
    s1 = "havefunonleetcode"
    k1 = 5
    # Expected output: 6 (Valid substrings: "havef", "avefu", "vefun", "efuno", "etcod", "tcode")
    result1 = solution.numKLenSubstrNoRepeats(s1, k1)
    print(f"Test 1 - Result: {result1}, Expected: 6")

    # Test case 2
    s2 = "abcd"
    k2 = 3
    # Expected output: 2 (Valid substrings: "abc", "bcd")
    result2 = solution.numKLenSubstrNoRepeats(s2, k2)
    print(f"Test 2 - Result: {result2}, Expected: 2")

    # Test case 3
    s3 = "aa"
    k3 = 1
    # Expected output: 2 (Valid substrings: "a", "a")
    result3 = solution.numKLenSubstrNoRepeats(s3, k3)
    print(f"Test 3 - Result: {result3}, Expected: 2")


# Run the test
test_num_k_len_substr_no_repeats()
