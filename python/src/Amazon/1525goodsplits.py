from collections import defaultdict


class Solution:
    def numSplits(self, s: str) -> int:
        left_count = defaultdict(int)
        right_count = defaultdict(int)

        # Step 1: Count distinct characters for the right part (initially the whole string)
        for char in s:
            right_count[char] += 1

        left_distinct = 0
        right_distinct = len(right_count)
        good_splits = 0

        # Step 2: Iterate through the string
        for i in range(len(s)):
            # Add current character to the left part
            left_count[s[i]] += 1
            if left_count[s[i]] == 1:
                left_distinct += 1

            # Remove current character from the right part
            right_count[s[i]] -= 1
            if right_count[s[i]] == 0:
                right_distinct -= 1

            # Compare distinct counts
            if left_distinct == right_distinct:
                good_splits += 1

        return good_splits


# Testing
solution = Solution()
s = "aacaba"
print("Python Test Result:", solution.numSplits(s))  # Output should be 2
