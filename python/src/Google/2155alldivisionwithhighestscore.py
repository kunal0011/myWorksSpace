"""
LeetCode 2155 - All Divisions With the Highest Score of Binary Array

Problem Statement:
You are given a 0-indexed binary array nums of length n. You can divide nums at any index i 
(where 0 <= i <= n) into two arrays (possibly empty) numsleft and numsright:
- numsleft has all the elements from index 0 to i-1 (inclusive)
- numsright has all the elements from index i to n-1 (inclusive)
The division score of an index i is the sum of the number of 0's in numsleft and the number 
of 1's in numsright. Return all distinct indices that have the highest possible division score.

Time Complexity: O(n) where n is length of nums
Space Complexity: O(n) for storing prefix sums
"""


class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
        """
        Logic:
        1. Use prefix sums to efficiently calculate counts:
           - zeros[i] stores count of zeros from index 0 to i-1
           - ones[i] stores count of ones from index 0 to i-1
        2. For each division point i (0 to n):
           - Left part score = zeros[i]
           - Right part score = ones[n] - ones[i]
           - Total score = left + right
        3. Track maximum score and all indices achieving it

        Args:
            nums: Binary array (containing only 0s and 1s)
        Returns:
            List of indices achieving maximum division score
        """
        n = len(nums)
        max_score = -1
        scores = []

        # Calculate prefix sums of zeros and ones
        zeros = [0] * (n + 1)
        ones = [0] * (n + 1)

        for i in range(n):
            zeros[i + 1] = zeros[i] + (1 if nums[i] == 0 else 0)
            ones[i + 1] = ones[i] + (1 if nums[i] == 1 else 0)

        for i in range(n + 1):
            score = zeros[i] + (ones[n] - ones[i])
            if score > max_score:
                max_score = score
                scores = [i]
            elif score == max_score:
                scores.append(i)

        return scores


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'nums': [0, 0, 1, 0],
            'expected': [2, 4]
        },
        {
            'nums': [0, 0, 0],
            'expected': [3]
        },
        {
            'nums': [1, 1],
            'expected': [0]
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.maxScoreIndices(test['nums'])
        status = "PASSED" if result == test['expected'] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input: nums = {test['nums']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}\n")


if __name__ == "__main__":
    main()
