from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        # lengths[i] will be the length of the longest subsequence ending at i
        lengths = [1] * n
        counts = [1] * n   # counts[i] will be the number of such subsequences

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        # The length of the longest increasing subsequence
        longest = max(lengths)

        # Sum up the counts of subsequences of the longest length
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 3, 5, 4, 7]
    print(sol.findNumberOfLIS(nums1))  # Output: 2

    # Test case 2
    nums2 = [2, 2, 2, 2, 2]
    print(sol.findNumberOfLIS(nums2))  # Output: 5
