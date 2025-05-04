"""
LeetCode 1461. Check If a String Contains All Binary Codes of Size K

Problem Statement:
Given a binary string s and an integer k, return true if every binary code of length k is 
a substring of s. Otherwise, return false.
For example, if k=2, all possible binary codes are: "00", "01", "10", "11".

Time Complexity: O(n*k) where n is length of string and k is the size of binary code
Space Complexity: O(2^k) to store all possible combinations
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Logic:
        # 1. Calculate total possible binary codes of length k (2^k)
        # 2. Use sliding window of size k to get all substrings
        # 3. Store unique substrings in a set
        # 4. If set size equals 2^k, we found all possible codes

        required = 1 << k  # Total number of binary codes of length k (2^k)
        seen = set()

        # Use sliding window to check all substrings of length k
        for i in range(k, len(s) + 1):
            seen.add(s[i-k:i])
            if len(seen) == required:
                return True
        return False


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("00110110", 2),    # Expected: True (contains "00","01","10","11")
        ("0110", 1),        # Expected: True (contains "0","1")
        ("0110", 2),        # Expected: False (missing "00")
        ("00110", 2),       # Expected: True
        ("0000000001", 10)  # Expected: False
    ]

    for i, (s, k) in enumerate(test_cases):
        result = solution.hasAllCodes(s, k)
        print(f"Test case {i + 1}:")
        print(f"String: {s}")
        print(f"k: {k}")
        print(f"Contains all binary codes: {result}")
        print()
